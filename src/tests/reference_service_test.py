import unittest
from tempfile import NamedTemporaryFile
from services.reference_service import ReferenceServices
from repositories.datahandler import BibtexHandler
from unittest.mock import Mock, ANY
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

        self.assertEqual(io.outputs[-1], "BibTex tiedoston kirjoittaminen onnistui ")

    def test_add_reference_humanformat_returns_correct_output_when_writing_to_file_does_not_succeed(self):
        io = StubIO(["Sinuhe Egyptiläinen", "Mika Waltari", "1945", "WSOY", "avainsana"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        
        self.bibhandler_mock.write_to_bib_file_humanformat.return_value = False
        ref_service.add_reference_humanformat("kirja")

        self.assertEqual(io.outputs[-1], "BibTex tiedoston kirjoittaminen epäonnistui ")

    def test_add_reference_bibtexformat_returns_correct_output_when_writing_to_file_successful(self):
        io = StubIO(["testi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)

        self.bibhandler_mock.write_to_bib_file_bibtexformat.return_value = True
        ref_service.add_reference_bibtexformat()

        self.assertEqual(self.bibhandler_mock.write_to_bib_file_bibtexformat.call_count, 1)
        self.assertEqual(io.outputs[-1], "BibTex tiedoston kirjoittaminen onnistui ")

    def test_add_reference_bibtexformat_returns_correct_output_when_writing_to_file_failed(self):
        io = StubIO(["testi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)

        self.bibhandler_mock.write_to_bib_file_bibtexformat.return_value = False
        ref_service.add_reference_bibtexformat()

        self.assertEqual(self.bibhandler_mock.write_to_bib_file_bibtexformat.call_count, 1)
        self.assertEqual(io.outputs[-1], "BibTex tiedoston kirjoittaminen epäonnistui ")

    def test_add_reference_humanformat_works_with_article(self):
        io = StubIO(["avainsana", "nimi", "kirjoittaja", "1", "julkaisu"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.add_reference_humanformat("lehtiartikkeli")

        self.assertEqual(io.outputs[-1], "BibTex tiedoston kirjoittaminen onnistui ")

    def test_add_reference_humanformat_works_gradu(self):
        io = StubIO(["avainsana", "nimi", "kirjoittaja", "1", "koulu"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.add_reference_humanformat("gradu")

        self.assertEqual(io.outputs[-1], "BibTex tiedoston kirjoittaminen onnistui ")

    def test_add_reference_humanformat_works_with_tutkimus(self):
        io = StubIO(["avainsana", "nimi", "kirjoittaja", "1", "orgasinattio"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.add_reference_humanformat("tutkimusraportti")

        self.assertEqual(io.outputs[-1], "BibTex tiedoston kirjoittaminen onnistui ")

    def test_add_reference_humanformat_works_with_julkaisematon(self):
        io = StubIO(["avainsana", "nimi", "kirjoittaja", "1", "kommentti"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.add_reference_humanformat("julkaisematon")

        self.assertEqual(io.outputs[-1], "BibTex tiedoston kirjoittaminen onnistui ")

    def test_list_references_returns_correct_format_book(self):
        data = Mock(entries = [{
            "ENTRYTYPE": "book",
            "author": "author",
            "title": "title",
            "publisher": "publisher",
            "year": "2000",
            "ID": "1"
        }])
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.list_references(data)
        self.assertEqual(ref_service.list_references(data)[0], "kirja. 1. author. 2000. title. publisher. ")

    def test_list_references_returns_correct_format_article(self):
        data = Mock(entries = [{
            "ENTRYTYPE": "article",
            "author": "author",
            "title": "title",
            "journal": "journal",
            "year": "2000",
            "ID": "1"
        }])
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.list_references(data)
        self.assertEqual(ref_service.list_references(data)[0], "lehtiartikkeli. 1. author. 2000. title. journal. ")

    def test_list_references_returns_correct_format_gradu(self):
        data = Mock(entries = [{
            "ENTRYTYPE": "mastersthesis",
            "author": "author",
            "title": "title",
            "school": "school",
            "year": "2000",
            "ID": "1"
        }])
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.list_references(data)
        self.assertEqual(ref_service.list_references(data)[0], "gradu. 1. author. 2000. title. school. ")

    def test_list_references_returns_correct_format_techreport(self):
        data = Mock(entries = [{
            "ENTRYTYPE": "techreport",
            "author": "author",
            "title": "title",
            "institution": "institution",
            "year": "2000",
            "ID": "1"
        }])
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename,self.filterservice_mock)
        ref_service.list_references(data)
        self.assertEqual(ref_service.list_references(data)[0], "tutkimusraportti. 1. author. 2000. title. institution. ")

    def test_list_references_returns_correct_format_unpublished(self):
        data = Mock(entries = [{
            "ENTRYTYPE": "unpublished",
            "author": "author",
            "title": "title",
            "note": "note",
            "year": "2000",
            "ID": "1"
        }])
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename,self.filterservice_mock)
        ref_service.list_references(data)
        self.assertEqual(ref_service.list_references(data)[0], "julkaisematon. 1. author. 2000. title. note. ")


    def test_list_references_returns_correct_format_unpublished_year_None(self):
        data = Mock(entries = [{
            "ENTRYTYPE": "unpublished",
            "author": "author",
            "title": "title",
            "note": "note",
            "year": "None",
            "ID": "1"
        }])
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename,self.filterservice_mock)
        ref_service.list_references(data)
        self.assertEqual(ref_service.list_references(data)[0], "julkaisematon. 1. author. title. note. ")

    def test_write_references_writes_correct_output_if_references_empty(self):
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)

        ref_service.write_references([])
        self.assertEqual(io.outputs[-1], "Viitekirjasto on tyhjä. ")   

    def test_filter_service_filterby_year_calls_right_function(self):
        io = StubIO(["2022"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.filter_references("vuoden")
        self.assertEqual(self.filterservice_mock.filter_by.call_count, 1)

    def test_filter_service_filterby_author_calls_right_function(self):
        io = StubIO(["testi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.filter_references("tekijän")
        self.assertEqual(self.filterservice_mock.filter_by.call_count, 1)

    def test_filter_service_filterby_title_calls_right_function(self):
        io = StubIO(["testi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.filter_references("nimen")
        self.assertEqual(self.filterservice_mock.filter_by.call_count, 1)

    def test_filter_service_filterby_publisher_calls_right_function(self):
        io = StubIO(["testi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.filter_references("julkaisijan")
        self.assertEqual(self.filterservice_mock.filter_by.call_count, 1)

    def test_filter_service_filterby_entrytype_calls_right_function(self):
        io = StubIO(["testi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.filter_references("viitetyypin")
        self.assertEqual(self.filterservice_mock.filter_by.call_count, 1)

    def test_filter_service_sortby_year_calls_right_function_with_correct_keyword(self):
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.sort_references("vuoden")
        self.assertEqual(self.filterservice_mock.sort_by.call_count, 1)
        self.filterservice_mock.sort_by.assert_called_with(ANY, "year")

    def test_filter_service_sortby_author_calls_right_function_with_correct_keyword(self):
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.sort_references("tekijän")
        self.assertEqual(self.filterservice_mock.sort_by.call_count, 1)
        self.filterservice_mock.sort_by.assert_called_with(ANY, "author")

    def test_filter_service_sortby_publisher_calls_right_function_with_correct_keyword(self):
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.sort_references("julkaisijan")
        self.assertEqual(self.filterservice_mock.sort_by.call_count, 1)
        self.filterservice_mock.sort_by.assert_called_with(ANY, "publisher")

    def test_filter_service_sortby_entrytype_calls_right_function_with_correct_keyword(self):
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.sort_references("viitetyypin")
        self.assertEqual(self.filterservice_mock.sort_by.call_count, 1)
        self.filterservice_mock.sort_by.assert_called_with(ANY, "ENTRYTYPE")

    def test_filter_service_sortby_title_calls_right_function_with_correct_keyword(self):
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.sort_references("nimen")
        self.assertEqual(self.filterservice_mock.sort_by.call_count, 1)
        self.filterservice_mock.sort_by.assert_called_with(ANY, "title")

    def test_add_to_new_file_runs_to_end(self):
        io = StubIO(["tiedostonimi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.add_to_new_file(["kirja. 1. author. 2000. title. publisher. "])
        self.assertEqual(io.outputs[-1], "Viitteiden kirjoittaminen uuteen tiedostoon onnistui suoritettu. ")

    def test_add_to_new_file_adds_multiple(self):
        io = StubIO(["tiedostonimi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.add_to_new_file(["kirja. 1. author. 2000. title. publisher. ", 
            "kirja. 2. author2. 2002. title2. publisher2. "])
        self.assertEqual(io.outputs[-1], "Viitteiden kirjoittaminen uuteen tiedostoon onnistui suoritettu. ")

    def test_add_to_new_file_wrong_file_name(self):
        io = StubIO(["references", "tiedostonimi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock)
        ref_service.add_to_new_file(["kirja. 1. author. 2000. title. publisher. "])
        self.assertEqual(io.outputs[-1], "Viitteiden kirjoittaminen uuteen tiedostoon onnistui suoritettu. ")
