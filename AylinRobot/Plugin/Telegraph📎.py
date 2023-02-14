# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os, pyrogram
from telegraph import upload_file
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from AylinRobot.config import Config

    
@app.on_message(filters.command('tgm'))
async def tgm(client, message):
    try:
        text = await message.reply("💁‍♀️ Emal edilir...")
        async def progress(current, total):
            await text.edit_text(f"“Bir dəqiqə, səbirli ol, gecikmişəm ✌... {current * 100 / total:.1f}%")
        try:
            location = f"./media/group/"
            local_path = await message.reply_to_message.download(location, progress=progress)
            await text.edit_text("📤 Telegraph Lingi Göndərilir...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🌐 | Budur Sizin Telegraph Linginiz**:\n\n<code>https://telegra.ph{upload_path[0]}</code>Ling\n\n{Config.BOT_USERNAME}")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ |  Fayl yükləmə uğursuz oldu**\n\n<i>**Səbəb**: {e}</i>")
            os.remove(local_path) 
            return         
    except Exception:
        pass    