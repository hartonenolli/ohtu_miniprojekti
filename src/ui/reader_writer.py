from PyInquirer import prompt
from prompt_toolkit import prompt as toolprompt

class ReaderWriter:
    def read(self, prompt):
        return input(prompt)

    def write(self, value):
        print(value)

    def read_pyinquirer(self, value):
        return prompt(value)

    def read_bibtex(self, prompt):
        return toolprompt(prompt)
