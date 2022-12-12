import unittest
from services.filter_service import FilterService
from repositories.datahandler import BibtexHandler
from entities.reference import Reference
from tempfile import NamedTemporaryFile
from os import unlink

class TestFilterService(unittest.TestCase):
    def setUp(self) -> None:
        self.bib_file = NamedTemporaryFile(encoding="utf-8", mode="w+", delete=False)
        self.bib_handler = BibtexHandler()
        self.filter_service = FilterService()
        references = [
            Reference("kirja", "Waltari45", "Sinuhe Egyptiläinen", "Mika Waltari", "1945", "WSOY"),
            Reference("kirja", "Tolkien54", "The Fellowship of The Ring", "J. R. R Tolkien", "1954", "Allen & Unwin"),
            Reference("gradu", "Korhonen02", "Gradu Hienosta Asiata", "Pekka Korhonen", "2002", school="Helsingin Yliopisto"),
            Reference("gradu", "Virtanen15", "Toinen Hieno Gradu", "Janne Virtanen", "2015", school="Helsingin Yliopisto"),
            Reference("tutkimusraportti", "Nurmi00", "Mahtava tutkimusraportti", "Ilkka Nurmi", "2000", institution="Helsingin Yliopisto")
        ]
        self.bib_references = []
        for ref in references:
            ref = ref.create_bibtex_entry()
            self.bib_references.append(ref)
            self.bib_handler.write_to_bib_file_humanformat(ref, self.bib_file.name)
        self.bib_database = self.bib_handler.read_from_bib_file(self.bib_file.name)
        unlink(self.bib_file.name)
    
    def test_sorting_by_year_works(self):
        filter_result = self.filter_service.sort_by(self.bib_database, "year")
        self.assertEqual(self.bib_references[0].entries[0]["ID"], filter_result.entries[0]["ID"])
        self.assertEqual(self.bib_references[3].entries[0]["ID"], filter_result.entries[-1]["ID"])

    def test_sorting_by_year_descending_works(self):
        filter_result = self.filter_service.sort_by(self.bib_database, "year", descending=True)
        self.assertEqual(self.bib_references[3].entries[0]["ID"], filter_result.entries[0]["ID"])
        self.assertEqual(self.bib_references[0].entries[0]["ID"], filter_result.entries[-1]["ID"])

    def test_sorting_by_title_works(self):
        filter_result = self.filter_service.sort_by(self.bib_database, "title")
        self.assertEqual(self.bib_references[2].entries[0]["ID"], filter_result.entries[0]["ID"])
        self.assertEqual(self.bib_references[3].entries[0]["ID"], filter_result.entries[-1]["ID"])

    def test_filter_by_year_works(self):
        filter_result = self.filter_service.filter_by_year(self.bib_database, 1954)
        self.assertEqual(self.bib_references[1].entries[0]["ID"], filter_result.entries[0]["ID"])

