import asyncio

import discord

from bot.listener.HomeworkListener import HomeworkListener
from bot.listener.MessageListener import MessageListener


class CustomClient(discord.Client):

    def __init__(self, config, db, api, **options):
        super().__init__(**options)

        self._homework = None

        self._config = config
        self._db = db
        self._api = api
        self._index = 0

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        await self.updateRichPresence()
        asyncio \
            .get_event_loop() \
            .create_task(self.handleHomeworkLoop())
        asyncio \
            .get_event_loop() \
            .create_task(self.handleMessageLoop())

    async def updateRichPresence(self):
        await self \
            .change_presence(activity=discord.Game(name='L\'appel du devoir'))

    async def handleHomeworkLoop(self):
        await HomeworkListener(self, self._db, self._api, self._config) \
            .handle()

    async def handleMessageLoop(self):
        await MessageListener(self, self._db, self._api, self._config) \
            .handle()