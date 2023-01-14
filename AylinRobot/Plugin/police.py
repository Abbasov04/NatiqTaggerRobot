# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import time
from asyncio import sleep
from time import time
from random import choice
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from pyrogram import idle, filters
from AylinRobot.config import Config
from pyrogram import Client, filters

@app.on_message(filters.command("police") & ~filters.edited)
async def police(app: Client, msg: Message):
    m = await msg.reply("🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵")
    await sleep(0.5)
    await m.edit("🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴")
    await sleep(0.5)
    await m.edit("🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵")
    await sleep(0.5)
    await m.edit("🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴")
    await sleep(0.5)
    await m.edit("🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵")
    await sleep (0.5)
    await m.edit("🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴")
    await sleep (0.5)
    await m.edit("[☆☆☆](https://telegra.ph/file/d7ee756e1fc2a759041be.mp4)")    