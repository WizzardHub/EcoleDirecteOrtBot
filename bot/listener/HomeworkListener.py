import asyncio
from time import strftime, strptime

import discord

from bot.db.repos.HomeworkManager import HomeworkManager


class HomeworkListener:

    def __init__(self, client, db, api, config):
        self._client = client
        self._db = db
        self._api = api
        self._config = config

    async def handle(self):

        client = self._client
        db = self._db
        api = self._api
        config = self._config

        repo = HomeworkManager(db.getDb())
        homeworks = api.getHomeworks()

        while True:
            for web in homeworks:
                exists = False
                for db in repo.getAll():
                    if db.getIdDevoir() == web.getIdDevoir():
                        exists = True

                if exists is False:
                    repo.insert(web)
                    channel = client.get_channel(config.getHomework())

                    emb = discord.Embed(title=(web.getMatiere() if bool(
                        web.getInterrogation()) is False else f'{web.getMatiere()} (Intérrogation)'),
                                        description=f'> :books: On dirais qu\'il y a du taff à faire, cheh.\n> :smirk: Ça à pas l\'air compliqué en 10h c\'est poncé !\n > :lying_face: Tant que c\'est pas du C# ça va, il faut relativiser aussi.\n',
                                        color=(0x0f8fd1 if bool(web.getInterrogation()) is False else 0xde2a2a))
                    emb.add_field(name=':clock1: Donné le',
                                  value=f'`{strftime("%A %d %B %Y", strptime(web.getDonneLe(), "%Y-%m-%d"))}`',
                                  inline=True)
                    emb.add_field(name=':clock1: Deadline',
                                  value=f'`{strftime("%A %d %B %Y", strptime(web.getDate(), "%Y-%m-%d"))}`',
                                  inline=True)
                    emb.set_image(url='https://i.imgur.com/B5UvW3S.png')
                    emb.set_footer(text=f'EcoleDirecteBot - {strftime("%A %d %B %Y")}',
                                   icon_url='https://i.imgur.com/GECZEmd.png')
                    await channel.send(embed=emb)

            await asyncio.sleep(30)