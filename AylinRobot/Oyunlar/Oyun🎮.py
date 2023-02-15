import os
import logging
import random
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters
from pyrogram.errors import FloodWait


DART_E_MOJI = "🎯"
BOWLING = "🎳"
TRY_YOUR_LUCK = "🎰"
GOAL_E_MOJI = "⚽"
BASKETBALL = "🏀"
DICE = "🎲"


@app.on_message(filters.command(["ox"]))
async def ox(client, message):
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DART_E_MOJI,
        disable_notification=True
    )


@app.on_message(filters.command(["bowling"]))
async def bowling(client, message):
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=BOWLING,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )


@app.on_message(filters.command(["jackpot"]))
async def jackpot(client, message):
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=TRY_YOUR_LUCK,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )


@app.on_message(filters.command(["top"]))
async def top(client, message):
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=GOAL_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )


@app.on_message(filters.command(["basket"]))
async def basket(client, message):
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=BASKETBALL,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

@app.on_message(filters.command(["zer"]))
async def basket(client, message):
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DICE,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )
        