from bibtexparser.bibdatabase import BibDatabase
class FilterService():
    def __init__(self) -> None:
        pass

    def sort_by(self, bib_database, sort_keyword, descending=False):
        if descending:
            bib_database.entries.sort(key= lambda reference : reference[sort_keyword], reverse=True)
            return bib_database
        bib_database.entries.sort(key = lambda reference : reference[sort_keyword])
        return bib_database

    def filter_by(self, bib_database, filter_keyword : str, match_case):
        bib_result_database = BibDatabase()
        bib_result_database.entries = [reference for reference in bib_database.entries
        if filter_keyword in reference and reference[filter_keyword].find(match_case) != -1]
        return bib_result_database
