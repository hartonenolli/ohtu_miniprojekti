class Reference:
    def __init__(self, type, title, author, year=None, publisher=None, journal=None, school=None, institution=None, note=None):
        self._type = type
        self._title = title
        self._author = author
        self._year = year
        self._publisher = publisher
        self._journal = journal
        self._school  = school
        self._institution = institution
        self._note = note

    def __str__(self):
        if self._type == 'book':
            return f"{self._author}. {self._year}. {self._title}. {self._publisher}."
        elif self._type == 'article':
            return f"{self._author}. {self._year}. {self._title}. {self._journal}."
        elif self._type == 'thesis':
            return f"{self._author}. {self._year}. {self._title}. {self._school}."
        elif self._type == 'tech report':
            return f"{self._author}. {self._year}. {self._title}. {self._institution}."
        else:
            if self._year != None:
                return f"{self._author}. {self._year}. {self._title}. {self._note}."
            else:
                return f"{self._author}. {self._title}. {self._note}."
