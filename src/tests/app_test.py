import unittest
from tempfile import NamedTemporaryFile
from ui.app import CommandLineUI
from unittest.mock import Mock
from services.reference_service import ReferenceServices
from repositories.datahandler import BibtexHandler
from services.filter_service import FilterService

class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def read(self, prompt):
        return self.inputs.pop(0)
    
    def write(self, prompt):
        self.outputs.append(prompt)
    
    def read_pyinquirer(self, value):
        d = {}
        d[value["name"]] = self.inputs.pop(0)
        return d
    
    def read_bibtex(self, prompt):
        return self.inputs.pop(0)

class TestCommandLineUI(unittest.TestCase):
    def setUp(self):
        self.bibhandler_mock = Mock(wraps=BibtexHandler())
        self.filterservice_mock = Mock(wraps=FilterService())
        test_file = NamedTemporaryFile(encoding="utf-8", mode="w+", delete=False)
        self.filename = test_file.name

    def test_user_input_exit_works(self):
        io = StubIO(["poistu"])
        self.app = CommandLineUI(io, None)
        self.app.start_app()
        
        self.assertEqual(self.app._run, False)

    def test_add_reference_humanformat_calls_right_function(self):
        io = StubIO(["lisää viite", "ihmisluettava", "kirja", "Waltari45", "Sinuhe Egyptiläinen", "Mika Waltari", "1945", "WSOY", "poistu"])
        self.service_mock = Mock(wraps=ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock))
        self.app = CommandLineUI(io, self.service_mock)
        self.app.start_app()

        self.assertEqual(self.service_mock.add_reference_humanformat.call_count, 1)

    def test_add_reference_bibtexformat_calls_right_function(self):
        io = StubIO(["lisää viite", "bibtex", "kirja", "testisyöte", "poistu"])
        self.service_mock = Mock(wraps=ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock))
        self.app = CommandLineUI(io, self.service_mock)
        self.app.start_app()

        self.assertEqual(self.service_mock.add_reference_bibtexformat.call_count, 1)

    def test_sort_references_calls_right_function(self):
        io = StubIO(["listaa viitteet", "lisäysjärjestys", "poistu"])
        self.service_mock = Mock(wraps=ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock))
        self.app = CommandLineUI(io, self.service_mock)
        self.app.start_app()

        self.assertEqual(self.service_mock.sort_references.call_count, 1)

    def test_filter_references_calls_right_function(self):
        io = StubIO(["etsi viitteitä", "vuoden", "2022", "poistu"])
        self.service_mock = Mock(wraps=ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock))
        self.app = CommandLineUI(io, self.service_mock)
        self.app.start_app()

        self.assertEqual(self.service_mock.filter_references.call_count, 1)
    
    def test_delete_reference_calls_right_function(self):
        io = StubIO(["poista viite", "[]", "poistu"])
        self.service_mock = Mock(wraps=ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock))
        self.app = CommandLineUI(io, self.service_mock)
        self.app.start_app()
        self.assertEqual(self.service_mock.delete_reference.call_count, 1)

    def test_add_references_to_new_file_calls_right_function(self):
        io = StubIO(["siirrä viitteitä tiedostoon", "", "uusi", "poistu"])
        self.service_mock = Mock(wraps=ReferenceServices(io, self.bibhandler_mock, self.filename, self.filterservice_mock))
        self.app = CommandLineUI(io, self.service_mock)
        self.app.start_app()
        self.assertEqual(self.service_mock.add_to_new_file.call_count, 1)