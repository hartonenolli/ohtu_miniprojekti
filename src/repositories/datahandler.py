import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bparser import BibTexParser
from entities.reference import Reference

class BibtexHandler:
    def __init__(self):
        pass

    def _create_bibtex_format_humanformat(self, data):
        bibtex_entry = BibDatabase()
        bibtex_entry.entries = [
            {"title": str(data[1]),
            "author": str(data[2]),
            "year": str(data[3]),
            "publisher": str(data[4]),
            "ID": str(data[5]),
            "ENTRYTYPE": "book"}]
        return bibtex_entry

    def write_to_bib_file_humanformat(self, data, file):
        bibtex = self._create_bibtex_format_humanformat(data)
        writer = BibTexWriter()
        writer.indent = "    "
        try:
            with open(file, "a", encoding="utf-8") as bibfile:
                bibfile.write(writer.write(bibtex))
            return True
        except PermissionError:
            return False

    def _create_bibtex_format_bibtexformat(self, bibtex):
        bibparser = BibTexParser(interpolate_strings=False)
        bibtex_entry = bibparser.parse(bibtex)
        return bibtex_entry

    def write_to_bib_file_bibtexformat(self, bibtex, file):
        bibtex = self._create_bibtex_format_bibtexformat(bibtex)
        writer = BibTexWriter()
        writer.indent = "    "
        try:
            with open(file, "a", encoding="utf-8") as bibfile:
                bibfile.write(writer.write(bibtex))
            return True
        except PermissionError:
            return False

    def read_from_bib_file(self,file):
        try:
            with open(file, encoding="utf-8") as bibtex_file:
                bib_database = bibtexparser.load(bibtex_file)
            return bib_database
        except PermissionError:
            return None

#Uusi kirjoitusfunktio. Reference-olio luo itse itsestään bibtex-entryn oikeassa formaatissa tyypistä
# (kirja, artikkeli jne. riippuen), ja tämä funktio hoitaa vain kirjoittamisen.

    def write_to_bib_file_humanformat_new(self, entry, file):
        writer = BibTexWriter()
        writer.indent = "    "
        try:
            with open(file, "a", encoding="utf-8") as bibfile:
                bibfile.write(writer.write(entry))
            return True
        except PermissionError:
            return False