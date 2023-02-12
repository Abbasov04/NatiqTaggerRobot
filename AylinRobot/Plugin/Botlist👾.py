# @AylinRobot
#@MusicAzBot
# Repo Açığdısa İcazəsis Götürmə Oğlum

import time
from asyncio import sleep
from time import time
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from AylinRobot.config import Config
from pyrogram import Client, filters

@app.on_message(filters.command('list') & filters.group)
async def start(client, msj):
    BOTLAR = []
    chat_id = msj.chat.id
    async for members in app.iter_chat_members(chat_id):
        botmu = members.user.is_bot
        if botmu == True:
            BOTLAR.append(members.user.mention)
            botlarsiyahi = '\n'.join(BOTLAR)
        else:
            pass

    botlarsiyahi = '\n'.join(BOTLAR)
    await client.send_message(chat_id, botlarsiyahi)
    
    
@app.on_message(filters.command("del") & filters.group)
async def delAcc(client, msg):
    chat_id = msg.chat.id
    a = await client.send_message(chat_id, "Silinən Hesablar Axtarılır")
    await time.sleep(2.5)
    await app.delete_messages(chat_id, a.id)
    b = await client.send_message(chat_id, "Silinən Hesablar Göndərilir")
   await time.sleep(2.5)
    DELETED = []
    members = app.iter_chat_members(chat_id)
    async for m in members:
        if m.user.is_deleted == True:
            DELETED.append(str(m.user.id)) # silinen hesablar

    shesablar = '\n'.join(DELETED)
    await app.delete_messages(chat_id, b.id)
    await app.send_message(chat_id, f"🙎‍♀️ botun adi Silinən Hesabları Tapdı Silinən Hesablar- 👻 {len(DELETED)} {shesablar} 🙋‍♀️ Axtaran {msg.from_user.mention}")