# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
from pyrogram import Client, filters, emoji, idle
from pyrogram.types import Message, Chat, InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions
import sys
import os
import time
import random
from AylinRobot import AylinRobot as app
from AylinRobot import LOGGER
from pyrogram.errors import FloodWait
from AylinRobot.config import Config



DUR = False
SORGU = None
WSORGU = None
WDUR = False

GRUP = []

MENTION = "[{}](tg://user?id={})"
MESSAGE = "Salam! {}, Əyləncə Dolu Qrupumuza Xoş Gəldin🥳!Qaydalara riaət etdikcə səndə favori userlərimizdən biri olacaqsan🤩!Əminəmki Nümunəvi Userlərdən biri olacaqsan!🥰"


def btag():
	BUTTON=[[InlineKeyboardButton(text="👨🏻‍💻Sahibim", url="https://t.me/sjrvan")]]
	BUTTON=[[InlineKeyboardButton(text="Yeniliklər Kanalı📣", url="https://t.me/seninkanal")]]
	return InlineKeyboardMarkup(BUTTON)


def bstart():
	BUTTON=[[InlineKeyboardButton(text="👨🏻‍💻Sahibim", url="https://t.me/sjrvan")]]
	BUTTON+=[[InlineKeyboardButton(text="Məni Qrupa Əlavə Et✅", url=f"https://t.me/seninbot?startgroup=true")]]
	return InlineKeyboardMarkup(BUTTON)

@app.on_message(filters.command(["admin", "all"]) & filters.private)
async def priw(client, message):
	await message.reply_text("Hmm burada 2miz olduğumuz üçün və 2 mizdə online olduğumuz üçün bu əmri qruplarda işlət!🤠")

@app.on_message(filters.command("all")
	& filters.group)
async def tag(client: app, message: Message):
	global DUR
	global SORGU
	msg = " ".join(message.command[1:])
	chat = message.chat
	async for mem in app.iter_chat_members(chat_id=chat.id, filter="administrators"):
		if message.from_user.id == mem.user.id:
			await message.reply_text(f"{message.from_user.mention} Tag Prosesini Başlatdı! Hərkəsi Tag Edirəm Boss!⚡️",
				reply_markup=btag()
				)
			time.sleep(1.5)
			SORGU = True
			async for member in app.iter_chat_members(chat_id=chat.id, filter="all"):
				if DUR:
					DUR=False
					SORGU = None
					break
				time.sleep(1.5)
				await app.send_message(chat_id=chat.id, text=f"{member.user.mention} {msg}")
				time.sleep(1.5)
		if message.from_user.id != mem.user.id:
			pass
		
@app.on_message(filters.command("admin")
	& filters.group)
async def ta(client: app, message: Message):
	global DUR
	global SORGU
	msg = " ".join(message.command[1:])
	chat = message.chat
	async for mem in app.iter_chat_members(chat_id=chat.id, filter="administrators"):
		if message.from_user.id == mem.user.id:
			await message.reply_text(f"{message.from_user.mention} Adminləri tag etməyimi istədi⚡️ Adminləri Tag Edirəm Boss!🥳",
				reply_markup=btag()
				)
			time.sleep(1)
			SORGU = True
			async for member in app.iter_chat_members(chat_id=chat.id, filter="administrators"):
				if DUR:
					DUR=False
					SORGU = None
					break
				time.sleep(1)
				await app.send_message(chat_id=chat.id, text=f"{member.user.mention} {msg}")
				time.sleep(1.5)
		if message.from_user.id != mem.user.id:
			pass


		
@app.on_message(filters.group
	& filters.command("cancel"))
async def stop(client: app, message: Message):
	global DUR
	chat = message.chat
	async for mem in app.iter_chat_members(chat_id=chat.id, filter="administrators"):
		if message.from_user.id == mem.user.id:
			if SORGU == None:
				await message.reply_text("Aktiv bir all prosesi yoxdur😕👍🏻")
				return

			DUR = True
			await message.reply_text(f"{message.from_user.mention} Tag prosesini dayandırdı❌ Tamam heçkəsi tag etmirəm😒")	
		if message.from_user.id != mem.user.id:
			pass
	
	
@app.on_message(filters.group & filters.new_chat_members)
def welcome(client, message):
	global WDUR
	global WSORGU
	WSORGU=True
	for i in message.new_chat_members:
		new_members = MENTION.format(i.first_name, i.id)
		text = MESSAGE.format(new_members)
		message.reply(text, disable_web_page_preview=True)	