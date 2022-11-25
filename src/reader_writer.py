class ReaderWriter:
    def __init__(self):
        self.testi = "testi"

    def read(self,prompt):
        return input(prompt)

    def write(self, value):
        print(value)
