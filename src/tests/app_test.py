import unittest
from ui.app import CommandLineUI
from entities.book import Book
from unittest.mock import Mock
from services.reference_service import ReferenceServices
from repositories.datahandler import BibtexHandler

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

    def test_user_input_exit_works(self):
        io = StubIO(["poistu"])
        self.app = CommandLineUI(io, None)
        self.app.start_app()
        
        self.assertEqual(self.app._run, False)

    def test_add_reference_humanformat_calls_right_function(self):
        io = StubIO(["lisää viite", "ihmisluettava", "kirja","Sinuhe Egyptiläinen", "Mika Waltari", "1945", "WSOY", "Waltari45", "poistu"])
        self.service_mock = Mock(wraps=ReferenceServices(io, self.bibhandler_mock))
        self.app = CommandLineUI(io, self.service_mock)
        self.app.start_app()

        self.assertEqual(self.service_mock.add_reference_humanformat.call_count, 1)

    def test_add_reference_bibtexformat_calls_right_function(self):
        io = StubIO(["lisää viite", "bibtex", "kirja","testisyöte", "poistu"])
        self.service_mock = Mock(wraps=ReferenceServices(io, self.bibhandler_mock))
        self.app = CommandLineUI(io, self.service_mock)
        self.app.start_app()

        self.assertEqual(self.service_mock.add_reference_bibtexformat.call_count, 1)

    def test_list_references_with_empty_file_returns_correct_output(self):
        io = StubIO(["listaa viitteet", "poistu"])
        self.service_mock = Mock(wraps=ReferenceServices(io, self.bibhandler_mock))
        self.app = CommandLineUI(io, self.service_mock)
        self.service_mock.list_references.return_value = None
        self.app.start_app()

        self.assertEqual(io.outputs[-1], "Viitekirjasto on tyhjä.")

    def test_list_references_with_non_empty_file_returns_correct_output(self):
        io = StubIO(["listaa viitteet", "poistu"])
        self.service_mock = Mock(wraps=ReferenceServices(io, self.bibhandler_mock))
        self.app = CommandLineUI(io, self.service_mock)
        self.service_mock.list_references.return_value = ["testi1", "testi2"]
        self.app.start_app()

        self.assertEqual(self.service_mock.list_references.call_count, 1)
        self.assertEqual(io.outputs[-1], "testi2")
