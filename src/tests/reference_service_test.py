import unittest
from tempfile import NamedTemporaryFile
from services.reference_service import ReferenceServices
from repositories.datahandler import BibtexHandler
from unittest.mock import Mock

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
        test_file = NamedTemporaryFile(encoding="utf-8", mode="w+", delete=False)
        self.filename = test_file.name

    def test_add_reference_humanformat_works_with_correct_year_format(self):
        io = StubIO(["Sinuhe Egyptiläinen", "Mika Waltari", "1945", "WSOY", "avainsana"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename)
        ref_service.add_reference_humanformat("kirja")

        self.assertEqual(io.outputs[-1], "BibTex tiedoston kirjoittaminen onnistui")

    def test_add_reference_humanformat_returns_error_output_with_incorrect_year_format(self):
        io = StubIO(["Sinuhe Egyptiläinen", "Mika Waltari", "aaa", "1945", "WSOY", "avainsana"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename)
        ref_service.add_reference_humanformat("kirja")

        self.assertEqual(io.outputs[-3], "Virheellinen syöte")

    def test_add_reference_humanformat_returns_correct_output_when_writing_to_file_does_not_succeed(self):
        io = StubIO(["Sinuhe Egyptiläinen", "Mika Waltari", "1945", "WSOY", "avainsana"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename)
        
        self.bibhandler_mock.write_to_bib_file_humanformat.return_value = False
        ref_service.add_reference_humanformat("kirja")

        self.assertEqual(io.outputs[-1], "BibTex tiedoston kirjoittaminen epäonnistui")

    def test_add_reference_bibtexformat_returns_correct_output_when_writing_to_file_successful(self):
        io = StubIO(["testi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename)

        self.bibhandler_mock.write_to_bib_file_bibtexformat.return_value = True
        ref_service.add_reference_bibtexformat()

        self.assertEqual(self.bibhandler_mock.write_to_bib_file_bibtexformat.call_count, 1)
        self.assertEqual(io.outputs[-1], "BibTex tiedoston kirjoittaminen onnistui")

    def test_add_reference_bibtexformat_returns_correct_output_when_writing_to_file_failed(self):
        io = StubIO(["testi"])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename)

        self.bibhandler_mock.write_to_bib_file_bibtexformat.return_value = False
        ref_service.add_reference_bibtexformat()

        self.assertEqual(self.bibhandler_mock.write_to_bib_file_bibtexformat.call_count, 1)
        self.assertEqual(io.outputs[-1], "BibTex tiedoston kirjoittaminen epäonnistui")

    def test_list_references_calls_correct_handler_method(self):
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename)
        ref_service.list_references()

        self.assertEqual(self.bibhandler_mock.read_from_bib_file.call_count, 1)

    def test_list_references_returns_correct_format(self):
        data = Mock(entries = [{
            "author": "1",
            "title": "2",
            "publisher": "3",
            "year": "4"
        }])
        io = StubIO([])
        ref_service = ReferenceServices(io, self.bibhandler_mock, self.filename)
        self.bibhandler_mock.read_from_bib_file.return_value = data
        
        self.assertEqual(ref_service.list_references()[0].__str__(), "1, 2. 3, 4.")