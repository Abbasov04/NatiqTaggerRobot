import os
import re
import sys
import asyncio
import subprocess
import speedtest
from asyncio import sleep
from AylinRobot import AylinRobot as app
from pyrogram.types import Message
from helpers.filters import command
from pyrogram import Client, filters
from os import system, execle, environ
from AylinRobot.config import Config
from helpers.formatters import bytes

@app.on_message(command(["hiz"]) & ~filters.edited)
async def run_speedtest(_, message: Message):
    m = await message.reply_text("⚡️ çalışan sunucu hız testi")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = await m.edit("⚡️ indirme hızını çalıştırma..")
        test.download()
        m = await m.edit("⚡️ yükleme hızını çalıştırma...")
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        await m.edit(e)
        return
    m = await m.edit("🔄 en hızlı sonuçları paylaşma")
    path = wget.download(result["share"])

    output = f"""💡 **Hız Testi Sonuçları**
    
<u>**Client:**</u>
**ISP:** {result['client']['isp']}
**Ülke:** {result['client']['country']}
  
<u>**sunucu:**</u>
**İsim:** {result['server']['name']}
**Ülke:** {result['server']['country']}, {result['server']['cc']}
**Sponsor:** {result['server']['sponsor']}
**gecikme:** {result['server']['latency']}

⚡️ **Ping:** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=path, caption=output
    )
    os.remove(path)
    await m.delete()
