import os
from os import name

class CommandLineUI:
    def __init__(self, io, service):
        self._io = io
        self._service = service
        self._run = True

    def start_app(self):
        if name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        self._io.write("Tervetuloa viitekirjastoon!")
        while self._run is True:
            start_input = {
                'type': 'list',
                'name': 'start input',
                'message': 'Mitä haluat tehdä?',
                'choices': ['lisää viite','listaa viitteet', 'etsi viitteitä', 'siirrä viitteitä tiedostoon', 'poista viite', 'poistu']
                }
            user_input = self._io.read_pyinquirer(start_input)

            if user_input['start input'] == "lisää viite":

                add_input = {
                'type': 'list',
                'name': 'add input',
                'message': 'Missä muodossa viite lisätään',
                'choices': ['bibtex', 'ihmisluettava']
                }
                user_input = self._io.read_pyinquirer(add_input)

                if user_input['add input'] == "ihmisluettava":
                    add_input =  {
                    'type': 'list',
                    'name': 'add input',
                    'message': 'Minkälainen viite lisätään?',
                    'choices': ['kirja','lehtiartikkeli','gradu','tutkimusraportti','julkaisematon']
                    }
                    entry_type = self._io.read_pyinquirer(add_input)
                    self._service.add_reference_humanformat(entry_type['add input'])

                else:
                    self._service.add_reference_bibtexformat()


            elif user_input['start input'] == "listaa viitteet":
                add_input =  {
                'type': 'list',
                'name': 'add input',
                'message': 'Millä perusteella haluaisit listata viitteitä?',
                'choices': ['lisäysjärjestys', 'vuoden', 'tekijän', 'julkaisijan', 'viitetyypin', 'nimen']
                }
                entry_type = self._io.read_pyinquirer(add_input)
                self._service.sort_references(entry_type['add input'])

            elif user_input['start input'] == 'etsi viitteitä':
                add_input =  {
                'type': 'list',
                'name': 'add input',
                'message': 'Millä perusteella haluaisit etsiä viitteitä?',
                'choices': ['vuoden', 'tekijän', 'julkaisijan', 'viitetyypin', 'nimen']
                }
                entry_type = self._io.read_pyinquirer(add_input)
                self._service.filter_references(entry_type['add input'])

            elif user_input['start_input'] == 'poista viite':
                add_input =  {
                'type': 'checkbox',
                'qmark': 'X',
                'name': 'delete',
                'message': 'Mitkä viitteet poistetaan?',
                'choices': [self._service.list_reference]
                }

            elif user_input['start input'] == 'siirrä viitteitä tiedostoon':
                self._service.add_to_new_file()

            elif user_input['start input'] == "poistu":
                self._run = False
