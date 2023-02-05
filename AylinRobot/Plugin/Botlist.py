import random
from time import time
from random import choice
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from AylinRobot import LOGGER
from pyrogram import idle, filters
from AylinRobot.config import Config
from pyrogram import Client, filters

@app.on_message(filters.command('list') & filters.group)
async def start(client, msj):
    BOTLAR = []
    chat_id = msj.chat.id
    async for members in app.iter_chat_members(chat_id):
        botmu = members.user.is_bot
        #print(botmu)
        if botmu == True:
            BOTLAR.append(members.user.mention)
            botlarsiyahi = '\n'.join(BOTLAR)
        else:
            pass

    botlarsiyahi = '\n'.join(BOTLAR)
    await client.send_message(chat_id, botlarsiyahi)


