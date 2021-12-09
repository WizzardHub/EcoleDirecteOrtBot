import os
import sqlite3


class Database:

    def __init__(self):
        self._conn = sqlite3.connect(os.path.dirname(__file__) + '\\Database.db', check_same_thread=False)
        self._cur = self._conn.cursor()
        self.handleNewsTable()
        self.handleHomeworkTable()

    def getDb(self):
        return self._conn

    def close(self):
        self._conn.close()

    def handleHomeworkTable(self):
        self._cur.execute('create table if not exists Homework(id integer primary key autoincrement, date date, matiere text, codeMatiere text, aFaire boolean, idDevoir integer, documentsAFaire boolean, donneLe date, effectue boolean, interrogation boolean, rendreEnLigne boolean)')
        self._conn.commit()

    def handleNewsTable(self):
        self._cur.execute('create table if not exists News(id integer primary key autoincrement, sujet text, nom text, date date, fichiers integer)')
        self._conn.commit()