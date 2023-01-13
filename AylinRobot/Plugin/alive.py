from pyrogram.types import Message, User
from AylinRobot import AylinRobot as app
from AylinRobot import LOGGER
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import pyrogram
from AylinRobot.config import Config
from datetime import datetime

from os import path
from time import time
from datetime import datetime

from pyrogram.errors import FloodWait
from sys import version_info
from time import time

from helpers.filters import command, other_filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


from helpers import __version__
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@app.on_message(
    command(["alive"]) & filters.group & ~filters.edited
)
async def start_group(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Etiraf Botumuz", url=f"https://t.me/{Config.ETIRAFBOT}"),
                InlineKeyboardButton(
                    "🎧 Playlist Kanalı", url=f"https://t.me/{Config.PLAYLIST_NAME}"
                ),
            ]
        ]
    )

    alive = f"**Haycan❤️ {message.from_user.mention()}, Mənim Adım {Config.BOT_USERNAME}**\n\n✨ Mən Super İşləyirəm\n🍀 Sahibim: [{Config.ALIVE_NAME}](https://t.me/{Config.OWNER_NAME})\n✨ Bot Versiyası: `v{__version__}`\n🍀 Pyrogram Versiyası: `{pyrover}`\n✨ Python Versiyası: `{__python_version__}`\n🍀 İş vaxtı Status: `{uptime}`\n\n**Məni Qrupunuza əlavə etdiyiniz üçün təşəkkürlər ** ❤"

    await message.reply_video(
        video=f"{Config.ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )