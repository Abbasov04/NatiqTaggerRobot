import secrets
import string
import aiohttp
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters
from pyrogram import filters
from Sehid import random_line
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.filters import command


@app.on_callback_query(filters.regex("sehid"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text((await random_line('Sehid/sehid.txt')))
    
    
    
    
@app.on_message(command("sehid") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text((await random_line('Sehid/sehid.txt')))
    
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                  InlineKeyboardButton("⚙️ Command​​", callback_data="sehid"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )