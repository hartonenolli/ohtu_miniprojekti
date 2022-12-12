from os import path, remove

from entities.reference import Reference


class ReferenceServices:
    def __init__(self, io, bibhandler, filename, filterservice):
        self._io = io
        self._bibhandler = bibhandler
        self.filename = filename
        self.filterservice = filterservice

    def delete_reference(self,reference):
        pass

    def add_reference_bibtexformat(self):
        bibtex = self._io.read_bibtex("Syötä kirjan bibtex: ")
        if self._bibhandler.write_to_bib_file_bibtexformat(bibtex, self.filename):
            self._io.write("BibTex tiedoston kirjoittaminen onnistui")
        else:
            self._io.write("BibTex tiedoston kirjoittaminen epäonnistui")

    def write_references(self, referencelist):
        if referencelist:
            for reference in referencelist:
                self._io.write(reference)
        else:
            self._io.write("Viitekirjasto on tyhjä.")

    def list_references(self, references):
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
            refs.append(str(reference))
        return refs

    def add_reference_humanformat(self, entry_type):
        self._io.write("Syötä viitteen tiedot:")
        try_loop = True
        while try_loop:
            try:
                key = self._io.read("Avainsana, jolla haluat viitata teokseen: ")
                title = self._io.read("Nimi: ")
                author = self._io.read("Kirjoittaja/t: ")
                if not key or not title or not author:
                    raise ReferenceError
                try_loop = False
            except ReferenceError:
                self._io.write("Viitteellä oltava avainsana, nimi ja kirjoittaja")
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

    def filter_references(self, basis):
        keyword = self._io.read("Syötä hakusana: ")
        references = self._bibhandler.read_from_bib_file(self.filename)
        if basis == 'vuoden':
            references = self.filterservice.filter_by_year(references, int(keyword))

        elif basis == 'tekijän':
            references = self.filterservice.filter_by_author(references, keyword)

        elif basis == 'julkaisijan':
            references = self.filterservice.filter_by_publisher(references, keyword)

        elif basis == 'viitetyypin':
            references = self.filterservice.filter_by_entrytype(references, keyword)

        else:
            references = self.filterservice.filter_by_title(references, keyword)

        self.write_references(self.list_references(references))

    def sort_references(self, basis):
        references = self._bibhandler.read_from_bib_file(self.filename)
        if basis == 'lisäysjärjestys':
            self.write_references(self.list_references(references))
        else:
            if basis == 'vuoden':
                references = self.filterservice.sort_by(references, "year")

            elif basis == 'tekijän':
                references = self.filterservice.sort_by(references, "author")

            elif basis == 'julkaisijan':
                references = self.filterservice.sort_by(references, "publisher")

            elif basis == 'viitetyypin':
                references = self.filterservice.sort_by(references, "ENTRYTYPE")

            else:
                references = self.filterservice.sort_by(references, "title")

            self.write_references(self.list_references(references))

    def add_to_new_file(self, references):
        while True:
            new_file_name = self._io.read("Uuden tiedoston nimi: ")
            new_file_name = new_file_name + ".bib"
            if new_file_name != "references.bib":
                break
            self._io.write("Kokeile toista tiedoston nimeä")

        if path.isfile(new_file_name):
            remove(new_file_name)

        for entry in references:
            entry = entry.split(". ")
            if entry[0] == 'kirja':
                reference = Reference(entry[0], entry[1], entry[2], entry[4], entry[3], entry[5])
            elif entry[0] == 'lehtiartikkeli':
                reference = Reference(entry[0], entry[1], entry[2], entry[4], entry[3], None, entry[5])
            elif entry[0] == 'gradu':
                reference = Reference(entry[0], entry[1], entry[2], entry[4], entry[3], None, None, entry[5])
            elif entry[0] == 'tutkimusraportti':
                reference = Reference(entry[0], entry[1], entry[2], entry[4],
                entry[3], None, None, None, entry[5])
            else:
                reference = Reference(entry[0], entry[1], entry[2], entry[4],
                entry[3], None, None, None, None, entry[5])

            entry = reference.create_bibtex_entry()

            if self._bibhandler.write_to_bib_file_humanformat(entry, new_file_name):
                self._io.write(f"{str(reference)} lisääminen onnistui")
            else:
                self._io.write(f"{str(reference)} lisääminen epäonnistui")

    def all_references(self):
        references = self._bibhandler.read_from_bib_file(self.filename)
        references = self.list_references(references)
        refs = []
        for refererence in references:
            refs.append({'name' : refererence})
        return refs
