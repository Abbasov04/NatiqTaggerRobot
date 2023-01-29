import os
import time
import psutil
import shutil
import string
import asyncio
from random import choice
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from pyrogram import idle, filters
from pyrogram import Client, filters
from helpers.merrors import capture_err

@app.on_message(filters.command("ship"))
async def my_handler(client, msj):
@capture_err  
    chat_id = msj.chat.id
    chat_members = app.get_chat_members(chat_id)
    BU_QRUP_USERLERI = []
    for member in chat_members:
        if member.user.is_bot == True:
            pass
        elif member.user.is_bot == False:
            BU_QRUP_USERLERI.append((member.user.mention))

    rnduser = random.choice(BU_QRUP_USERLERI)
    sevgi2 = random.choice(BU_QRUP_USERLERI)

    if rnduser == sevgi2:
        rnduser = random.choice(BU_QRUP_USERLERI)
        # sevgi2 = random.choice(BU_QRUP_USERLERI)
        if rnduser == sevgi2:
            rnduser = random.choice(BU_QRUP_USERLERI)
            # sevgi2 = random.choice(BU_QRUP_USERLERI)
            if rnduser == sevgi2:
                rnduser = random.choice(BU_QRUP_USERLERI)
                if rnduser == sevgi2:
                    await client.send_message(chat_id, f"{msj.from_user.mention} yeniden cehd edin")
                elif rnduser != sevgi2:
                    await client.send_message(chat_id,
                                              f"Leyli ve Mecnun\n\n{rnduser} + {sevgi2} = {random.randint(0, 100)}%❤️")
            elif rnduser != sevgi2:
                await client.send_message(chat_id,
                                          f"Leyli ve Mecnun\n\n{rnduser} + {sevgi2} = {random.randint(0, 100)}%❤️")
        elif rnduser != sevgi2:
            await client.send_message(chat_id, f"Leyli ve Mecnun\n\n{rnduser} + {sevgi2} = {random.randint(0, 100)}%❤️")
    elif rnduser != sevgi2:
        await client.send_message(chat_id, f"Leyli ve Mecnun\n\n{rnduser} + {sevgi2} = {random.randint(0, 100)}%❤️")