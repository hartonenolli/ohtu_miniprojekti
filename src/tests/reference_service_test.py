import unittest
from tempfile import NamedTemporaryFile
from services.reference_service import ReferenceServices
from repositories.datahandler import BibtexHandler
from unittest.mock import Mock
from services.filter_service import FilterService

class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def read(self, prompt):
        return self.inputs.pop(0)
    
    def write(self, prompt):
        self.outputs.append(prompt)

    def read_bibtex(self, prompt):
        return self.inputs.pop(0)

class StubData:
    def __init__(self):
        self.entries = [{
            "author": "Mika Waltari",
            "publisher": "WSOY",
            "title": "Sinuhe Egyptiläinen",
            "year": "1945"
        }]


class TestReferenceServices(unittest.TestCase):
    def setUp(self):
        self.bibhandler_mock = Mock(wraps=BibtexHandler())
        self.filterservice_mock = Mock(wraps=FilterService())
        test_file = NamedTemporaryFile(encoding="utf-8", mode="w+", delete=False)
        self.filename = test_file.name

    def test_add_reference_humanformat_works_with_correct_year_format(self):
        io = StubIO(["Sinuhe Egyptiläinen", "Mika Waltari", "1945", "WSOY", "avainsana"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.add_reference_humanformat("kirja")

        self.assertEqual(io.outputs[-1], "BibTex tiedoston kirjoittaminen onnistui")

    def test_add_reference_humanformat_returns_correct_output_when_writing_to_file_does_not_succeed(self):
        io = StubIO(["Sinuhe Egyptiläinen", "Mika Waltari", "1945", "WSOY", "avainsana"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        
        self.bibhandler_mock.write_to_bib_file_humanformat.return_value = False
        ref_service.add_reference_humanformat("kirja")

        self.assertEqual(io.outputs[-1], "BibTex tiedoston kirjoittaminen epäonnistui")

    def test_add_reference_bibtexformat_returns_correct_output_when_writing_to_file_successful(self):
        io = StubIO(["testi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)

        self.bibhandler_mock.write_to_bib_file_bibtexformat.return_value = True
        ref_service.add_reference_bibtexformat()

        self.assertEqual(self.bibhandler_mock.write_to_bib_file_bibtexformat.call_count, 1)
        self.assertEqual(io.outputs[-1], "BibTex tiedoston kirjoittaminen onnistui")

    def test_add_reference_bibtexformat_returns_correct_output_when_writing_to_file_failed(self):
        io = StubIO(["testi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)

        self.bibhandler_mock.write_to_bib_file_bibtexformat.return_value = False
        ref_service.add_reference_bibtexformat()

        self.assertEqual(self.bibhandler_mock.write_to_bib_file_bibtexformat.call_count, 1)
        self.assertEqual(io.outputs[-1], "BibTex tiedoston kirjoittaminen epäonnistui")

    def test_list_references_returns_correct_format_book(self):
        data = Mock(entries = [{
            "ENTRYTYPE": "book",
            "author": "1",
            "title": "2",
            "publisher": "3",
            "year": "4",
            "ID": "1"
        }])
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.list_references(data)
        self.assertEqual(io.outputs[-1], "1. 4. 2. 3.")

    def test_add_reference_humanformat_works_with_article(self):
        io = StubIO(["avainsana", "nimi", "kirjoittaja", "1", "julkaisu"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.add_reference_humanformat("lehtiartikkeli")

        self.assertEqual(io.outputs[-1], "BibTex tiedoston kirjoittaminen onnistui")

    def test_add_reference_humanformat_works_gradu(self):
        io = StubIO(["avainsana", "nimi", "kirjoittaja", "1", "koulu"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.add_reference_humanformat("gradu")

        self.assertEqual(io.outputs[-1], "BibTex tiedoston kirjoittaminen onnistui")

    def test_add_reference_humanformat_works_with_tutkimus(self):
        io = StubIO(["avainsana", "nimi", "kirjoittaja", "1", "orgasinattio"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.add_reference_humanformat("tutkimusraportti")

        self.assertEqual(io.outputs[-1], "BibTex tiedoston kirjoittaminen onnistui")

    def test_add_reference_humanformat_works_with_julkaisematon(self):
        io = StubIO(["avainsana", "nimi", "kirjoittaja", "1", "kommentti"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.add_reference_humanformat("julkaisematon")

        self.assertEqual(io.outputs[-1], "BibTex tiedoston kirjoittaminen onnistui")

    def test_list_references_returns_correct_format_article(self):
        data = Mock(entries = [{
            "ENTRYTYPE": "article",
            "author": "1",
            "title": "2",
            "journal": "3",
            "year": "4",
            "ID": "1"
        }])
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.list_references(data)
        self.assertEqual(io.outputs[-1], "1. 4. 2. 3.")

    def test_list_references_returns_correct_format_gradu(self):
        data = Mock(entries = [{
            "ENTRYTYPE": "mastersthesis",
            "author": "1",
            "title": "2",
            "school": "3",
            "year": "4",
            "ID": "1"
        }])
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.list_references(data)
        self.assertEqual(io.outputs[-1], "1. 4. 2. 3.")

    def test_list_references_returns_correct_format_techreport(self):
        data = Mock(entries = [{
            "ENTRYTYPE": "techreport",
            "author": "1",
            "title": "2",
            "institution": "3",
            "year": "4",
            "ID": "1"
        }])
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename,self.filterservice_mock)
        ref_service.list_references(data)
        self.assertEqual(io.outputs[-1], "1. 4. 2. 3.")

    def test_list_references_returns_correct_format_unpublished(self):
        data = Mock(entries = [{
            "ENTRYTYPE": "unpublished",
            "author": "1",
            "title": "2",
            "note": "3",
            "year": "4",
            "ID": "1"
        }])
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        
        ref_service.list_references(data)
        self.assertEqual(io.outputs[-1], "1. 4. 2. 3.")


    def test_list_references_returns_correct_format_unpublished_year_None(self):
        data = Mock(entries = [{
            "ENTRYTYPE": "unpublished",
            "author": "1",
            "title": "2",
            "note": "3",
            "year": "None",
            "ID": "1"
        }])
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)

        ref_service.list_references(data)
        self.assertEqual(io.outputs[-1], "1. 2. 3.")

    def test_write_references_writes_correct_output_if_references_empty(self):
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)

        ref_service.write_references([])
        self.assertEqual(io.outputs[-1], "Viitekirjasto on tyhjä.")   

    def test_filter_service_filterby_year_calls_right_function(self):
        io = StubIO(["2022"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.filter_references("vuoden")
        self.assertEqual(self.filterservice_mock.filter_by_year.call_count, 1)

    def test_filter_service_filterby_author_calls_right_function(self):
        io = StubIO(["testi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.filter_references("tekijän")
        self.assertEqual(self.filterservice_mock.filter_by_author.call_count, 1)

    def test_filter_service_filterby_title_calls_right_function(self):
        io = StubIO(["testi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.filter_references("nimen")
        self.assertEqual(self.filterservice_mock.filter_by_title.call_count, 1)

    def test_filter_service_filterby_publisher_calls_right_function(self):
        io = StubIO(["testi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.filter_references("julkaisijan")
        self.assertEqual(self.filterservice_mock.filter_by_publisher.call_count, 1)

    def test_filter_service_filterby_entrytype_calls_right_function(self):
        io = StubIO(["testi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.filter_references("viitetyypin")
        self.assertEqual(self.filterservice_mock.filter_by_entrytype.call_count, 1)

    def test_filter_service_sortby_year_calls_right_function(self):
        io = StubIO(["2022"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.sort_references("vuoden")
        self.assertEqual(self.filterservice_mock.sort_by_year.call_count, 1)

    def test_filter_service_sortby_author_calls_right_function(self):
        io = StubIO(["testi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.sort_references("tekijän")
        self.assertEqual(self.filterservice_mock.sort_by_author.call_count, 1)

    def test_filter_service_sortby_title_calls_right_function(self):
        io = StubIO(["testi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.sort_references("nimen")
        self.assertEqual(self.filterservice_mock.sort_by_title.call_count, 1)

    def test_filter_service_sortby_publisher_calls_right_function(self):
        io = StubIO(["testi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.sort_references("julkaisijan")
        self.assertEqual(self.filterservice_mock.sort_by_publisher.call_count, 1)

    def test_filter_service_sortby_entrytype_calls_right_function(self):
        io = StubIO(["testi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.sort_references("viitetyypin")
        self.assertEqual(self.filterservice_mock.sort_by_entrytype.call_count, 1)
