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
	BUTTON += [[InlineKeyboardButton(text="🔐 Bağla", callback_data = " ".join(["close",str(user_id)]))]]
	return InlineKeyboardMarkup(BUTTON)


@app.on_callback_query()
async def _(client, callback_query):
	sehid=random.choice(sehid)
	user = callback_query.from_user
	c_q_d, user_id = callback_query.data.split()
	if str(user.id) == str(user_id):
		if c_q_d == "sehid":	
async def deyis(_, query: CallbackQuery):
    await query.edit_message_text(text="{} Əmri İcra Etdi!".format(user.mention, await random_line('Sehid/sehid.txt')), 
    reply_markup=d_or_c(user.id)
		)