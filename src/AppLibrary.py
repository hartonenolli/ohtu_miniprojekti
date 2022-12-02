from app import CommandLineUI

class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def read(self):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        return ""

    def write(self, prompt):
        self.outputs.append(prompt)

    def add_input(self, value):
        self.inputs.append(value)

class AppLibrary():
    def __init__(self):
        self._io = StubIO()
        # täällä pitäisi olla alustettuna BibtexController
        self._app = CommandLineUI(self._io)

    def input(self, value):
        self._io.add_input(value)

    def run_app(self):
        self._app.start_app()

    def output_should_contain(self, value):
        outputs = self._io.outputs
        if not value in outputs:
            raise AssertionError(f"Output \"{value}\" is not in {str(outputs)}")
