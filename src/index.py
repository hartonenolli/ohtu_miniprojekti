from ui.app import CommandLineUI
from ui.reader_writer import ReaderWriter
from repositories.datahandler import BibtexHandler
from services.reference_service import ReferenceServices
from services.filter_service import FilterService

def main():
    io = ReaderWriter()
    bibhandler = BibtexHandler()
    filterservice = FilterService()
    ref_service = ReferenceServices(io, bibhandler, "references.bib", filterservice)
    ui = CommandLineUI(io, ref_service)
    ui.start_app()


if __name__ == "__main__":
    main()
