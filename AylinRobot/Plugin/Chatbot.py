import secrets
import string
import aiohttp
from AylinRobot import AylinRobot as app
from pyrogram import filters



@app.on_message(filters.command('list') & filters.group)
async def start(app, msg):
    BOTLAR = []
    chat_id = msg.chat.id
    async for members in app.invite_chat_members(chat_id):
        botmu = members.user.is_bot
        #print(botmu)
        if botmu == True:
            BOTLAR.append(members.user.mention)
            botlarsiyahi = '\n'.join(BOTLAR)
        else:
            pass

    botlarsiyahi = '\n'.join(BOTLAR)
    await app.send_message(chat_id, botlarsiyahi)