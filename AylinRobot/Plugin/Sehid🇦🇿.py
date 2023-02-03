# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import secrets, string, aiohttp
from AylinRobot import AylinRobot as app
from Sehid import random_line
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@app.on_message(filters.command(["sehid"]) & ~filters.edited)
async def commit(_, message):
    await message.reply_text((await random_line('Sehid/sehid.txt')), reply_markup=button)
    
button = reply_markup=InlineKeyboardMarkup(
[[InlineKeyboardButton("🇦🇿 Dəyiş", callback_data="back_data"),
InlineKeyboardButton("🔐 Bağla", callback_data="close")]]) 

      async def "close" in cb_data:
          await cmd.message.delete()
          await cmd.message.reply_to_message.delete()
    
@app.on_callback_query(filters.regex("deyis"))
async def deyis(_, query: CallbackQuery):
    await query.edit_message_text((await random_line('Sehid/sehid.txt')), reply_markup=button)