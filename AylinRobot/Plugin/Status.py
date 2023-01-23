import os
import time
import psutil
import shutil
import string
import asyncio
from helpers.display_progress import humanbytes
from AylinRobot.config import Config
from AylinRobot import AylinRobot as app
from AylinRobot import LOGGER
from pyrogram import idle, filters
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait, UserNotParticipant
from helpers.database.access_db import db
from helpers.database.add_user import AddUserToDatabase


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