import locale

from api.ecoledirecte.EcoleDirecte import EcoleDirecte
from bot.Client import CustomClient
from bot.config.Config import CustomConfig
from bot.db.Database import Database

print(f'Loading config ...')
locale.setlocale(locale.LC_TIME, 'fr_FR')
config = CustomConfig()
db = Database()

print(f'Loading api ...')
api = EcoleDirecte(config)

print(f'Loading client ...')
client = CustomClient(config, db, api)
client.run(config.getToken())