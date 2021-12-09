class Message:

    def __init__(self, idMessage, sujet, nom, date, fichiers):
        self.id = idMessage
        self.sujet = sujet
        self.nom = nom
        self.date = date
        self.fichiers = fichiers

    def getIdMessage(self):
        return self.id

    def getSujet(self):
        return self.sujet

    def hasSujet(self):
        return len(self.sujet) > 0

    def getNom(self):
        return self.nom

    def getDate(self):
        return self.date

    def getFichiers(self):
        return self.fichiers

    def __str__(self):
        return f'Id: {self.id} Sujet: {self.getSujet()} Nom: {self.getNom()} Date: {self.getDate()} Fichiers: {self.getFichiers()}'