# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os, pyrogram
from telegraph import upload_file
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from AylinRobot.config import Config


@app.on_message(filters.command("tgm"))
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
        await message.reply(message=document)
    else:
        await message.reply(f"**Budur Sizin Teleqraf Linkiniz :\n\nhttps://telegra.ph{response[0]}**", disable_web_page_preview=False)
    finally:
        os.remove(download_location)
    
    
@app.on_message(filters.command('tl'))
async def get_link_group(client, message):
    try:
        text = await message.reply("Processing...")
        async def progress(current, total):
            await text.edit_text(f"Ruko zara sabar karo bana raha hu thodi der mai ✌... {current * 100 / total:.1f}%")
        try:
            location = f"./media/group/"
            local_path = await message.reply_to_message.download(location, progress=progress)
            await text.edit_text("📤 Ab ek mantra bol - Om swaha boom chik chik phat...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🌐 | Telegraph Link**:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ | File upload failed**\n\n<i>**Reason**: {e}</i>")
            os.remove(local_path) 
            return         
    except Exception:
        pass    