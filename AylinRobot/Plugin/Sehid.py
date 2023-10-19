import secrets, string, aiohttp
from AylinRobot import AylinRobot as app
from Sehid import random_line
from pyrogram.errors import FloodWait
from pyrogram import Client, filters
import os
import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


button = InlineKeyboardMarkup([
    [InlineKeyboardButton("🔄Dəyiş", callback_data="deyis")]
])

@app.on_message(filters.command("sehid") & ~filters.edited)
async def commit(_, message):
    await message.reply_text((await random_line('Sehid/sehid.txt')), reply_markup=button)



@app.on_callback_query(filters.regex("deyis"))
async def deyis(_, query: CallbackQuery):
    await query.edit_message_text((await random_line('Sehid/sehid.txt')), reply_markup=button)