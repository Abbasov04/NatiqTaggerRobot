# @AylinRobot
#@MusicAzBot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə

import os
import time
import psutil
import shutil
import string
import asyncio
from AylinRobot.config import Config
from asyncio import TimeoutError
from AylinRobot.translation import Translation
from helper.database.access_db import db
from helper.broadcast import broadcast_handler
from helper.database.add_user import AddUserToDatabase
from helper.display_progress import humanbytes
from pyrogram import Client
from helper.forcesub import ForceSub
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from LeoSongDownloaderBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from LeoSongDownloaderBot import LeoSongDownloaderBot as app
from LeoSongDownloaderBot import LOGGER

AylinIMG = f"{Config.START_IMG}"

@app.on_message(filters.command("start"))
async def start(client, message):
    await AddUserToDatabase(client, message)
    FSub = await ForceSub(client, message)
    if FSub == 400:
        return
    await message.reply_photo(
        AylinIMG,
        caption=Translation.START_TEXT.format(message.from_user.mention),
        reply_markup=Translation.START_BUTTONS
    )
    
@app.on_message(filters.private & filters.command("broadcast") & filters.user(Config.OWNER_ID) & filters.reply)
async def _broadcast(_, client: Message):
    await broadcast_handler(client)


@app.on_message(filters.private & filters.command("status") & filters.user(Config.OWNER_ID))
async def show_status_count(_, client: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await client.reply_text(
        text=f"**Ümumi Disk Sahəsi:** {total} \n**İstifadə edilmiş Sahə:** {used}({disk_usage}%) \n**Boş Yer:** {free} \n**CPU  İstifadə:** {cpu_usage}% \n**RAM İstifadəsi:** {ram_usage}%\n\n**{Config.BOT_USERNAME}-Ümumi İstifadəçiləri:** `{total_users}`"  ,
        parse_mode="Markdown",
        quote=True
    )

app.start()
LOGGER.info(f"{Config.BOT_USERNAME} Uğurla Başladı Sahibim {Config.OWNER_NAME}")
idle()
