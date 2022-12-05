from entities.book import Book

class ReferenceServices:
    def __init__(self, io, bibhandler):
        self._io = io
        self._bibhandler = bibhandler

    def add_reference_humanformat(self, reference):
        self._io.write("Syötä viitteen tiedot:")
        title = self._io.read("Kirjan nimi: ")
        author = self._io.read("Kijailija: ")
        while True:
            try:
                year = int(self._io.read("Julkaisuvuosi: "))
                break
            except ValueError:
                self._io.write("Virheellinen syöte")
        publisher = self._io.read("Julkaisija: ")
        keyword = self._io.read("Avainsana, jolla haluat viitata teokseen: ")
        text = f"""Lisätään {reference} {title} ({year}), kirjoittanut {author},
                julkaissut {publisher}, avainsanalla {keyword}"""
        self._io.write(text)

        data = (reference, title, author, year, publisher, keyword)
        if self._bibhandler.write_to_bib_file_humanformat(data,"references.bib"):
            self._io.write("BibTex tiedoston kirjoittaminen onnistui")
        else:
            self._io.write("BibTex tiedoston kirjoittaminen epäonnistui")

    def edit_reference(self, reference):
        pass

    def delete_reference(self,reference):
        pass

    def add_reference_bibtexformat(self):
        bibtex = self._io.read_bibtex("Syötä kirjan bibtex: ")
        if self._bibhandler.write_to_bib_file_bibtexformat(bibtex, "references.bib"):
            self._io.write("BibTex tiedoston kirjoittaminen onnistui")
        else:
            self._io.write("BibTex tiedoston kirjoittaminen epäonnistui")




    def list_references(self):
        references = self._bibhandler.read_from_bib_file("references.bib")
        refs = []
        for entry in references.entries:
            book = Book(entry["author"], entry["title"], entry["publisher"], entry["year"])
            refs.append(book)
        return refs
