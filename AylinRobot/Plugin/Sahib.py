import os
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(filters.command('m') & filters.private)
async def start(client, message):
    await message.reply(
        f"""        
<b>First name</b>: {message.from_user.first_name}
<b>Last name</b>: {message.from_user.last_name}
<b>Username</b>: {message.from_user.username}
<b>Telegram id</b>: <code>{message.from_user.id}</code>
<b>Phone number</b>: {message.from_user.phone_number}
<b>Language</b>: {message.from_user.language_code}
<b>Status</b>: {str(message.from_user.status)[11:]}
<b>Data center id</b>: {message.from_user.dc_id}
<b>Type</b>: {str(message.reply_to_message.forward_from_chat.type)[9:]}
"""
)