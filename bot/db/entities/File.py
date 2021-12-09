class File:

    def __init__(self, file):
        self._libelle = None
        self._date = None

        if len(file) <= 0:
            return

        self._libelle = file['libelle']
        self._date = file['date']

    def getLibelle(self):
        return self._libelle

    def getDate(self):
        return self._date

    def isEmpty(self):
        return self._libelle is None

    def __str__(self):
        return f'Libelle: {self._libelle} Date: {self._date}'