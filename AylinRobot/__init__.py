# Leo Projects <https://t.me/leosupportx>

import logging
from pyrogram import Client
from config import API_HASH, API_ID, BOT_TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

LeoSongDownloaderBot = Client("LeoSongDownloaderBot", bot_token=BOT_TOKEN, api_hash=API_HASH, api_id=API_ID)
