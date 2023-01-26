# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os
import time
import psutil
import shutil
import string
import asyncio
from AylinRobot.config import Config
from asyncio import TimeoutError
from AylinRobot.translation import Translation
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from AylinRobot.Plugin import *
from AylinRobot.Music import *
from AylinRobot.Oyunlar import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from AylinRobot import AylinRobot as app
from AylinRobot import LOGGER

AylinIMG = f"{Config.START_IMG}"

@app.on_message(filters.private & filters.incoming & filters.command(['start']))
async def start(client, message):
    await message.reply_photo(
        AylinIMG,
        caption=Translation.START_TEXT.format(message.from_user.mention, Config.BOT_USERNAME),
        reply_markup=Button.START_BUTTONS
    )
    
    


    await app.start()
    ...  # Invoke API methods
    await app.restart()
    ...  # Invoke other API methods
    await app.stop()


app.run(main())

idle()