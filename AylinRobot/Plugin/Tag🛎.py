# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import random, time, os, sys
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters, emoji
from pyrogram.errors import FloodWait
from AylinRobot.config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery, ChatPermissions

DUR = False
SORGU = None
tagAktiv = False
MENTION = "[{}](tg://user?id={})"

def btag():
	BUTTON = [[InlineKeyboardButton(text="👨‍💻 Sahibim", url=f"https://t.me/{Config.OWNER_NAME}"),              InlineKeyboardButton("🎧 Playlist", url=f"https://t.me/{Config.PLAYLIST_NAME}"),],]	
	return InlineKeyboardMarkup(BUTTON)



### Səbəbsiz Tag Edər
@app.on_message(filters.command(["tag"]) & filters.group)
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
				await app.send_message(chat_id=chat.id, text=f"{member.user.mention} **Bayaqdan səni gözləyirəm gəl 🥰**")
				time.sleep(1)
		if message.from_user.id != mem.user.id:
			pass
		
		
### Sadəcə Adminləri Tağ Edər		
@app.on_message(filters.command(["admin"]) & filters.group)
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
@app.on_message(filters.command(["cancel"]) & filters.group)
async def stop(client: app, message: Message):
	global tagAktiv
	chat = message.chat
	async for mem in app.iter_chat_members(chat_id=chat.id, filter="administrators"):
		if message.from_user.id == mem.user.id:
			if SORGU == None:
				await message.reply_text("**Aktiv Bir Tag Prosesi Yoxdur 😕👍🏻**")
				return

			tagAktiv = True
			await message.reply_text(f"{message.from_user.mention} **Tag prosesini dayandırdı 😒**")	
		if message.from_user.id != mem.user.id:
			pass


@app.on_message(filters.command("ttg") & filters.group)
async def eTag(client, msj):
    # ayuyes @c9ala
    global tagAktiv
    chat_id = msj.chat.id
    mojiler = ["🛎", "🌌", "🎉", "😱", "😶‍", "🌫", "🥶"]
    reply = msj.reply_to_message
    userler = []
    await client.send_message(chat_id, f"[tag prosesi baslayir ayuye](https://t.me/)")
    time.sleep(2)
    members = app.iter_chat_members(chat_id)
    async for m in members:
        userler.append(m.user.id) # BOTLARI TAG ETMEYINI ISTEMIRSINIZSE, BURANI SILIN ASAGIDAKI KODDA DA # SILIN
        #if m.user.is_bot == True:
        #    pass
        #else:
        #    userler.append(str(m.user.id))
    try:
        tagMesaji = msj.text.split(" ", 1)[1]
        mesaj  = True
    except IndexError:
        mesaj = False
    usrsay = len(userler)
    s = 5 * round(usrsay / 5)
    t = s / 5
    ysay = t + 1
    ysay = int(ysay)
    if tagAktiv == False:
        for i in range(0, ysay):
            if mesaj == True:
                try:
                    await client.send_message(chat_id, f"[{random.choice(mojiler)}](tg://user?id={userler[0]}) [{random.choice(mojiler)}](tg://user?id={userler[1]}) [{random.choice(mojiler)}](tg://user?id={userler[2]}) [{random.choice(mojiler)}](tg://user?id={userler[3]}) [{random.choice(mojiler)}](tg://user?id={userler[4]})\n\n{tagMesaji}")
                    for i in range(0, 5):
                        userler.pop(0)
                    time.sleep(2)
                    tagAktiv = True
                except IndexError:
                    tagAktiv = False
                    await client.send_message(chat_id, f"bitdi ")
            else:
                try:
                    await client.send_message(chat_id, f"[{random.choice(mojiler)}](tg://user?id={userler[0]}) [{random.choice(mojiler)}](tg://user?id={userler[1]}) [{random.choice(mojiler)}](tg://user?id={userler[2]}) [{random.choice(mojiler)}](tg://user?id={userler[3]}) [{random.choice(mojiler)}](tg://user?id={userler[4]})")
                    for i in range(0, 5):
                        userler.pop(0)
                    time.sleep(2)
                    tagAktiv = True
                except IndexError:
                    tagAktiv = False
                    await client.send_message(chat_id, f"bitdi ")
    else:
        pass			