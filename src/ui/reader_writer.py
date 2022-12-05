from PyInquirer import prompt

class ReaderWriter:
    def read(self, prompt):
        return input(prompt)

    def write(self, value):
        print(value)

    def read_pyinquirer(self, value):
        return prompt(value)
