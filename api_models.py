import json
from random import randint


class APIBooks:
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
        book = [book for book in self.all() if book['id'] == _id]
        if book:
            return book[0]
        return []

    def create2(self, data):
        self.books.append(data)
        self.save_all()
        self.size += 1

    def save_all(self):
        with open("books.json", "w") as file:
            json.dump(self.books, file)

    def update(self, _id, data):
        book = self.get(_id)
        if book:
            index = self.books.index(book)
            self.books[index] = data
            self.save_all()
            return True
        return False

    def choose_random(self):
        rng = randint(0, self.size - 1)
        chosen_book = self.books[rng]
        return chosen_book

    def delete(self, _id):
        book = self.get(_id)
        if book:
            self.books.remove(book)
            self.save_all()
            return True
        return False











