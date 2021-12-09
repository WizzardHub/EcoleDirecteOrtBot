import asyncio
from time import strftime, strptime

import discord

from bot.db.repos.MessageManager import MessageManager


class MessageListener:

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

        repo = MessageManager(db.getDb())
        messages = api.getMessages()

        while True:
            for web in messages:
                exists = False
                for db in repo.getAll():
                    if db.getIdMessage() == web.getIdMessage():
                        exists = True

                if exists is False:
                    channel = client.get_channel(config.getInbox())
                    repo.insert(web)

                    fichiers = ''
                    if len(web.getFichiers()) > 0:
                        for fichier in web.getFichiers():
                            fichiers += f' - :file_folder: `{fichier.getLibelle()}`\n'
                    emb = discord.Embed(title=str(web.getSujet()).upper() if web.hasSujet() else '[AUCUN OBJET]', description=f'> :exclamation: Un nouveau message viens d\'arriver !\n> :envelope: Veuillez prendre conaissance de ce message au plus vite !\n', color=0x0f8fd1)
                    emb.add_field(name=f':clock10: Reçu le', value=f'`{strftime("%A %d %B %Y à %H:%M", strptime(web.getDate(), "%Y-%m-%d %H:%M:%S"))}`', inline=True)
                    emb.add_field(name=f':person_curly_hair: Par', value=f'`{web.getNom()}`', inline=True)
                    emb.set_image(url='https://i.imgur.com/B5UvW3S.png')
                    emb.add_field(name=f':link: Fichiers liés :', value=(':warning: `Aucun fichiers liée à ce message.`' if len(web.getFichiers()) == 0 else fichiers), inline=False)
                    emb.set_footer(text=f'EcoleDirecteBot - {strftime("%A %d %B %Y")}',
                                   icon_url='https://i.imgur.com/GECZEmd.png')
                    await channel.send(embed=emb)

            await asyncio.sleep(30)