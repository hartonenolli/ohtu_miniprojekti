from app import CommandLineUI

class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def read(self, prompt):
        return self.inputs.pop(0)
    
    def write(self, prompt):
        self.outputs.append(prompt)

    def add_input(self, value):
        self.inputs.append(value)

class AppLibrary:
    def __init__(self):
        self._app = CommandLineUI()
        self._io = StubIO()

    def input(self, value):
        self._io.add_input(value)

    def start_app(self):
        self._app.start_app()
