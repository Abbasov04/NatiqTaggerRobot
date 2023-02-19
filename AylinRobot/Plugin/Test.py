import os
from pyrogram import idle, filters
import requests
import wget
from AylinRobot import AylinRobot as app
from yt_dlp import YoutubeDL
from pyrogram import Client, filters
import yt_dlp
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



@app.on_message(filters.command(["music"]))
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
        audio_file,
        thumb=preview,
        duration=int(info_dict["duration"]),
        caption_for_logchannel = f'''
**╭───────────────**
**├▷ 🎧 Başlıq: [{title}]({link})**
**├───────────────**
**├▷ 👁‍🗨 Baxış: {views}**
**├───────────────**
**├▷ 👤 İstəyən: {isteyen}**
**├───────────────**
**├▷ 🌀 Bot: @{Config.BOT_USERNAME}**
**╰───────────────**
'''
        caption_for_private = f'''
**╭───────────────**
**├▷ 🎧 Başlıq: [{title}]({link})**
**├───────────────**
**├▷ 👁‍🗨 Baxış: {views}**
**├───────────────**
**├▷ 🌀 Bot: @{Config.BOT_USERNAME}**
**╰───────────────**
'''

        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
    await cb.edit("📤 Yüklənir..")
        message.reply_audio(audio_file, caption=caption_for_private, quote=False, title=title, duration=dur, thumb=thumb_name, performer = f"{Config.PLAYLIST_NAME}", reply_markup=buttons['markup_for_private'])
    await cb.delete()
    await cb.send_audio(chat_id=Config.PLAYLIST_ID, audio=audio_file, caption=caption_for_logchannel, performer = f"{Config.BOT_USERNAME}", title=title, duration=dur, thumb=thumb_name, reply_markup=buttons['add_to_group'])
    except Exception as e:
        m.edit(f'**⚠️ Gözlənilməyən xəta yarandı.**\n**Xahiş edirəm xətanı {Config.OWNER_NAME} sahibimə xəbərdar et!**')
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)