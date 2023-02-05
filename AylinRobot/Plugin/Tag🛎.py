# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
import sys
import os
import time
import random
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters, emoji, idle
from AylinRobot import LOGGER
from pyrogram.errors import FloodWait
from AylinRobot.config import Config
from pyrogram.types import Message, Chat, InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

DUR = False
SORGU = None

MENTION = "[{}](tg://user?id={})"

def btag():
	BUTTON=[[InlineKeyboardButton(text="📝 Sahibim ", url=f"{Config.OWNER_NAME}"),
  InlineKeyboardButton(text="🎧 Playlist", url=f"{Config.PLAYLIST_NAME}")),],]
	return InlineKeyboardMarkup(BUTTON)


@app.on_message(filters.command(["admin", "tag"]) & filters.private)
async def priw(client, message):
	await message.reply_text("Hmm burada 2miz olduğumuz üçün və 2 mizdə online olduğumuz üçün bu əmri qruplarda işlət!🤠")


### Tək-Tək Tağ Edər

@app.on_message(filters.command("tag")
	& filters.group)
async def tektag(client: app, message: Message):
	global DUR
	global SORGU
	msg = " ".join(message.command[1:])
	chat = message.chat
	async for mem in app.iter_chat_members(chat_id=chat.id, filter="administrators"):
		if message.from_user.id == mem.user.id:
			await message.reply_text(f"{message.from_user.mention} Tag Prosesini Başlatdı! Hərkəsi Tag Edirəm Boss!⚡️",
				reply_markup=btag()
				)
			time.sleep(1)
			SORGU = True
			async for member in app.iter_chat_members(chat_id=chat.id, filter="all"):
				if DUR:
					DUR=False
					SORGU = None
					break
				time.sleep(1)
				await app.send_message(chat_id=chat.id, text=f"{member.user.mention} {msg}")
				time.sleep(1.5)
		if message.from_user.id != mem.user.id:
			pass
		
		
### Sadəcə Adminləri Tağ Edər		
		
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



### Tag Prosesin Dayandırar

@app.on_message(filters.group
	& filters.command("cancel"))
async def stop(client: app, message: Message):
	global DUR
	chat = message.chat
	async for mem in app.iter_chat_members(chat_id=chat.id, filter="administrators"):
		if message.from_user.id == mem.user.id:
			if SORGU == None:
				await message.reply_text("Aktiv Bir Tag Prosesi Yoxdur😕👍🏻")
				return

			DUR = True
			await message.reply_text(f"{message.from_user.mention} Tag prosesini dayandırdı❌ Tamam heçkəsi tag etmirəm😒")	
		if message.from_user.id != mem.user.id:
			pass