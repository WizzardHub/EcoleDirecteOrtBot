from bot.db.entities.Homework import Homework


class HomeworkManager:

    def __init__(self, db):
        self._db = db

    def getAll(self):
        cur = self._db.cursor()
        cur.execute('SELECT * FROM Homework')

        homeworks = []
        for homework in cur.fetchall():
            homeworks.append(Homework(homework[1], homework[2], homework[3], homework[4], homework[5], homework[6], homework[7], homework[8], homework[9], homework[10]))
        return homeworks

    def insert(self, homework):
        cur = self._db.cursor()
        cur.execute('INSERT INTO Homework (date, matiere, codeMatiere, aFaire, idDevoir'
                    ', documentsAFaire, donneLe, effectue, interrogation, rendreEnLigne'
                    ') values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                    (homework.getDate(), homework.getMatiere(), homework.getCodeMatiere(),
                     homework.getAFaire(), homework.getIdDevoir(), homework.getDocumentAFaire(),
                     homework.getDonneLe(), homework.getEffectue(), homework.getInterrogation(),
                     homework.getRendreEnLigne(),))
        self._db.commit()