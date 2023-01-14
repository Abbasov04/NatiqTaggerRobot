from MusicAzBot import MusicAzBot as app
from pyrogram import Client, filters
from MusicAzBot.config import Config
import os, youtube_dl, requests, aiohttp, wget, time, yt_dlp, lyricsgenius
from youtube_search import YoutubeSearch
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message, User
from yt_dlp import YoutubeDL
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message, CallbackQuery
)


@app.on_message(filters.command("lyrics") & ~filters.edited)
async def lrsearch(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("**İstifadə:**\n\n/lyrics [ Musiqi Adı]")
    m = await message.reply_text("Mahnı sözləri axtarılır")
    query = message.text.split(None, 1)[1]
    x = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    y = lyricsgenius.Genius(x)
    y.verbose = False
    S = y.search_song(query, get_full_info=False)
    if S is None:
        return await m.edit("Lyrics not found :p")
    xxx = f"""
** Yüklədi {Config.BOT_USERNAME} 🇦🇿**

**Axtarılan Mahnı:-** __{query}__
 **Found Lyrics For:-** __{S.title}__
 **Rəssam:-** {S.artist}

 **__ Mahnı sözləri:__**

{S.lyrics}"""
    if len(xxx) > 4096:
        await m.delete()
        filename = "lyrics.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(xxx.strip()))
        await message.reply_document(
            document=filename,
            caption=f"**Sözlər çox olduğundan fayl edib atdım...:**\n\n`Lyrics`",
            quote=False,
        )
        os.remove(filename)
    else:
        await m.edit(xxx)
