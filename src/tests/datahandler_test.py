import unittest 
from unittest.mock import mock_open, patch
from repositories.datahandler import BibtexHandler


class TestBibtexHandler(unittest.TestCase):
    def setUp(self):
        self.data = {
            "title": "Sinuhe Eqyptiläinen",
            "author": "Mika Waltari",
            "year": "1945",
            "publisher": "WSOY",
            "ID": "Waltari45",
            "ENTRYTYPE": "book"
        }
        self.list_data = list(self.data.values())
        self.list_data.insert(0, self.list_data.pop())
        self.bibHandler = BibtexHandler()

    def test_creating_bibtex_format_works(self):
        bibEntry = self.bibHandler._create_bibtex_format(self.list_data)
        self.assertEqual(bibEntry.entries[0], self.data)

    def test_writing_to_bib_file_works(self):
        write_mock = mock_open()
        with patch("builtins.open", write_mock):
            call_result = self.bibHandler.write_to_bib_file(self.list_data, write_mock)
        self.assertEqual(call_result, True)
        write_mock().write.assert_called()


    def test_reading_from_bib_file_works(self):
        read_mock = mock_open()
        with patch("builtins.open", read_mock):
            self.bibHandler.read_from_bib_file(read_mock)
        read_mock().read.assert_called()