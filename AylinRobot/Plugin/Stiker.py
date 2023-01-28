from io import BytesIO
from traceback import format_exc
from AylinRobot import AylinRobot as app
from AylinRobot import LOGGER
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message
from Python_ARQ import ARQ
from helpers.merrors import capture_err
import aiohttp
from pyrogram import Client, filters


import traceback
from asyncio import get_running_loop
from io import BytesIO

from googletrans import Translator
from gtts import gTTS
from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR


def convert(text):
    audio = BytesIO()
    i = Translator().translate(text, dest="en")
    lang = i.src
    tts = gTTS(text, lang=lang)
    audio.name = lang + ".ogg"
    tts.write_to_fp(audio)
    return audio


@app.on_message(filters.command(["tts"]))
async def text_to_speech(_, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("__😫Reply to some texts!__")
    if not message.reply_to_message.text:
        return await message.reply_text("__❗️Reply to some texts!__")
    m = await message.reply_text("🔁 Processing...")
    text = message.reply_to_message.text
    try:
        loop = get_running_loop()
        audio = await loop.run_in_executor(None, convert, text)
        await message.reply_audio(audio)
        await m.delete()
        audio.close()
    except Exception as e:
        await m.edit(str(e))
        es = traceback.format_exc()
        print(es)

