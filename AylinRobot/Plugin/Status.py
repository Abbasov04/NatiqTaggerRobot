# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
from pyrogram import Client, filters, emoji, idle
from pyrogram.types import Message, Chat, InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions
import sys
import os
import time
import random
from time import time
from random import choice
from AylinRobot import AylinRobot as app
from AylinRobot import LOGGER
from pyrogram.errors import FloodWait
from AylinRobot.config import Config



DUR = False
SORGU = None

@app.on_message(filters.command(["admin", "tag"]) & filters.private)
async def priw(client, message):
	await message.reply_text("Hmm burada 2miz olduğumuz üçün və 2 mizdə online olduğumuz üçün bu əmri qruplarda işlət!🤠")
	
@app.on_message(filters.command("tag")
	& filters.group)
async def tag(client, message):
	global DUR
	global SORGU
	msg = " ".join(message.command[1:])
	chat = message.chat
	async for mem in client.iter_chat_members(chat_id=chat.id, filter="administrators"):
		if message.from_user.id == mem.user.id:
			await message.reply_text(f"{message.from_user.mention} Tag Prosesini Başlatdı! Hərkəsi Tag Edirəm Boss!⚡️",
				reply_markup=btag()
				)
			time.sleep(1)
			SORGU = True
			async for member in client.iter_chat_members(chat_id=chat.id, filter="tag"):
				if DUR:
					DUR=False
					SORGU = None
					break
				time.sleep(1)
				await client.send_message(chat_id=chat.id, text=f"{member.user.mention} {msg}")
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
	