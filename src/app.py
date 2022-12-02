from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from PyInquirer import prompt

class CommandLineUI:
    def __init__(self, io, controller):
        self._io = io
        self._bibcontroller = controller
        self._run = True

    def start_app(self):
        self._io.write("Tervetuloa viitekirjastoon!")
        while self._run is True:
            start_input = {
                'type': 'list',
                'name': 'start input',
                'message': 'Mitä haluat tehdä?',
                'choices': ['lisää viite','listaa viitteet','poistu']
                }
            user_input = prompt(start_input)

            if user_input['start input'] == "lisää viite":
                add_input =  {
                'type': 'list',
                'name': 'add input',
                'message': 'Minkälainen viite lisätään?',
                'choices': ['kirja','lehtiartikkeli','gradu','muu']
                }
                reference = prompt(add_input)
                self.add_reference(reference['add input'])

            elif user_input['start input'] == "listaa viitteet":
                referencelist = self._bibcontroller.read_from_bib_file()
                for reference in referencelist:
                    self._io.write(reference)

            elif user_input['start input'] == "poistu":
                self._run = False

            else:
                self._io.write("Virheellinen syöte.")

    def add_reference(self, reference):
        self._io.write("Syötä viitteen tiedot:")
        title = self._io.read("Kirjan nimi: ")
        author = self._io.read("Kijailija: ")
        while True:
            try:
                year = int(self._io.read("Julkaisuvuosi: "))
                break
            except ValueError:
                self._io.write("Virheellinen syöte")
        publisher = self._io.read("Julkaisija: ")
        keyword = self._io.read("Avainsana, jolla haluat viitata teokseen: ")
        self._io.write(f"Lisätään {reference} {title} ({year}), kirjoittanut {author}, julkaissut {publisher}, avainsanalla {keyword}")

        data = (reference, title, author, year, publisher, keyword)
        if self._bibcontroller.write_to_bib_file(data):
            self._io.write("BibTex tiedoston kirjoittaminen onnistui")
        else:
            self._io.write("BibTex tiedoston kirjoittaminen epäonnistui")
