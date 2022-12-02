from app import CommandLineUI
from reader_writer import ReaderWriter
from services.reference_service import BibtexController

def main():
    io = ReaderWriter()
    bibcontroller = BibtexController()
    ui = CommandLineUI(io, bibcontroller)
    ui.start_app()


if __name__ == "__main__":
    main()
