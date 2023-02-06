# @AylinRobot
#@MusicAzBot
# Repo Açığdısa İcazəsis Götürmə Oğlum

from pyrogram.errors import FloodWait
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from AylinRobot import LOGGER
from AylinRobot.config import Config
from pyrogram import Client, idle, filters
from pyrogram import enums

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
    
    
    
# adminlist
@app.on_message(filters.command('alist'))
async def start(client, msj):
    chat_id = msj.chat.id
    reply = msj.reply_to_message
    ADMINS = []
    async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        ADMINS.append(m.user.mention)
        adminsiyahi = '\n'.join(ADMINS)

    #adminsiyahi = '\n'.join(ADMINS)
    t = f"Qrupdaki adminler\n{adminsiyahi}"
    await app.send_message(chat_id, t)    