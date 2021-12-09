import os

from dotenv import load_dotenv


class CustomConfig:
    def __init__(self):
        load_dotenv()
        self._token = os.getenv('DISCORD_TOKEN')
        self._guild = int(os.getenv('DISCORD_GUILD'))
        self._channel_inbox = int(os.getenv('DISCORD_CHANNEL_INBOX'))
        self._channel_homework = int(os.getenv('DISCORD_CHANNEL_HOMEWORK'))

        self._username = os.getenv('API_USERNAME')
        self._password = os.getenv('API_PASSWORD')

    def getToken(self):
        return self._token

    def getGuild(self):
        return self._guild

    def getInbox(self):
        return self._channel_inbox

    def getHomework(self):
        return self._channel_homework

    def getUsername(self):
        return self._username

    def getPassword(self):
        return self._password