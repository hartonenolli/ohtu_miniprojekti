from bibtexparser.bibdatabase import BibDatabase

class Reference:
    def __init__(self, ref_type, key, title, author, year=None,
    publisher=None, journal=None, school=None, institution=None, note=None):
        self._id = key
        self._type = ref_type
        self._title = title
        self._author = author
        try:
            self._year = int(year)
        except ValueError:
            self._year = None
        self._publisher = publisher
        self._journal = journal
        self._school  = school
        self._institution = institution
        self._note = note

    def create_bibtex_entry(self):
        bibtex_entry = BibDatabase()
        if self._type == 'kirja':
            bibtex_entry.entries = [
            {"title": self._title,
            "author": self._author,
            "year": str(self._year),
            "publisher": self._publisher,
            "ENTRYTYPE": "book",
            "ID": self._id}]
        elif self._type == 'lehtiartikkeli':
            bibtex_entry.entries = [
            {"title": self._title,
            "author": self._author,
            "year": str(self._year),
            "journal": self._journal,
            "ENTRYTYPE": "article",
            "ID": self._id}]
        elif self._type == 'gradu':
            bibtex_entry.entries = [
            {"title": self._title,
            "author": self._author,
            "year": str(self._year),
            "school": self._school,
            "ENTRYTYPE": "mastersthesis",
            "ID": self._id}]
        elif self._type == 'tutkimusraportti':
            bibtex_entry.entries = [
            {"title": self._title,
            "author": self._author,
            "year": str(self._year),
            "institution": self._institution,
            "ENTRYTYPE": "techreport",
            "ID": self._id}]
        else:
            bibtex_entry.entries = [
            {"title": self._title,
            "author": self._author,
            "year": str(self._year),
            "note": self._note,
            "ENTRYTYPE": "unpublished",
            "ID": self._id}]
        return bibtex_entry

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
