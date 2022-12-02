import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

class BibtexController():
    def __init__(self):
        pass

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
        try:
            with open("references.bib", "a") as bibfile:
                bibfile.write(writer.write(db))
            return True
        except:
            return False

    def read_from_bib_file(self):
        with open("references.bib") as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
        refs = []
        for entry in bib_database.entries:
            book = Book(entry["author"], entry["title"], entry["publisher"], entry["year"])
            refs.append(book)
        return refs