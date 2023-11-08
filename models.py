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
        return self.books[_id]

    def create(self, data):
        data.pop('csrf_token')
        self.books.append(data)
        self.size += 1

    def save_all(self):
        with open("books.json", "w") as file:
            json.dump(self.books, file)

    def update(self, _id, data):
        data.pop('csrf_token')
        self.books[_id] = data
        self.save_all()

    def choose_random(self):
        rng = randint(0, self.size - 1)
        chosen_book = self.books[rng]
        return chosen_book


books = Books()
