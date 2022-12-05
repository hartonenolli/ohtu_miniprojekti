from ui.app import CommandLineUI
from repositories.datahandler import BibtexHandler
from services.reference_service import ReferenceServices

class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def read(self, prompt):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        return ""

    def read_pyinquirer(self, value):
        d = {}
        if len(self.inputs) > 0:
            d[value["name"]] = self.inputs.pop(0)
            return d
        return ""

    def write(self, prompt):
        self.outputs.append(prompt)

    def add_input(self, value):
        self.inputs.append(value)

class AppLibrary():
    def __init__(self):
        self._io = StubIO()
        self._bibhandler = BibtexHandler()
        self._ref_service = ReferenceServices(self._io, self._bibhandler)
        self._app = CommandLineUI(self._io, self._ref_service)

    def input(self, value):
        self._io.add_input(value)

    def input_int(self, value):
        self._io.add_input(int(value))

    def run_app(self):
        self._app.start_app()

    def output_should_contain(self, value):
        outputs = self._io.outputs
        if not value in outputs:
            raise AssertionError(f"Output \"{value}\" is not in {str(outputs)}")
