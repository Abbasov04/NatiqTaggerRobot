from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from pyrogram import idle, filters
from pyrogram import Client, filters



    
@app.on_message(filters.command('list') & filters.group)
def list(client, msj):
    BOTLAR = []
    chat_id = msj.chat.id
    async for members in client.get_chat_members(chat_id):
        botmu = members.user.is_bot
        if botmu == True:
            BOTLAR.append(members.user.mention)
            botlarsiyahi = '\n'.join(BOTLAR)
        else:
            pass
    botlarsiyahi = '\n'.join(BOTLAR)
    await client.send_message(chat_id, botlarsiyahi)