from io import BytesIO
from traceback import format_exc
from AylinRobot import AylinRobot as app
from AylinRobot import LOGGER
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message
from Python_ARQ import ARQ
from helpers.merrors import capture_err
import aiohttp
from pyrogram import Client, filters


@app.on_message(filters.command(["git"]))
@capture_err
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("🙄__Give me a valid github username__")
        return
    username = message.text.split(None, 1)[1]
    URL = f"https://api.github.com/{username}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()
            try:
                url = result["html_url"]
                name = result["name"]
                company = result["company"]
                bio = result["bio"]
                created_at = result["created_at"]
                avatar_url = result["avatar_url"]
                blog = result["blog"]
                location = result["location"]
                repositories = result["public_repos"]
                followers = result["followers"]
                following = result["following"]
                caption = f"""**Info Of {name}**
**🧸Username:** `{username}`
**💌Bio:** `{bio}`
**🔗Profile Link:** [Here]({url})
**⛱Company:** `{company}`
**🗓Created On:** `{created_at}`
**🧰Repositories:** `{repositories}`
**🎓Blog:** `{blog}`
**📍Location:** `{location}`
**💡Followers:** `{followers}`
**📡Following:** `{following}`"""
            except Exception as e:
                print(str(e))
    await message.reply_photo(photo=avatar_url, caption=caption)

