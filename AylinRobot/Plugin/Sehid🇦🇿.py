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
	await message.reply_text(text="{} Əmri İcra Etdi!".format(user.mention, await random_line('Sehid/sehid.txt')), 
			reply_markup=sehid(user.id)
		)
    
def sehid(user_id):
	BUTTON = [[InlineKeyboardButton(text="🇦🇿 Səhid", callback_data = " ".join(["deyis",str(user_id)]))]]
	BUTTON += [[InlineKeyboardButton("🔐 Bağla", callback_data="close"),]])
	return InlineKeyboardMarkup(BUTTON)


@app.on_callback_query(filters.regex("deyis"))
async def deyis(_, query: CallbackQuery):
    await query.edit_message_text(text="{} Əmri İcra Etdi!".format(user.mention, await random_line('Sehid/sehid.txt')), 
    reply_markup=sehid(user.id)
		)