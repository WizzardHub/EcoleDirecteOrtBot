import json
from types import SimpleNamespace

import requests

from bot.db.entities.File import File
from bot.db.entities.Homework import Homework
from bot.db.entities.Message import Message


class EcoleDirecte:

    def __init__(self, config):
        # Variables
        self._token = None
        self._id = None
        self._session = None
        self._config = config

        # Methods
        self.handleLogin()

    def handleLogin(self):
        # Http Request
        url = "https://api.ecoledirecte.com/v3/login.awp"
        payload = "data={\"identifiant\": \"" + self._config.getUsername() + "\", \"motdepasse\": \"" + self._config.getPassword() + "\"}"
        response = requests.post(url, data=payload)
        # Parsing
        self._session = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))
        self._id = self._session.data.accounts[0].id
        self._token = self._session.token

    def getHomeworks(self):
        # Http Request
        url = f"https://api.ecoledirecte.com/v3/Eleves/{self._id}/cahierdetexte.awp?verbe=get"
        payload = "data={\"token\": \"" + self._token + "\"}"
        response = requests.post(url, data=payload)
        # Parsing
        json_content = json.loads(response.text)['data']

        homeworks = []
        for date in json_content:
            for key in json_content[date]:
                homeworks.append(Homework(date, key['matiere'], key['codeMatiere'], key['aFaire'], key['idDevoir'], key['documentsAFaire'], key['donneLe'], key['effectue'], key['interrogation'], key['rendreEnLigne']))

        return homeworks

    def getMessages(self):
        # Http Request
        url = f"https://api.ecoledirecte.com/v3/eleves/{self._id}/messages.awp?verbe=getall&orderBy=date&order=desc"
        payload = "data={\"token\": \"" + self._token + "\"}"
        response = requests.post(url, data=payload)
        # Parsing
        json_content = json.loads(response.text)['data']['messages']['received']

        messages = []
        for message in json_content:

            files = []
            for file in message['files']:
                files.append(File(file))

            messages.append(Message(message['id'], message['subject'], message['from']['name'], message['date'], files))

        return messages

    def getId(self):
        return self._id

    def getToken(self):
        return self._token
