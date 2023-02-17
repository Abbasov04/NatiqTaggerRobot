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
			reply_markup=d_or_c(user.id)
		)
    
def d_or_c(user_id):
	BUTTON = [[InlineKeyboardButton(text="Sehid", callback_data = " ".join(["d_data",str(user_id)]))]]
	BUTTON += [[InlineKeyboardButton(text="Sehid", callback_data = " ".join(["c_data",str(user_id)]))]]
	return InlineKeyboardMarkup(BUTTON)


@app.on_callback_query(filters.regex("deyis"))
async def deyis(_, query: CallbackQuery):
    await query.edit_message_text(text="{} Əmri İcra Etdi!".format(user.mention, await random_line('Sehid/sehid.txt')), reply_markup=button)