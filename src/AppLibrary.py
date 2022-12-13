from ui.app import CommandLineUI
from tempfile import NamedTemporaryFile
from repositories.datahandler import BibtexHandler
from services.reference_service import ReferenceServices
from services.filter_service import FilterService

class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def read(self, prompt):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        return ""

    def read_bibtex(self, prompt):
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
        self.outputs.append(prompt[0:len(prompt)-1])

    def add_input(self, value):
        self.inputs.append(value)

class AppLibrary():
    def __init__(self):
        self._io = StubIO()
        self._bibhandler = BibtexHandler()
        self._filterservice = FilterService()
        test_file = NamedTemporaryFile(encoding="utf-8", mode="w+", delete=False)
        self._ref_service = ReferenceServices(self._io, self._bibhandler, test_file.name, self._filterservice)
        self._app = CommandLineUI(self._io, self._ref_service)

    def input(self, value):
        self._io.add_input(value)

    def run_app(self):
        self._app.start_app()

    def output_should_contain(self, value):
        outputs = self._io.outputs
        if not value in outputs:
            raise AssertionError(f"Output \"{value}\" is not in {str(outputs)}")
    
    def first_output_filter(self, value):
        outputs = self._io.outputs
        if value != outputs[3]:
            raise AssertionError(f"Not same {str(outputs)}")
    
    def output_should_not_contain(self, value):
        outputs = self._io.outputs
        if value in outputs:
            raise AssertionError(f"Output \"{value}\" is in {str(outputs)}")