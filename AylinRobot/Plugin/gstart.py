from AylinRobot.config import Config
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from pyrogram import idle, filters
from AylinRobot.config import Config
from pyrogram import Client, filters

import logging
from tglogging import TelegramLogHandler

# TGLOGGING Uygulamanızın logunu Telegram'a anlık göndermenizi sağlar. 

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        TelegramLogHandler(
            token=f"{Config.BOT_TOKEN}", 
            Config.LOG_GROUP=f"{Config.LOG_GROUP}", 
            update_interval=27, 
            minimum_lines=1000, # Her Mesajda gönderilecek satır sayısı
            pending_logs=200000),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(f"{Config.BOT_USERNAME}")

logger.info("Telegram'a canlı log başlatıldı.")