from AylinRobot import AylinRobot as app
from pyrogram import Client, emoji, filters

TARGET = -1001845751616
# Welcome message template
MESSAGE = "Salam {} {} Grupuna Xoş Gəldin"

@app.on_message(filters.chat(TARGET) & filters.new_chat_members)
async def welcome(client, message):
    new_members = [u.mention for u in message.new_chat_members]
    text = MESSAGE.format(emoji.SPARKLES, ", ".join(new_members))
    await message.reply_text(text, disable_web_page_preview=True)