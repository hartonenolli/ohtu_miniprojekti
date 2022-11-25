from app import CommandLineUI
from reader_writer import ReaderWriter

def main():
    io = ReaderWriter()
    ui = CommandLineUI(io)
    ui.start_app()


if __name__ == "__main__":
    main()
