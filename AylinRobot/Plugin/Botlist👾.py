# @AylinRobot
#@MusicAzBot
# Repo Açığdısa İcazəsis Götürmə Oğlum

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
async def delAcc(client, msj):
    chat_id = msj.chat.id
    DELETED = []
    members = app.iter_chat_members(chat_id)
    async for m in members:
        if m.user.is_deleted == True:
            DELETED.append(str(m.user.id)) # silinen hesablar

    shesablar = '\n'.join(DELETED) 
    await app.send_message(chat_id, f"silinen hesablarin sayi - {len(DELETED)}\n\n{shesablar}") 
    
    
@app.on_message(filters.commands=['google']))
def google_search(client, message):
    input_word = message.command[1]
    results = app.search.google(input_word)
    message.reply_text(f"Axtariş uzre melumat '{input_word}':\n\n{results}")