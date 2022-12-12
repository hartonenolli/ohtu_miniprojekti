import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bparser import BibTexParser


class BibtexHandler:
    def __init__(self):
        pass

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

    def write_to_bib_file_humanformat(self, entry, file):
        writer = BibTexWriter()
        writer.indent = "    "
        try:
            with open(file, "a", encoding="utf-8") as bibfile:
                bibfile.write(writer.write(entry))
            return True
        except PermissionError:
            return False
