from FidanRobot import FidanRobot as app
from pyrogram.errors.exceptions import ChatAdminRequired
from pyrogram.types import Photo, Video, Animation, Audio
from helpers.filters import command


CHANNEL_ID = -1001872847436

BOT_OWNER = 1347601562

BOT_OWNER = 5637445914

@app.on_message(command("log"))
async def log(client, message):
    try:
        if not message.reply_to_message:
            await message.reply_text("Log üçün bir mesaja yanıt verməlisiniz.")
            return
        if message.from_user.id != BOT_OWNER:
            await message.reply_text("Bu əmr yalnızca bot sahibi tərəfindən işlədilə bilər.")
            return
        reply_message = message.reply_to_message
        if reply_message.photo:
            photo: Photo = reply_message.photo[-1]
            caption = f"Gönderen: {message.from_user.mention}\n{reply_message.caption or ''}"
            await app.send_photo(chat_id=CHANNEL_ID, photo=photo.file_id, caption=caption)
            await app.send_photo(chat_id=BOT_OWNER, photo=photo.file_id, caption=caption)
            await message.reply_text("Fotoğraf log kanalına ve bot sahibine gönderildi.")
        elif reply_message.video:
            video: Video = reply_message.video
            caption = f"Gönderen: {message.from_user.mention}\n{reply_message.caption or ''}"
            await app.send_video(chat_id=CHANNEL_ID, video=video.file_id, caption=caption)
            await app.send_video(chat_id=BOT_OWNER, video=video.file_id, caption=caption)
            await message.reply_text("Video log kanalına ve bot sahibine gönderildi.")
        elif reply_message.animation:
            animation: Animation = reply_message.animation
            caption = f"Gönderen: {message.from_user.mention}\n{reply_message.caption or ''}"
            await app.send_animation(chat_id=CHANNEL_ID, animation=animation.file_id, caption=caption)
            await app.send_animation(chat_id=BOT_OWNER, animation=animation.file_id, caption=caption)
            await message.reply_text("Animasiya log kanalına ve bot sahibine gönderildi.")
        elif reply_message.audio:
            audio: Audio = reply_message.audio
            caption = f"Gönderen: {message.from_user.mention}\n{reply_message.caption or ''}"
            await app.send_audio(chat_id=CHANNEL_ID, audio=audio.file_id, caption=caption)
            await app.send_audio(chat_id=BOT_OWNER, audio=audio.file_id, caption=caption)
            await message.reply_text("Audio log kanalına ve bot sahibine gönderildi.")
        elif reply_message.text:
            text = reply_message.text
            await app.send_message(chat_id=CHANNEL_ID, text=f"Gönderen: {message.from_user.mention}\n{text}")
            await app.send_message(chat_id=BOT_OWNER, text=f"Gönderen: {message.from_user.mention}\n{text}")
            await message.reply_text("Metin log kanalına ve bot sahibine gönderildi.")
        else:
            await message.reply_text("Yalnızca fotoğraf, video, animasiya, audio və ya mətn yanıtlayabilirsiniz.")
    except ChatAdminRequired:
        await message.reply_text("Hata: Botun log göndərə bilmək üçün qrupda admin olması lazımdır.")
