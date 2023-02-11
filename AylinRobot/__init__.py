# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Satan Kodları Götürən Kimliyindən Adlı Olmayaraq Peysərdi

import logging
from pyrogram import Client
from AylinRobot.config import Config
from telethon import TelegramClient
from logging import *

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



TOKEN    = config.TOKEN

API_ID   = config.API_ID

API_HASH = config.API_HASH

basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=INFO)

logger = getLogger(__name__)

_ = TelegramClient('AylinRobot', api_id=API_ID, api_hash=API_HASH)
bot = _.start(bot_token=TOKEN)