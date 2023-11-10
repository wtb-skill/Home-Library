from flask import Flask, jsonify, abort, make_response, request, g
from api_models import APIBooks

app = Flask(__name__)
app.config.from_pyfile('config.py')


def create_books_instance():
    return APIBooks()


@app.before_request
def before_request():
    # Create a new instance of Books before each request
    g.books = create_books_instance()


@app.teardown_request
def teardown_request(exception=None):
    # Cleanup after each request
    g.pop('books', None)


@app.route("/api/v1/books/", methods=["GET"])
def list_books_api_v1():
    return jsonify(g.books.all())


@app.route("/api/v1/books/<int:book_id>", methods=["GET"])
def get_book_api_v1(book_id):
    book = g.books.get(book_id)
    if not book:
        abort(404)
    return jsonify({"book": book})


@app.route("/api/v1/books/", methods=["POST"])
def create_book_api_v1():
    if not request.json or 'title' not in request.json or 'author' not in request.json:
        abort(400)
    book = {
        'id': g.books.all()[-1]['id'] + 1 if g.books.all() else 1,
        'title': request.json['title'],
        'author': request.json['author'],
        'description': request.json.get('description', ""),
        'read': False
    }
    g.books.create2(book)
    return jsonify({'book': book}), 201


@app.route("/api/v1/books/<int:book_id>", methods=['DELETE'])
def delete_book_api_v1(book_id):
    result = g.books.delete(book_id)
    if not result:
        abort(404)
    return jsonify({'result': result})


@app.route("/api/v1/books/<int:book_id>", methods=["PUT"])
def update_book_api_v1(book_id):
    book = g.books.get(book_id)
    if not book:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'author' in data and not isinstance(data.get('author'), str),
        'description' in data and not isinstance(data.get('description'), str),
        'read' in data and not isinstance(data.get('read'), bool)
    ]):
        abort(400)

    # Update fields
    book['title'] = data.get('title', book['title'])
    book['author'] = data.get('author', book['author'])
    book['description'] = data.get('description', book['description'])
    book['read'] = data.get('read', book['read'])

    g.books.update(book_id, book)
    return jsonify({'book': book})


# Error Handlers:
@app.errorhandler(404)
def handle_not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)


@app.errorhandler(400)
def handle_bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)
