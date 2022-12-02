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
                self.read_from_csv_file()

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

        # poistetaan kun ei tarvita enää csv
        data = f"{author};{title};{publisher};{year}\n"
        self.write_to_csv_file(data, reference)
        #

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
        with open("references.bib", "a") as bibfile:
            bibfile.write(writer.write(db))
        self._io.write("BibTex tiedoston kirjoittaminen onnistui")

    def write_to_csv_file(self, data, reference):
        with open(f"{reference}.csv", "a", encoding="UTF8") as file:
            file.write(data)

    def read_from_csv_file(self):
        for reference in self._references:
            with open(f"{reference}.csv", "r", encoding="UTF8") as file:
                for line in file:
                    line = line.replace("\n", "")
                    parts = line.split(";")
                    book = Book(parts[0], parts[1], parts[2], parts[3])
                    self._io.write(book)
