import json
from random import randint


class Books:
    def __init__(self):
        try:
            with open("books.json", "r") as file:
                self.books = json.load(file)
        except FileNotFoundError:
            self.books = []

        self.size = len(self.books)

    def all(self):
        return self.books

    def get(self, _id):
        book = [book for book in self.all() if book['id'] == int(_id)]
        if book:
            return book[0]
        return []

    def create(self, data):
        print("BOOKS")
        data.pop('csrf_token')
        data['id'] = int(data.get('id', 0))
        self.books.append(data)
        self.size += 1

    def save_all(self):
        with open("books.json", "w") as file:
            json.dump(self.books, file)

    def update(self, _id, data):
        data.pop('csrf_token')
        book = self.get(_id)
        if book:
            index = self.books.index(book)
            self.books[index] = data
            self.save_all()
            return True
        return False

    def choose_random(self):
        unread_books = [book for book in self.books if not book['read']]
        if unread_books:
            rng = randint(0, len(unread_books) - 1)
            chosen_book = unread_books[rng]
            return chosen_book['id']

    def delete(self, _id):
        book = self.get(_id)
        if book:
            self.books.remove(book)
            self.save_all()
            return True
        return False

    def sort_by_title(self):
        sorted_books = sorted(self.books, key=lambda x: x['title'])
        return sorted_books

    def sort_by_author(self):
        sorted_books = sorted(self.books, key=lambda x: x['author'])
        return sorted_books

    def sort_by_read(self):
        sorted_books = sorted(self.books, key=lambda x: x['read'])
        return sorted_books







