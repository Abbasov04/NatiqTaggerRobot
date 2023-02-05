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
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery, ChatPermissions

DUR = False
SORGU = None
MENTION = "[{}](tg://user?id={})"

def btag():
	BUTTON = [[InlineKeyboardButton(text="👨‍💻 Sahibim", url=f"https://t.me/{Config.OWNER_NAME}"),              InlineKeyboardButton("🎧 Playlist", url=f"https://t.me/{Config.PLAYLIST_NAME}"),],]	
	return InlineKeyboardMarkup(BUTTON)


@app.on_message(
	filters.command(["admin", "tag"])
	& filters.private)
async def priw(client, message):
	await message.reply_text("🚫 Bu Əmri Qrupda İşlət")


### Tək-Tək Tağ Edər

@app.on_message(filters.command("tag") & filters.group)
async def tag(client: app, message: Message):
	global DUR
	global SORGU
	msg = " ".join(message.command[1:])
	chat = message.chat
	async for mem in app.iter_chat_members(chat_id=chat.id, filter="administrators"):
		if message.from_user.id == mem.user.id:
			await message.reply_text(f"{message.from_user.mention}\n**Tag Prosesini Başlatdı 🥰**\n**Tagı Dayandırmaq Üçün**\n/cancel Yazın 🙎‍♀️**",
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
				await app.send_message(chat_id=chat.id, text=f"{member.user.mention} {msg} **Bayaqdan səni gözləyirəm gəl 🥰**")
				time.sleep(1)
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
			await message.reply_text(f"{message.from_user.mention}\n**Adminləri Tag Etməyimi İstədi 🤓**\n**Tagı Dayandırmaq Üçün**\n/cancel Yazın**",
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
				time.sleep(1)
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
				await message.reply_text("**Hmmm Aktiv Bir Tag Prosesi Yoxdur 😕👍🏻**")
				return

			DUR = True
			await message.reply_text(f"{message.from_user.mention} **Tag prosesini dayandırdı 😒 Artığ Tağ Etmərəm 🥹**")	
		if message.from_user.id != mem.user.id:
			pass