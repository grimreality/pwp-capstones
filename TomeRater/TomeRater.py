from statistics import mean
import re


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
        assert("@" in email and re.search(".com|.edu|.org", email)), "Invalid"

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Your email has been changed to " + address)
        assert ("@" in email and re.search(".com|.edu|.org", email)), "Invalid"

    def __repr__(self):
        return "User : " + self.name + " , Email : " + self.email + " , Books read : " + str(len(self.books))

    def __eq__(self, other_user):
        if self is other_user:
            return True
        else:
            return self.name == other_user.name

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        average = 0
        total_ratings = 0
        for book in self.books:
            if self.books[book] is not None:
                average += self.books[book]
                total_ratings += 1
        return average/total_ratings

    def __hash__(self):
        return hash((self.name, self.email))


class Book(object):

    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        return "ISBN has been set to" + str(self.isbn)

    def add_rating(self, rating):
            if rating >= 0 and rating <= 4:
                self.ratings.append(rating)
            else:
                return "Invalid Rating."

    def get_average_rating(self):
        average = 0
        count = 0
        for rating in self.ratings:
            count += 1
            average += rating

        return average / count

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __eq__(self, other):
        if self is other:
            return True
        else:
            return self.title == other.title


class Fiction(Book):

    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        print("{title} by {author}".format(title=self.title, author=self.author))


class NonFiction(Book):

    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)


class TomeRater(object):

    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_novel = Fiction(title, author, isbn)
        return new_novel

    def create_non_fiction(self, title, subject, level, isbn):
        new_nf = NonFiction(title, subject, level, isbn)
        return new_nf

    def add_book_to_user(self, book, email, rating=None):
        if email not in self.users:
            print("No one with that email.")
            return False
        self.users[email].read_book(book, rating)
        if rating is not None:
            book.add_rating(rating)
        if book not in self.books:
            self.books[book] = 1
        else:
            self.books[book] += 1

    def add_user(self, name, email, user_books=None):
        self.users[email] = User(name, email)
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books:
            print(book.title)

    def print_users(self):
        for user in self.users:
            print(user)

    def most_read_book(self):
        book = ""
        amount = 0
        for i in self.books.keys():
            if i.get_average_rating() > amount:
                book = i.title
                amount = self.books[i]
        return book

    def highest_rated_book(self):
        average = {}
        for book in self.books:
            average[book] = book.get_average_rating()
        highest = max(average.values())
        highest_book = [book for book, rating in average.items() if rating == highest]
        print("{} is the best with an exceptional rating of {}".format(highest_book, highest))

    def most_positive_user(self):
        average_rating = {}
        for user in self.users.values():
            average_rating[user] = user.get_average_rating()
        high_rating = max(average_rating.values())
        happiest_user = [user for user, rating in average_rating.items() if rating == high_rating]
        print("{} is such a positive human being with an average rating of {}".format(happiest_user, high_rating))









