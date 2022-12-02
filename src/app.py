import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from entities.book import Book

class CommandLineUI:
    def __init__(self, io):
        self._io = io
        self._run = True
        self._references = []

    def start_app(self):
        self._io.write("Tervetuloa viitekirjastoon!")
        while self._run is True:
            user_input = self._io.read("Mitä haluat tehdä? [lisää viite/listaa viitteet/poistu] ")

            if user_input == "lisää viite":
                reference = self._io.read("Minkälainen viite lisätään? [kirja] ")
                if reference not in self._references:
                    self._references.append(reference)
                self.add_reference(reference)

            elif user_input == "listaa viitteet":
                self.read_from_bib_file()

            elif user_input == "poistu":
                self._run = False

            else:
                self._io.write("Virheellinen syöte.")

    def add_reference(self, reference):
        self._io.write("Syötä viitteen tiedot:")
        title = self._io.read("Kirjan nimi: ")
        author = self._io.read("Kijailija: ")
        year = int(self._io.read("Julkaisuvuosi: "))
        publisher = self._io.read("Julkaisija: ")
        keyword = self._io.read("Avainsana, jolla haluat viitata teokseen: ")
        self._io.write(f"Lisätään {reference} {title} ({year}), kirjoittanut {author}, julkaissut {publisher}, avainsanalla {keyword}")

        data = (reference, title, author, year, publisher, keyword)
        self.write_to_bib_file(data)

    def write_to_bib_file(self, data):
        db = BibDatabase()
        db.entries = [
            {"title": str(data[1]),
            "author": str(data[2]),
            "year": str(data[3]),
            "publisher": str(data[4]),
            "ID": str(data[5]),
            "ENTRYTYPE": "book"}]

        writer = BibTexWriter()
        writer.indent = "    "
        with open("references.bib", "a") as bibfile:
            bibfile.write(writer.write(db))
        self._io.write("BibTex tiedoston kirjoittaminen onnistui")

    def read_from_bib_file(self):
        with open("references.bib") as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
        for entry in bib_database.entries:
            self._io.write(f'{entry["author"]}, {entry["title"]}. {entry["publisher"]}, {entry["year"]}.')
