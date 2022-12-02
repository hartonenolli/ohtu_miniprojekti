import unittest
from app import CommandLineUI
from entities.book import Book
from unittest.mock import Mock

class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def read(self, prompt):
        return self.inputs.pop(0)
    
    def write(self, prompt):
        self.outputs.append(prompt)

class TestCommandLineUI(unittest.TestCase):
    def setUp(self):
        self.book = Book("Mika Waltari", "Sinuhe Egyptiläinen", "WSOY", "1945")

    def test_user_input_exit_works(self):
        io = StubIO(["poistu"])
        self.app = CommandLineUI(io)
        self.app.start_app()
        
        self.assertEqual(self.app._run, False)

    def test_user_input_add_reference_works(self):
        io = StubIO(["lisää viite", "kirja", "1", "2", "3", "4", "5", "poistu"])
        self.app = CommandLineUI(io)
        self.app.start_app()

        self.assertEqual(len(self.app._references), 1)

    def test_user_input_not_in_options_works(self):
        io = StubIO(["käpistely", "poistu"])
        self.app = CommandLineUI(io)
        self.app.start_app()

        self.assertEqual(io.outputs[1], "Virheellinen syöte.")

    def test_user_input_list_references_works(self):
        io = StubIO(["lisää viite", "kirja", "Sinuhe Egyptiläinen", "Mika Waltari", "1945", "WSOY", "Waltari45", "listaa viitteet", "poistu"])
        self.app = CommandLineUI(io)
        self.app.start_app()

        self.assertEqual(io.outputs[-1].__str__(), self.book.__str__())

    def test_add_reference_adds_correct_string_to_database(self):
        io = StubIO(["Sinuhe Egyptiläinen", "Mika Waltari", "1945", "WSOY", "Waltari45"])
        self.app = CommandLineUI(io)
        self.app._references.append("kirja")
        self.app.add_reference("kirja")
        self.app.read_from_bib_file()

        self.assertEqual(io.outputs[-1].__str__(), self.book.__str__())