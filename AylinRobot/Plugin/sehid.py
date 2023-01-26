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



soz = open("Sehid/sehid.txt, "r"
yazilar = test.readlines()
rndyazi = random.choice(yazilar)

@app.on_message(filters.command('sehid'))
async def start(client, msj):
    global soz
    chat_id = msj.chat.id
    soz = random.choice(soz)
    await client.send_message(chat_id,
                              soz,
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
    soz2 = random.choice(sozler)
    if soz2 == soz:
        soz2 = random.choice(sozler)
        if soz2 == soz:
            pass
        elif soz2 != soz:
            await msj.message.edit_text(text=soz2, reply_markup=msj.message.reply_markup)
    elif soz2 != soz:
        await msj.message.edit_text(text=soz2, reply_markup=msj.message.reply_markup)