from bibtexparser.bibdatabase import BibDatabase
class FilterService():
    def __init__(self) -> None:
        pass

    def sort_by_year(self, bib_database, descending=False):
        if descending:
            bib_database.entries.sort(key= lambda x : x["year"], reverse=True)
            return bib_database
        bib_database.entries.sort(key = lambda x : x["year"])
        return bib_database
    
    def filter_by_year(self, bib_database, year : int):
        bib_result_database = BibDatabase()
        bib_result_database.entries = [n for n in bib_database.entries if int(n["year"]) == year]
        return bib_result_database
    
    def sort_by_author(self, bib_database, descending=False):
        if descending:
            bib_database.entries.sort(key= lambda x : x["author"], reverse=True)
            return bib_database
        bib_database.entries.sort(key = lambda x : x["author"])
        return bib_database
    
    def filter_by_author(self, bib_database, author : str):
        bib_result_database = BibDatabase()
        bib_result_database.entries = [n for n in bib_database.entries if n["author"].lower() == author.lower()]
        return bib_result_database

    def sort_by_title(self, bib_database, descending=False):
        if descending:
            bib_database.entries.sort(key= lambda x : x["title"], reverse=True)
            return bib_database
        bib_database.entries.sort(key = lambda x : x["title"])
        return bib_database
    
    def filter_by_title(self, bib_database, title : str):
        bib_result_database = BibDatabase()
        bib_result_database.entries = [n for n in bib_database.entries if n["title"].lower() == title.lower()]
        return bib_result_database 

    def sort_by_publisher(self, bib_database, descending=False):
        if descending:
            bib_database.entries.sort(key= lambda x : x["publiser"], reverse=True)
            return bib_database
        bib_database.entries.sort(key = lambda x : x["publisher"])
        return bib_database
    
    def filter_by_publisher(self, bib_database, publisher : str):
        bib_result_database = BibDatabase()
        bib_result_database.entries = [n for n in bib_database.entries if n["publisher"].lower() == publisher.lower()]
        return bib_result_database 

    def sort_by_entrytype(self, bib_database, descending=False):
        if descending:
            bib_database.entries.sort(key= lambda x : x["ENTRYTYPE"], reverse=True)
            return bib_database
        bib_database.entries.sort(key = lambda x : x["ENTRYTYPE"])
        return bib_database
    
    def filter_by_entrytype(self, bib_database, entrytype : str):
        bib_result_database = BibDatabase()
        bib_result_database.entries = [n for n in bib_database.entries if n["ENTRYTYPE"].lower() == entrytype.lower()]
        return bib_result_database 