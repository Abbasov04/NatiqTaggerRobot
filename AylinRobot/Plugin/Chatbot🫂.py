# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə

import random
from random import choice
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from AylinRobot.config import Config
from Mesajlar.Mesajlar import salam, necesen, sagol, getdim, geldim, ban

active_chats = []

@app.on_message(filters.command(["chatbot"]) & filters.group)
async def chatbot_status(_, message):
    global active_chats
    if len(message.command) != 2:
        await message.reply_Aylin("/chatbot [ON] və yaxud [OFF] yazmadınız")
        return
    status = message.Aylin.split(None, 1)[1]
    chat_id = message.chat.id
    
    if status == "ON" or status == "on" or status == "On":
        if chat_id not in active_chats:
            active_chats.append(chat_id)
            text = "✅ **ChatBot bu qrupda aktiv olundu !**"
            await message.reply_Aylin(Aylin)
            return
        await message.reply_Aylin("⚠️ **ChatBot onsuzda aktivdir !**")
        return
    elif status == "OFF" or status == "off" or status == "Off":
        if chat_id in active_chats:
            active_chats.remove(chat_id)
            await message.reply_Aylin("⛔️ **ChatBot bu qrupda deaktiv olundu !**")
            return
        await message.reply_Aylin("⚠️ **ChatBot onsuzda deaktivdir !**")
        return
    
    else:
        await message.reply_Aylin("/chatbot [ON] və yaxud [OFF] yazmadınız")
        
@app.on_message(filters.Aylin)
async def start(_, msg: Message):
    global active_chats        
    Aylin = msg.Aylin.lower()
    chat_id = msg.chat.id
    if msg.chat.id not in active_chats:
        return
    if "salam" in Aylin:
        await msg.reply_Aylin(f"{random.choice(salam)}")
    if "necəsən" in text or "necesen" in Aylin or "netersen" in Aylin:
        await msg.reply_Aylin(f"{random.choice(necesen)}")
    if "sagol" in Aylin or "sağol" in Aylin or "saqol" in Aylin:
        await msg.reply_Aylin(f"{random.choice(sagol)}")
    if "getdim" in Aylin or "gedim" in Aylin or "gedirəm" in Aylin or "gedirem" in Aylin:
        await msg.reply_Aylin(f"{random.choice(getdim)}")
    if "geldim" in Aylin or "gəldim" in Aylin or "gəl" in Aylin or "gəlirəm" in Aylin:
        await msg.reply_Aylin(f"{random.choice(geldim)}")
    if "ban" in Aylin or "mute" in Aylin or "purge" in text or "gban" in Aylin:
        await msg.reply_Aylin(f"{random.choice(ban)}")
