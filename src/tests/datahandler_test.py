import unittest 
from unittest.mock import mock_open, patch
from tempfile import NamedTemporaryFile
from os import unlink
from repositories.datahandler import BibtexHandler
from entities.reference import Reference


class TestBibtexHandler(unittest.TestCase):
    def setUp(self):
        self.data = {
            "title": "Sinuhe Egyptiläinen",
            "author": "Mika Waltari",
            "year": "1945",
            "publisher": "WSOY",
            "ID": "Waltari45",
            "ENTRYTYPE": "book"
        }
        self.data_humanformat = Reference("kirja", "Waltari45", "Sinuhe Egyptiläinen", "Mika Waltari", "1945", "WSOY")
        self.humanbibtex_entry = self.data_humanformat.create_bibtex_entry()
        self.data_bibtexformat = "@book{Waltari45,"\
        "author = {Mika Waltari},"\
        "title = {Sinuhe Egyptiläinen},"\
        "year = {1945},"\
        "publisher = {WSOY},"\
        "}"

        self.bibHandler = BibtexHandler()

    def test_creating_bibtex_format_works_bibtexformat(self):
        bibEntry = self.bibHandler._create_bibtex_format_bibtexformat(self.data_bibtexformat)
        self.assertEqual(bibEntry.entries[0], self.data)

    def test_writing_to_bib_file_works_humanformat(self):
        write_mock = mock_open()
        with patch("builtins.open", write_mock):
            call_result = self.bibHandler.write_to_bib_file_humanformat(self.humanbibtex_entry, write_mock)
        self.assertEqual(call_result, True)
        write_mock().write.assert_called()

    def test_writing_to_bib_file_works_bibtexformat(self):
        write_mock = mock_open()
        with patch("builtins.open", write_mock):
            call_result = self.bibHandler.write_to_bib_file_bibtexformat(self.data_bibtexformat, write_mock)
        self.assertEqual(call_result, True)
        write_mock().write.assert_called()

    def test_reading_from_bib_file_works(self):
        read_mock = mock_open()
        with patch("builtins.open", read_mock):
            self.bibHandler.read_from_bib_file(read_mock)
        read_mock().read.assert_called()

    def test_read_contents_correct(self):
        test_file = NamedTemporaryFile(encoding="utf-8", mode="w+", delete=False)
        self.bibHandler.write_to_bib_file_humanformat(self.humanbibtex_entry, test_file.name)
        read_result = self.bibHandler.read_from_bib_file(test_file.name)
        self.assertEqual(read_result.entries[0], self.data)
        unlink(test_file.name)

    def test_rewrite_to_bib_file_works_humanformat(self):
        write_mock = mock_open()
        with patch("builtins.open", write_mock):
            call_result = self.bibHandler.rewrite_bib_file_humanformat([self.humanbibtex_entry], write_mock)
        self.assertEqual(call_result, True)
        write_mock().write.assert_called()