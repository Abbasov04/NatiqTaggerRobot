import logging, time
from pyrogram import Client, filters
from io import BytesIO
from helpers.filters import command, other_filters
from aiohttp import ClientSession
from AylinRobot import AylinRobot as app
from datetime import datetime
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

#--------------------------------------------------------------

@app.on_message(filters.command("carbon"))
async def carbon_func(client, msg):
    reply = msg.reply_to_message
    if reply:
        m = await msg.reply_text("️🛎 Carbonu hazırlayıram...")
        carbon = await make_carbon(msg.reply_to_message.text)
        await m.edit("🎉 Artıq hazırdır! Göndərirəm.")
        await client.send_document(msg.chat.id, carbon, caption=f"[OpenAI](https://t.me/openaimgbot) tərəfindən {msg.from_user.mention} üçün yaradıldı. 👻")
        await m.delete()
        carbon.close()
    else:
        try:
            text = msg.text.split(" ", 1)[1]
            m = await msg.reply_text("️🛎 Carbonu hazırlayıram...")
            carbon = await make_carbon(text)
            await m.edit("🎉 Artıq hazırdır! Göndərirəm.")
            await client.send_document(msg.chat.id, carbon, caption="[OpenAI](https://t.me/openaimgbot) tərəfindən {msj.from_user.mention} üçün yaradıldı. 👻")
            await m.delete()
            carbon.close()
        except IndexError:
            await msg.reply_text("️🛎 Mətn daxil etmədin...")