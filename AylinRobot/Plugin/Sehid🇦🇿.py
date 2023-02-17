# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import secrets, string, aiohttp
from AylinRobot import AylinRobot as app
from Sehid import random_line
from pyrogram.errors import FloodWait
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@app.on_message(filters.command("sehid"))
async def _(client, message):
	user = message.from_user
	await message.reply_text(text="{} Əmri İcra Etdi!".format(user.mention, 
  await random_line('Sehid/sehid.txt')),
			reply_markup=(BUTTON)
		)	
    
BUTTON = reply_markup=InlineKeyboardMarkup(
[[InlineKeyboardButton("🇦🇿 Şəhid", callback_data="sehid"),
InlineKeyboardButton("🔐 Bağla", callback_data="close")]])


@app.on_callback_query(filters.regex("sehid"))
async def deyis(_, query: CallbackQuery):
    await sleep(5) 
    await query.edit_message_text((await random_line('Sehid/sehid.txt')),
    reply_markup=(BUTTON))    