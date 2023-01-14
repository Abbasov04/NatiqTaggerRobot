# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os
import asyncio
import random
import time
from asyncio import sleep
from time import time
from random import choice
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from pyrogram import idle, filters
from AylinRobot.config import Config
from pyrogram import Client, filters

@app.on_message(filters.command("yd") & ~filters.private & ~filters.channel)
async def yd(app: Client, msg: Message):
    m = await msg.reply("✍️ indi sənin Yalan və ya Doğru Söylədiyini araşdıracam")
    await sleep(0.9)
    await m.edit("❤️Niyə inanım ki sənə?🧐")
    await sleep(1)
    await m.edit("Araşıdıraq görək yalan deyirsən ya doğru🔬")
    await sleep(0.5)
    await m.edit("araşdırılır...🔎")
    await sleep(0.1)
    await m.edit("Yalan🤥")
    await sleep (0.1)
    await m.edit("Doğru👍")
    await sleep (0.1)
    await m.edit("Yalan🤥")    
    await sleep (0.1)
    await m.edit("Doğru👍")
    await sleep (0.4)
    await m.edit(random.choice(["Yalan deyirsən❌", "Doğru deyirsən✅"]))

