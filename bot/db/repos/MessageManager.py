import pickle

from bot.db.entities.Message import Message


class MessageManager:
    def __init__(self, db):
        self._db = db

    def getAll(self):
        cur = self._db.cursor()
        cur.execute('SELECT * FROM Message')

        messages = []
        for message in cur.fetchall():
            messages.append(Message(message[5], message[1], message[2], message[3], message[4]))
        return messages

    def insert(self, message):
        cur = self._db.cursor()
        cur.execute('INSERT INTO Message (sujet, nom, date, fichiers, idMessage) values (?, ?, ?, ?, ?)',
                    (message.getSujet(), message.getNom(), message.getDate(), pickle.dumps(message.getFichiers()), message.getIdMessage(),))
        self._db.commit()