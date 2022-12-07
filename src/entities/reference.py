from bibtexparser.bibdatabase import BibDatabase

class Reference:
    def __init__(self, type, id, title, author, year=None,
    publisher=None, journal=None, school=None, institution=None, note=None):
        self._id = id
        self._type = type
        self._title = title
        self._author = author
        try:
            self._year = int(year)
        except:
            self._year = None
        self._publisher = publisher
        self._journal = journal
        self._school  = school
        self._institution = institution
        self._note = note

    def create_bibtex_entry(self):
        if self._type == 'kirja':
            return None
        if self._type == 'lehtiartikkeli':
            bibtex_entry = BibDatabase()
            bibtex_entry.entries = [
            {"title": self._title,
            "author": self._author,
            "year": str(self._year),
            "journal": self._journal,
            "ENTRYTYPE": "article",
            "ID": self._id}]
            return bibtex_entry
        if self._type == 'gradu':
            return None
        if self._type == 'tutkimusraportti':
            return None
        return None

    def __str__(self):
        if self._type == 'kirja':
            return f"{self._author}. {self._year}. {self._title}. {self._publisher}."
        if self._type == 'lehtiartikkeli':
            return f"{self._author}. {self._year}. {self._title}. {self._journal}."
        if self._type == 'gradu':
            return f"{self._author}. {self._year}. {self._title}. {self._school}."
        if self._type == 'tutkimusraportti':
            return f"{self._author}. {self._year}. {self._title}. {self._institution}."
        if self._year is not None:
            return f"{self._author}. {self._year}. {self._title}. {self._note}."
        return f"{self._author}. {self._title}. {self._note}."
