class Book:
    def __init__(self, author, title, publisher, year):
        self._author = author
        self._title = title
        self._publisher = publisher
        self._year = year

    def __str__(self):
        return f"{self._author}, {self._title}. {self._publisher}, {self._year}."
