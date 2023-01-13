import logging

import time
from pyrogram import Client, filters, idle
from AylinRobot import AylinRobot as app
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import pyrogram
from AylinRobot.config import Config
from datetime import datetime

from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, idle, filters
from io import BytesIO
from aiohttp import ClientSession
#--------------------------------------------------------------


aiohttpsession = ClientSession()


async def get_http_status_code(url: str) -> int:
    async with aiohttpsession.head(url) as resp:
        return resp.status
    

async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiohttpsession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image

@app.on_message(filters.command("carbon"))
async def carbon_func(bot: app, msg: Message):
    m = await msg.reply_text("`Hazırlanır`")
    carbon = await make_carbon(msg.reply_to_message.text)
    await m.edit("`Göndərilir`")
    await bot.send_photo(msg.chat.id, photo=carbon)
    await m.delete()
    carbon.close()