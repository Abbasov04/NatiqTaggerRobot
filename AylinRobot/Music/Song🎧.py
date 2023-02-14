# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

from AylinRobot import AylinRobot as app
from __future__ import unicode_literals
from io import BytesIO
from random import randint
from urllib.parse import urlparse
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import os, youtube_dl, requests, aiohttp, wget, time, yt_dlp
from youtube_search import YoutubeSearch
from pyrogram.handlers import MessageHandler
from AylinRobot.config import Config
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)



def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


buttons = {
  "markup_for_private": InlineKeyboardMarkup([[InlineKeyboardButton('Playlist 🎧', url=f'https://t.me/{Config.PLAYLIST_NAME}')]]),
  "add_to_group": InlineKeyboardMarkup([[InlineKeyboardButton('️✨️ Qrupa əlavə et ️✨️', url=f'https://t.me/{Config.BOT_USERNAME}?startgroup=true')]]),
}


@app.on_message(filters.command(["song", f"song@{Config.BOT_USERNAME}"])
def song(client, message):

    message.delete()
    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    chutiya = "["+user_name+"](tg://user?id="+str(user_id)+")"
    
    isteyen = message.from_user.first_name 
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply(f"🔎 **Axtarılır...{query}**")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:100]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{Config.BOT_USERNAME}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)


        performer = f"Unknown Artist"  
        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]
        channel = results[0]["channel"]   

    except Exception as e:
        m.edit("İstədiyiniz musiqi tapılmadı 😔")
        print(str(e))
        return
    m.edit(f"🎵**{title}**")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
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
        m.edit("📤 Yüklənir..")
        message.reply_audio(audio_file, caption=caption_for_private, quote=False, title=title, duration=dur, thumb=thumb_name, performer = f"{Config.PLAYLIST_NAME}", reply_markup=buttons['markup_for_private'])
        m.delete()
        app.send_audio(chat_id=Config.PLAYLIST_ID, audio=audio_file, caption=caption_for_logchannel, performer = f"{Config.BOT_USERNAME}", title=title, duration=dur, thumb=thumb_name, reply_markup=buttons['add_to_group'])
    except Exception as e:
        m.edit(f'**⚠️ Gözlənilməyən xəta yarandı.**\n**Xahiş edirəm xətanı {Config.OWNER_NAME} sahibimə xəbərdar et!**')
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)



def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " not in text_to_return:
        return None
    try:
        return message.text.split(None, 1)[1]
    except IndexError:
        return None


def humanbytes(size):
    if not size:
        return ""
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


async def progress(current, total, message, start, type_of_ps, file_name=None):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        if elapsed_time == 0:
            return
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            "".join("🔴" for i in range(math.floor(percentage / 10))),
            "".join("🔘" for i in range(10 - math.floor(percentage / 10))),
            round(percentage, 2),
        )

        tmp = progress_str + "{0} of {1}\nETA: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            try:
                await message.edit(
                    "{}\n**File Name:** `{}`\n{}".format(type_of_ps, file_name, tmp)
                )
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass
        else:
            try:
                await message.edit("{}\n{}".format(type_of_ps, tmp))
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass


def get_user(message: Message, text: str) -> [int, str, None]:
    asplit = None if text is None else text.split(" ", 1)
    user_s = None
    reason_ = None
    if message.reply_to_message:
        user_s = message.reply_to_message.from_user.id
        reason_ = text or None
    elif asplit is None:
        return None, None
    elif len(asplit[0]) > 0:
        user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        if len(asplit) == 2:
            reason_ = asplit[1]
    return user_s, reason_


def get_readable_time(seconds: int) -> int:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["d", "m", "j", "hari"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time


def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + " day(s), ") if days else "")
        + ((str(hours) + " hour(s), ") if hours else "")
        + ((str(minutes) + " minute(s), ") if minutes else "")
        + ((str(seconds) + " second(s), ") if seconds else "")
        + ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    )
    return tmp[:-2]


ydl_opts = {
    "format": "bestaudio/best",
    "writethumbnail": True,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}


def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]


# Funtion To Download Song
async def download_song(url):
    song_name = f"{randint(6969, 6999)}.mp3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(song_name, mode="wb")
                await f.write(await resp.read())
                await f.close()
    return song_name


is_downloading = False


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))

