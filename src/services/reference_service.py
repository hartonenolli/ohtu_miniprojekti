from entities.book import Book
from entities.reference import Reference

class ReferenceServices:
    def __init__(self, io, bibhandler):
        self._io = io
        self._bibhandler = bibhandler
    def add_reference_humanformat(self, reference):
        self._io.write("Syötä viitteen tiedot:")
        title = self._io.read("Nimi: ")
        author = self._io.read("Kirjoittaja/t: ")
        while True:
            try:
                year = int(self._io.read("Julkaisuvuosi (jätä tyhjäksi jos ei ole): "))
                break
            except ValueError:
                self._io.write("Virheellinen syöte")
        publisher = self._io.read("Kustantaja: ")
        keyword = self._io.read("Avainsana, jolla haluat viitata teokseen: ")
        text = f"Lisätään {reference} {title} ({year}), kirjoittanut {author}, "  \
        f"julkaissut {publisher}, avainsanalla {keyword}"
        self._io.write(text)

        data = (reference, title, author, year, publisher, keyword)
        if self._bibhandler.write_to_bib_file_humanformat(data,"references.bib"):
            self._io.write("BibTex tiedoston kirjoittaminen onnistui")
        else:
            self._io.write("BibTex tiedoston kirjoittaminen epäonnistui")

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

#Uusi funktio viittauksen lisäämiseen. Entry-typestä riippuen kysytään oikeat attribuutit. Loppuihin tulee None.
#Funktio kutsuu reference-olion create_bibtex_entry metodia, jonka paluuarvona on suoraan bibtex-tallennettava formaatti.
#Paluuarvo viedään bibhandlerille, joka ainoastaan kirjoittaa.
#HUOM käyttö rikkoo testejä atm. List_references ei vielä osaa lukea kaikkia attribuutteja.

    def add_reference_humanformat_new(self, entry_type):
        self._io.write("Syötä viitteen tiedot:")
        id = self._io.read("Avainsana, jolla haluat viitata teokseen: ")
        title = self._io.read("Nimi: ")
        author = self._io.read("Kirjoittaja/t: ")
        year = self._io.read("Julkaisuvuosi (jätä tyhjäksi jos ei ole): ")
        if entry_type == 'kirja':
            publisher = self._io.read("Kustantaja: ")
            reference = Reference(entry_type, id, title, author, year, publisher)
        elif entry_type == 'lehtiartikkeli':
            journal = self._io.read("Julkaisu: ")
            reference = Reference(entry_type, id, title, author, year, None, journal)
        elif entry_type == 'gradu':
            school = self._io.read("Koulu: ")
            reference = Reference(entry_type, id, title, author, year, None, None, school)
        elif entry_type == 'tutkimusraportti':
            institution = self._io.read("Organisaatio: ")
            reference = Reference(entry_type, id, title, author, year, None, None, None, institution)
        else:
            note = self._io.read("Kommentti: ")
            reference = Reference(entry_type, id, title, author, year, None, None, None, None, note)
        self._io.write("Lisätään " + reference.__str__())
        entry = reference.create_bibtex_entry()
        if self._bibhandler.write_to_bib_file_humanformat_new(entry, "references.bib"):
            self._io.write("BibTex tiedoston kirjoittaminen onnistui")
        else:
            self._io.write("BibTex tiedoston kirjoittaminen epäonnistui")
