# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə

import random
from random import choice
from helpers.filters import command, other_filters
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from pyrogram import idle, filters
from pyrogram.errors import FloodWait
from AylinRobot.config import Config
from Mesajlar.Mesajlar import salam, necesen, sagol, getdim, geldim, ban

active_chats = []

@app.on_message(command(["chatbot"]) & filters.group & ~filters.edited)
async def chatbot_status(_, message):
    global active_chats
    if len(message.command) != 2:
        await message.reply_text("/chatbot [ON] və yaxud [OFF] yazmadınız")
        return
    status = message.text.split(None, 1)[1]
    chat_id = message.chat.id
    
    if status == "ON" or status == "on" or status == "On":
        if chat_id not in active_chats:
            active_chats.append(chat_id)
            text = "✅ **ChatBot bu qrupda aktiv olundu !**"
            await message.reply_text(text)
            return
        await message.reply_text("⚠️ **ChatBot onsuzda aktivdir !**")
        return
    elif status == "OFF" or status == "off" or status == "Off":
        if chat_id in active_chats:
            active_chats.remove(chat_id)
            await message.reply_text("⛔️ **ChatBot bu qrupda deaktiv olundu !**")
            return
        await message.reply_text("⚠️ **ChatBot onsuzda deaktivdir !**")
        return
    
    else:
        await message.reply_text("/chatbot [ON] və yaxud [OFF] yazmadınız")
        
        
