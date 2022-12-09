from ui.app import CommandLineUI
from ui.reader_writer import ReaderWriter
from repositories.datahandler import BibtexHandler
from services.reference_service import ReferenceServices

def main():
    io = ReaderWriter()
    bibhandler = BibtexHandler()
    ref_service = ReferenceServices(io, bibhandler, "references.bib")
    ui = CommandLineUI(io, ref_service)
    ui.start_app()


if __name__ == "__main__":
    main()
