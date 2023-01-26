import secrets
import string
import aiohttp
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters
from pyrogram import filters
from Sehid import random_line
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.filters import command


@app.on_callback_query(filters.regex("sehidler"))
async def commit(_, message):
    await message.reply_text((await random_line('Sehid/sehid.txt')))
    
    
    
    
@app.on_message(command("sehid") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>✨ Welcome {message.from_user.mention()}!</ballows you to play music on groups through the new Telegram's voice chats!**

💡 Find out all the **Bot's commands** and how they work by clicking on the **» ⚙️ Commands** button!""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ Add me to your group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "⚙️ Command​​", callback_data="sehidler"
                    ),
     disable_web_page_preview=True
    )    