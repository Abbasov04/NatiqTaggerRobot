# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import random
from random import choice
from pyrogram.types import Message
from helpers.filters import command, other_filters
from AylinRobot import AylinRobot as app
from pyrogram import filters
from pyrogram.errors import FloodWait
from AylinRobot.config import Config


@app.on_message(command(["ship"]) & filters.group & ~filters.edited)
async def my_handler(client, msj):
    chat_id = msj.chat.id

    BU_QRUP_USERLERI = []
    async for member in client.iter_chat_members(chat_id):
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