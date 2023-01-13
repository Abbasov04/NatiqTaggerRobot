import secrets
import string
import aiohttp
from AylinRobot import AylinRobot as app

from pyrogram import filters
from Sehid import random_line


@app.on_message(filters.command("sehid") & ~filters.edited)
async def commit(_, message):
    await message.reply_text((await random_line('Sehid/sehid.txt')))