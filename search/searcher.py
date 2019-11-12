#!/usr/bin/env python3

import ast


class Linear:

    def __init__(self):
        print("Constructing a Linear Search Object")
        self.data = {}

    def load_data(self):
        with open('./bookshelf-data.dat', 'r') as f:
            s = f.read()
            self.data = ast.literal_eval(s)

    def search(self, value):
        for index, book in enumerate(self.data):
            print("Loop #{}".format(index))

            if book['title'] == value:
                print(book)

    def print_data(self):
        for book in self.data:
            print(book)


class BetterLinear:
    def __init__(self):
        print("Constructing a Better Linear Search Object")
        self.data = {}

    def load_data(self):
        with open('./bookshelf-data.dat', 'r') as f:
            s = f.read()
            self.data = ast.literal_eval(s)

    def search(self, value):
        for index, book in enumerate(self.data):
            print("Loop #{}".format(index))

            if book['title'] == value:
                print(book)
                break

    def print_data(self):
        for book in self.data:
            print(book)
