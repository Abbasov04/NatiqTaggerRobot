# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Satan Kodları Götürən Kimliyindən Adlı Olmayaraq Peysərdi

import logging
from pyrogram import Client
from AylinRobot.config import Config

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

AylinRobot = Client(
    'AylinRobot',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)


from telethon import TelegramClient

from Telethon.Mesajlar import * 

from logging import *
from AylinRobot.config import Config

TOKEN    = Config.TOKEN
API_ID   = Config.API_ID
API_HASH = Config.API_HASH

basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=INFO)

logger = getLogger(__name__)

_ = TelegramClient('Aylin', api_id=API_ID, api_hash=API_HASH)
bot = _.start(bot_token=TOKEN)

owner = config.OWNER

anlıq = []

tək = []

qruplar = []

istifadeci = []

admins = []

delay = Config.DELAY

botadı = Config.BOT_USERNAME

