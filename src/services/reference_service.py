from entities.reference import Reference

class ReferenceServices:
    def __init__(self, io, bibhandler, filename):
        self._io = io
        self._bibhandler = bibhandler
        self.filename = filename

    def delete_reference(self,reference):
        pass

    def add_reference_bibtexformat(self):
        bibtex = self._io.read_bibtex("Syötä kirjan bibtex: ")
        if self._bibhandler.write_to_bib_file_bibtexformat(bibtex, self.filename):
            self._io.write("BibTex tiedoston kirjoittaminen onnistui")
        else:
            self._io.write("BibTex tiedoston kirjoittaminen epäonnistui")



    def list_references(self):
        references = self._bibhandler.read_from_bib_file(self.filename)
        refs = []
        for entry in references.entries:
            if entry["ENTRYTYPE"] == "book":
                reference = Reference("kirja", entry["ID"], entry["title"],
                entry["author"], entry["year"], entry["publisher"])

            elif entry["ENTRYTYPE"] == "article":
                reference = Reference("lehtiartikkeli", entry["ID"], entry["title"],
                entry["author"], entry["year"], None, entry["journal"])

            elif entry["ENTRYTYPE"] == "mastersthesis":
                reference = Reference("gradu", entry["ID"], entry["title"],
                entry["author"], entry["year"], None, None, entry["school"])

            elif entry["ENTRYTYPE"] == "techreport":
                reference = Reference("tutkimusraportti", entry["ID"], entry["title"],
                entry["author"], entry["year"], None, None, None, entry["institution"])
            else:
                reference = Reference("julkaisematon", entry["ID"], entry["title"],
                entry["author"], entry["year"], None, None, None, None, entry["note"])
            refs.append(reference)
        return refs

    def add_reference_humanformat(self, entry_type):
        self._io.write("Syötä viitteen tiedot:")
        key = self._io.read("Avainsana, jolla haluat viitata teokseen: ")
        title = self._io.read("Nimi: ")
        author = self._io.read("Kirjoittaja/t: ")
        year = self._io.read("Julkaisuvuosi (jätä tyhjäksi jos ei ole): ")
        if entry_type == 'kirja':
            publisher = self._io.read("Kustantaja: ")
            reference = Reference(entry_type, key, title, author, year, publisher)
        elif entry_type == 'lehtiartikkeli':
            journal = self._io.read("Julkaisu: ")
            reference = Reference(entry_type, key, title, author, year, None, journal)
        elif entry_type == 'gradu':
            school = self._io.read("Koulu: ")
            reference = Reference(entry_type, key, title, author, year, None, None, school)
        elif entry_type == 'tutkimusraportti':
            institution = self._io.read("Organisaatio: ")
            reference = Reference(entry_type, key, title, author,
            year, None, None, None, institution)
        else:
            note = self._io.read("Kommentti: ")
            reference = Reference(entry_type, key, title, author,
            year, None, None, None, None, note)
        self._io.write("Lisätään " + str(reference))
        entry = reference.create_bibtex_entry()
        if self._bibhandler.write_to_bib_file_humanformat(entry, self.filename):
            self._io.write("BibTex tiedoston kirjoittaminen onnistui")
        else:
            self._io.write("BibTex tiedoston kirjoittaminen epäonnistui")
