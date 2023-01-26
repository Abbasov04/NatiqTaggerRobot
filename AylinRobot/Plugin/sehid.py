import secrets
import string
import aiohttp
from AylinRobot import AylinRobot as app
import pyrogram
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import filters
from Sehid import random_line



sehid = open("Sehid/sehid.txt")
yazilar = sehid.readlines()
rndyazi = random.choice(yazilar)

@app.on_message(filters.command('sehid'))
async def start(client, msj):
    global soz
    chat_id = msj.chat.id
    sehid = random.choice(sehid)
    await client.send_message(chat_id,
                              sehid,
                              reply_markup=InlineKeyboardMarkup(
                                  [
                                      [
                                          InlineKeyboardButton(
                                              "Deyisdir",
                                              callback_data="deyisdir"
                                          )
                                      ]
                                  ]
                              )
                              )

@app.on_callback_query(filters.regex(r"^deyisdir$"))
async def callback(cl, msj: CallbackQuery):
    sehid2 = random.choice(sehid)
    if sehid2 == sehid:
        sehid2 = random.choice(sehid)
        if sehid2 == sehid:
            pass
        elif sehid2 != sehid:
            await msj.message.edit_text(text=sehid2, reply_markup=msj.message.reply_markup)
    elif sehid2 != sehid:
        await msj.message.edit_text(text=sehid2, reply_markup=msj.message.reply_markup)