import unittest
from app import CommandLineUI
from entities.book import Book

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