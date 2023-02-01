# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os
from telegraph import upload_file
import pyrogram
from AylinRobot import AylinRobot as app
from helpers.filters import command
from AylinRobot import LOGGER
from pyrogram import idle, filters
from pyrogram import filters, Client
from AylinRobot.config import Config
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,InlineKeyboardMarkup, InlineKeyboardButton,CallbackQuery, InlineQuery)


@app.on_message(filters.command(["tgm"]))
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply("Dəstəklənən media faylına cavab verin")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("Dəstəklənmir!!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(f"**Budur Sizin Teleqraf Linkiniz :\n\nhttps://telegra.ph{response[0]}**", disable_web_page_preview=False)
    finally:
        os.remove(download_location)
    