import os
from pyrogram import idle, filters
import requests
import wget
from AylinRobot import AylinRobot as app
from AylinRobot.config import Config
from pyrogram import filters, Client
from pyrogram.types import *
from pyrogram.types import Message
from pyrogram import *
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
import asyncio
import math
import io
import re
import time
import aiofiles
import aiohttp
import wget
import os
from asyncio import get_running_loop
from functools import partial
from io import BytesIO
from urllib.parse import urlparse
import ffmpeg
import lyricsgenius
from youtubesearchpython import VideosSearch



@app.on_message(filters.command(["song", "search", "music"]))
async def ytsearch(client, message):
    try:
        if len(message.command) < 2:
            await message.reply("Give me some title")
            return
        user_id = message.from_user.id
        query = " ".join(message.command[1:])
        msg = await message.reply("**Searching...**")
        results = YoutubeSearch(query, max_results=5).to_dict()
        try:
            toxxt = "**❣𝚂𝚎𝚕𝚎𝚌𝚝 𝚃𝚑𝚎 𝚜𝚘𝚗𝚐 𝚈𝚘𝚞 𝚠𝚊𝚗𝚝 𝚃𝚘 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍❣**\n\n"
            emojilist = ["❰❶❱", "❰❷❱", "❰❸❱", "❰❹❱", "❰❺❱"]
            for j in range(5):
                toxxt += f"{emojilist[j]} <b>ᴛɪᴛʟᴇ - [{results[j]['title']}](https://youtube.com{results[j]['url_suffix']})</b>\n"
                toxxt += f" 🕒 ╚ <b>ᴅᴜʀᴀᴛɪᴏɴ</b> - {results[j]['duration']}\n"
                toxxt += f" 👻 ╚ <b>ᴠɪᴇᴡꜱ</b> - {results[j]['views']}\n"
                toxxt += f" 📛 ╚ <b>ᴄʜᴀɴɴᴇʟ</b> - {results[j]['channel']}\n\n"

            koyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "❰ ❶ ❱", callback_data=f"plll 0|{query}|{user_id}"
                        ),
                        InlineKeyboardButton(
                            "❰ ❷ ❱", callback_data=f"plll 1|{query}|{user_id}"
                        ),
                        InlineKeyboardButton(
                            "❰ ❸ ❱", callback_data=f"plll 2|{query}|{user_id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "❰ ❹ ❱", callback_data=f"plll 3|{query}|{user_id}"
                        ),
                        InlineKeyboardButton(
                            "❰ ❺ ❱", callback_data=f"plll 4|{query}|{user_id}"
                        ),
                    ],
                    [InlineKeyboardButton(text="Close", callback_data="close")],
                ]
            )
            await msg.edit(toxxt, reply_markup=koyboard, disable_web_page_preview=True)
        except Exception as e:
            await msg.edit(e)
    except Exception as e:
        await message.reply(e)


@app.on_callback_query(filters.regex(pattern=r"plll"))
async def youtube_cb(b, cb):
    cbd = cb.data.strip()
    typed_ = cbd.split(None, 1)[1]
    try:
        x, query, useer_id = typed_.split("|")
    except:
        await cb.message.edit("Song Not Found")
        return
    useer_id = int(useer_id)
    if cb.from_user.id != useer_id:
        await cb.answer(
            "You ain't the person who requested to play the song!", show_alert=True
        )
        return
    await cb.message.edit("▱▱▱▱▱▱")
    await cb.message.edit("▰▱▱▱▱▱")
    await cb.message.edit("▰▰▱▱▱▱")
    await cb.message.edit("▰▰▰▱▱▱")
    await cb.message.edit("▰▰▰▰▱▱")
    await cb.message.edit("▰▰▰▰▰▱")
    await cb.message.edit("▰▰▰▰▰▰")

    x = int(x)
    results = YoutubeSearch(query, max_results=5).to_dict()
    resultss = results[x]["url_suffix"]
    title = results[x]["title"][:40]
    thumbnail = results[x]["thumbnails"][0]
    url = f"https://youtube.com{resultss}"
    performer = f"Unknown Artist"  
    duration = results[0]["duration"]
    url_suffix = results[0]["url_suffix"]
    views = results[0]["views"]
    channel = results[0]["channel"]
    link = f"https://youtube.com{results[0]['url_suffix']}"
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        preview = wget.download(thumbnail)
    except BaseException:
        pass
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        audio_file = ydl.prepare_filename(info_dict)
        ydl.process_info(info_dict)
    await cb.message.edit("🅂🄴🄽🄳🄸🄽🄶")
    await cb.message.reply_audio(
        audio_file,
        thumb=preview,
        duration=int(info_dict["duration"]),
        caption=(f"""
 ━━━━━━━━━━━━━━━━━━━━━━━━━━┑
💽 𝙽𝚊𝚖𝚎 : __[{title}]({link})__

♪ 𝙰𝚛𝚝𝚒𝚜𝚝 : **{channel}**

⏳ 𝙳𝚞𝚛𝚊𝚝𝚒𝚘𝚗 : {duration}

💠 V𝚒𝚎𝚠𝚜 : --{views}--

┕━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
    )
    try:
        os.remove(audio_file)
        os.remove(preview)
        await cb.message.delete()
    except BaseException:
        pass


@app.on_callback_query(filters.regex(pattern=r"close"))
async def close(b, cb):
    await cb.answer("Closed!")
    await cb.message.delete()


