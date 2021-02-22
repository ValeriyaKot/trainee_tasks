from enum import Enum
from collections import defaultdict
from datetime import datetime
import sys


class Genre(Enum):
    History = 1
    Horror = 2
    Adventure = 3
    Fantasy = 4
    Romance = 5


class Author:
    def __init__(self, first_name, surname, birthday):
        self.first_name = first_name
        self.surname = surname
        self.__birthday = birthday

    def __str__(self):
        return '{} {}'.format(self.first_name, self.surname)

    def __hash__(self):
        return hash(str(self))

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, new_date):
        b_date = new_date.split('.')
        b_date = [int(el) for el in b_date]
        b_date = datetime(b_date[2], b_date[1], b_date[0])
        today = datetime.now()
        if b_date > today:
            raise ValueError
        else:
            self.__birthday = new_date


class Book:
    def __init__(self, genre, name, publishing_house, year_of_publication, author=None):
        self.genre = genre
        self._name = name
        self.publication_house = publishing_house
        self.year_of_publication = year_of_publication
        self.author = author

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.genre, self._name, self.year_of_publication,
                                           self.publication_house, self.author)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return self.genre == other.genre

    @property
    def name(self):
        return self._name


class Library:
    def __init__(self, phone_number, books=None):
        self.__phone_number = phone_number
        self.books = (defaultdict(int, books)
                      if books is not None
                      else defaultdict(int))

    def __str__(self):
        return str(['{}: {}'.format(v, k) for k, v in self.books.items()])

    def __getitem__(self, key):
        return self.books[key]

    def __setitem__(self, key, value):
        self.books[key] = value

    def __delitem__(self, key):
        del self.books[key]

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, number):
        if len(str(number)) != 5:
            raise ValueError
        else:
            self.__phone_number = number

    @staticmethod
    def write_csv(books_dict, destination_file_path):
        with open(destination_file_path, 'w') as f_obj:
            csv_text = 'Genre, Book, Year of publication, Publishing house, Author, Quantity'
            for k, v in books_dict.items():
                csv_text += '\n{}, {}'.format(k, v)
            f_obj.write(csv_text)

    def sort_by_name(self):
        return sorted(self.books.keys(), key=lambda key: key.name)

    def sort_by_author(self):
        return sorted(self.books.keys(), key=lambda key: key.author.surname)

    def filter_name(self, name):
        return list(filter(lambda key: name.title() in key.name, [key for key in self.books.keys()]))

    def filter_authors_surname(self, surname):
        return list(filter(lambda key: surname.title() in key.author.surname, [key for key in self.books.keys()]))

    def filter_year_of_publication(self, year):
        return list(filter(lambda key: str(year) in str(key.year_of_publication), [key for key in self.books.keys()]))

    def filter_genre(self, genre):
        return list(filter(lambda key: genre.title() in key.genre.name, [key for key in self.books.keys()]))


if __name__ == "__main__":
    history = Genre.History
    horror = Genre.Horror
    fantasy = Genre.Fantasy
    romance = Genre.Romance
    adventure = Genre.Adventure

    liz_twist = Author('Liz', 'Twist', '12.03.1950')
    david_di = Author('David', 'Di', '03.04.1940')
    tom_vil = Author('Tom', 'Vil', '10.02.1910')
    jerry_chu = Author('Jerry', 'Chu', '13.09.1930')
    ann_mary = Author('Ann', 'Mary', '17.11.1950')

    second_planet = Book(history, 'Second planet', 'DWD', 1980, liz_twist)
    blue_flower = Book(fantasy, 'Blue Flower', 'DWD', 1970, ann_mary)
    black_glass = Book(horror, 'Black glass', 'F&S', 1950, jerry_chu)
    island = Book(adventure, 'Island', 'Big.Co', 1977, david_di)
    madonna = Book(romance, 'Madonna', 'Big.Co', 1980, tom_vil)
    six_birds = Book(horror, 'Six birds', 'F&S', 1951, jerry_chu)

    library = Library(99089, {second_planet: 1, black_glass: 4, blue_flower: 10, island: 2, madonna: 5, six_birds: 2})

    liz_twist.birthday = '12.03.1947'
    library.phone_number = 99904

    del library[madonna]

    print(liz_twist.birthday)
    print(library.phone_number)

    sort_by_name = library.sort_by_name()
    print([str(book) for book in sort_by_name])

    sort_by_author = library.sort_by_author()
    print([str(book) for book in sort_by_author])

    filter_by_name = library.filter_name('island')
    print([str(book) for book in filter_by_name])

    filter_authors_surname = library.filter_authors_surname('chu')
    print([str(book) for book in filter_authors_surname])

    filter_genre = library.filter_genre('Horror')
    print([str(book) for book in filter_genre])

    filter_year_of_publication = library.filter_year_of_publication('1980')
    print([str(book) for book in filter_year_of_publication])

    Library.write_csv(library.books, sys.argv[1])
