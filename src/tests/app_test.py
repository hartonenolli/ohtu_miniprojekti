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

class TestCommandLineUI(unittest.TestCase):
    def setUp(self):
        self.book = Book("Mika Waltari", "Sinuhe Egyptiläinen", "WSOY", "1945")

    def test_user_input_exit_works(self):
        io = StubIO(["poistu"])
        self.app = CommandLineUI(io, None)
        self.app.start_app()
        
        self.assertEqual(self.app._run, False)

    def test_user_input_add_reference_works(self):
        io = StubIO(["lisää viite", "kirja","Sinuhe Egyptiläinen", "Mika Waltari", "1945", "WSOY", "Waltari45", "poistu"])
        self.app = CommandLineUI(io, ReferenceServices(io, BibtexHandler()))
        self.app.start_app()

        self.assertEqual(io.outputs[-2].__str__(), "Lisätään kirja Sinuhe Egyptiläinen (1945), kirjoittanut Mika Waltari, julkaissut WSOY, avainsanalla Waltari45")

    def test_user_input_not_in_options_works(self):
        io = StubIO(["käpistely", "poistu"])
        self.app = CommandLineUI(io, None)
        self.app.start_app()

        self.assertEqual(io.outputs[1], "Virheellinen syöte.")

    def test_add_reference_adds_correct_string_to_database(self):
        io = StubIO(["lisää viite", "kirja","Sinuhe Egyptiläinen", "Mika Waltari", "1945", "WSOY", "Waltari45", "poistu"])
        self.app = CommandLineUI(io, ReferenceServices(io, BibtexHandler()))
        self.app.start_app()

        self.assertEqual(self.app._service.list_references()[-1].__str__(), self.book.__str__())

    def test_add_referense_input(self):
        io = StubIO(["listaa viitteet", "poistu"])
        self.app = CommandLineUI(io, ReferenceServices(io, BibtexHandler()))
        self.app.start_app()

        self.assertEqual(self.app._service.list_references()[-1].__str__(), self.book.__str__())    