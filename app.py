from flask import Flask, request, render_template, redirect, url_for

from forms import BooksForm
from models import books

app = Flask(__name__)
app.config["SECRET_KEY"] = "verySECRETkey"


@app.route("/menu", methods=["GET", "POST"])
def library_menu():
    return render_template("menu.html")


@app.route("/add_book", methods=["GET", "POST"])
def library_add_book():
    form = BooksForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            books.create(form.data)
            books.save_all()
        return redirect(url_for("library_menu"))

    return render_template("add_book.html", form=form, error=error)


@app.route("/display", methods=["GET", "POST"])
def library():
    form = BooksForm()
    return render_template("display.html", form=form, books=books.all())


@app.route("/display/<int:book_id>/", methods=["GET", "POST"])
def details(book_id):
    book = books.get(book_id - 1)
    form = BooksForm(data=book)

    if request.method == "POST":
        if form.validate_on_submit():
            books.update(book_id - 1, form.data)
            return redirect(url_for("library"))
    return render_template("edit.html", form=form, books=books.all(), book_id=book_id)


if __name__ == "__main__":
    app.run(debug=True)
