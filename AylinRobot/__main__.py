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
from Telethon.Plugin import Telethon
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from AylinRobot.Plugin import *
from AylinRobot.Music import *
from AylinRobot.Oyunlar import *
from Telethon.Plugin import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from AylinRobot import AylinRobot as app
from AylinRobot import LOGGER
    
    
app.start()
LOGGER.info(f"{Config.BOT_USERNAME} Uğurla Başladı Sahibim {Config.OWNER_NAME}")
idle()