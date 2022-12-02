import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from entities.book import Book

class BibtexController:
    def __init__(self):
        pass

    def _create_bibtex_format(self, data):
        bibtex_entry = BibDatabase()
        bibtex_entry.entries = [
            {"title": str(data[1]),
            "author": str(data[2]),
            "year": str(data[3]),
            "publisher": str(data[4]),
            "ID": str(data[5]),
            "ENTRYTYPE": "book"}]
        return bibtex_entry

    def write_to_bib_file(self, data, file):
        bibtex = self._create_bibtex_format(data)
        writer = BibTexWriter()
        writer.indent = "    "
        try:
            with open(file, "a", encoding="utf-8") as bibfile:
                bibfile.write(writer.write(bibtex))
            return True
        except:
            return False

    def read_from_bib_file(self,file):
        with open(file, encoding="utf-8") as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
        refs = []
        for entry in bib_database.entries:
            book = Book(entry["author"], entry["title"], entry["publisher"], entry["year"])
            refs.append(book)
        return refs
