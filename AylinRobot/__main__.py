# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Satan Kodları Götürən Kimliyindən Aslı Olmayaraq Peysərdi

import os
import psutil
import shutil
import string
import asyncio
from helpers.database.add_user import AddUserToDatabase
from helpers.forcesub import ForceSub
from AylinRobot.config import Config
from asyncio import TimeoutError
from AylinRobot.translation import Translation
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from AylinRobot.Plugin import *
from AylinRobot.Music import *
from AylinRobot.Oyunlar import *
from AylinRobot.Telethon import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from AylinRobot import AylinRobot as app
from AylinRobot import LOGGER

AylinIMG = f"{Config.START_IMG}"

@app.on_message(filters.private & filters.incoming & filters.command(['start']))
async def start(client, message):
    await AddUserToDatabase(client, message)
    FSub = await ForceSub(client, message)
    if FSub == 400:
        return
    await client.send_message(Config.LOG_CHANNEL, f"🙋‍♀️ Yeni İstifadəçi:\n\n🙎‍♀️ Ad: {message.from_user.name}\n[ling](https://t.me/{message.from_user.mention})\n🧟‍♀️ ID:`{message.from_user.id}`\n\n💁‍♀️ Bot: [{Config.BOT_NAME}](https://t.me/{Config.BOT_USERNAME})")
    await message.reply_photo(
        AylinIMG,
        caption=Translation.START_TEXT.format(message.from_user.mention, Config.BOT_USERNAME,Config.OWNER_NAME, Config.BOT_NAME),
        reply_markup=Button.START_BUTTONS
    )
    
    
app.start()
LOGGER.info(f"{Config.BOT_USERNAME} Uğurla Başladı Sahibim {Config.OWNER_NAME}")
idle()
