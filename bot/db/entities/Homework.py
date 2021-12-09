class Homework:

    def __init__(self, date, matiere, code_matiere, a_faire, id_devoir, documents_a_faire, donne_le, effectue, interrogation, rendre_en_ligne):
        self.date = date
        self.matiere = matiere
        self.code_matiere = code_matiere
        self.a_faire = a_faire
        self.id_devoir = id_devoir
        self.documents_a_faire = documents_a_faire
        self.donne_le = donne_le
        self.effectue = effectue
        self.interrogation = interrogation
        self.rendre_en_ligne = rendre_en_ligne

    def getDate(self):
        return self.date

    def getMatiere(self):
        return self.matiere

    def getCodeMatiere(self):
        return self.code_matiere

    def getAFaire(self):
        return self.a_faire

    def getIdDevoir(self):
        return self.id_devoir

    def getDocumentAFaire(self):
        return self.documents_a_faire

    def getDonneLe(self):
        return self.donne_le

    def getEffectue(self):
        return self.effectue

    def getInterrogation(self):
        return self.interrogation

    def getRendreEnLigne(self):
        return self.rendre_en_ligne

    def __str__(self):
        return f"Date: {self.date} Matiere: {self.matiere} CodeMatiere: {self.code_matiere} AFaire: {self.a_faire} idDevoir: {self.id_devoir} DocumentsAFaire: {self.documents_a_faire} DonneLe: {self.donne_le} Effectué: {self.effectue} Interrogation: {self.interrogation} RendreEnLigne: {self.rendre_en_ligne}"