from flask import Flask, request, render_template, redirect, url_for, g, flash
from flask_wtf.csrf import CSRFProtect
from forms import BooksForm
from models import Books
from api_routes import list_books_api_v1, get_book_api_v1, create_book_api_v1, delete_book_api_v1, update_book_api_v1, \
    choose_unread_book_api_v1, handle_not_found, handle_bad_request

app = Flask(__name__)
app.config.from_pyfile('config.py')
# csrf = CSRFProtect(app)


def create_books_instance():
    return Books()


@app.before_request
def before_request():
    g.books = create_books_instance()


@app.teardown_request
def teardown_request(exception=None):
    # Cleanup after each request
    g.pop('books', None)


@app.route("/", methods=["GET"])
def library_menu():
    return render_template("menu.html")


@app.route("/books/add/", methods=["GET", "POST"])
def library_add_book():
    form = BooksForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            book_id = g.books.all()[-1]['id'] + 1 if g.books.all() else 1
            form.set_id(book_id)
            g.books.create(form.data)
            flash('Book successfully added!', 'success')
        return redirect(url_for("library_menu"))

    return render_template("add_book.html", form=form, error=error)


# @app.route("/books/", methods=["GET"])
# def library():
#     form = BooksForm()
#     return render_template("display.html", form=form, books=g.books.all())

# @app.route("/books/", methods=["GET"])
# def library():
#     form = BooksForm()
#     sort_method = request.args.get("sort")
#
#     books = g.books.sort_books(sort_method) if sort_method in ["title", "author", "read"] else g.books.all()
#     return render_template("display.html", form=form, books=books)


@app.route("/books/", methods=["GET"])
def library():
    form = BooksForm()
    sort_method = request.args.get("sort", default="")

    if sort_method in ["title", "author", "read"]:
        books = getattr(g.books, f"sort_by_{sort_method}")()
    else:
        books = g.books.all()

    return render_template("display.html", form=form, books=books)


@app.route("/books/<int:book_id>/", methods=["GET", "POST"])
def details(book_id):
    book_id = int(book_id)
    book = g.books.get(book_id)
    form = BooksForm(data=book)

    if request.method == "POST":
        if form.validate_on_submit():
            form.set_id(book_id)
            g.books.update(book_id, form.data)
            flash('Book successfully edited!', 'success')
            return redirect(url_for("library"))
    return render_template("edit.html", form=form, books=g.books.all(), book_id=book_id)


@app.route("/choose_unread_book/", methods=["GET"])
def choose_unread_book():
    chosen_book_id = g.books.choose_random()

    if chosen_book_id is not None:
        chosen_book = g.books.get(chosen_book_id)
        form = BooksForm(data=chosen_book)

        return render_template("edit.html", form=form, books=g.books.all(), book_id=chosen_book_id)
    else:
        flash("No unread books available", "error")
        return redirect(url_for("library_menu"))


@app.route("/api/", methods=["GET"])
def list_routes():
    routes = []

    for rule in app.url_map.iter_rules():
        readable_methods = rule.methods
        readable_methods.discard('OPTIONS')
        readable_methods.discard('HEAD')
        methods = ', '.join(readable_methods)
        routes.append({"endpoint": rule.endpoint, "methods": methods, "path": str(rule)})

    return {"routes": routes}


# REST API routes
app.add_url_rule('/api/v1/books/', 'list_books_api_v1', list_books_api_v1)
app.add_url_rule('/api/v1/books/choose_unread_book/', 'choose_unread_book_api_v1', choose_unread_book_api_v1)
app.add_url_rule('/api/v1/books/<int:book_id>', 'get_book_api_v1', get_book_api_v1)
app.add_url_rule('/api/v1/books/', 'create_book_api_v1', create_book_api_v1, methods=['POST'])
app.add_url_rule('/api/v1/books/<int:book_id>', 'delete_book_api_v1', delete_book_api_v1, methods=['DELETE'])
app.add_url_rule('/api/v1/books/<int:book_id>', 'update_book_api_v1', update_book_api_v1, methods=['PUT'])

# Define error handlers
app.register_error_handler(404, handle_not_found)
app.register_error_handler(400, handle_bad_request)


if __name__ == "__main__":
    app.run(debug=True)
