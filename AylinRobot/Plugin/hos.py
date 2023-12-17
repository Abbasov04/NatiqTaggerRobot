from pyrogram import Client, filters
from pyrogram.types import Message
from AylinRobot import AylinRobot as app

owner_idim = 6603298819

# Client oluşturma

# Bot sahibinin gruba katılması durumunda mesaj gönderen fonksiyon
@app.on_message(filters.new_chat_members)
def on_new_chat_members(client, message: Message):
    for user in message.new_chat_members:
        if user.id == owner_idim:
            # Bot sahibi gruba katıldığında mesaj gönder
            reply_message = message.reply("Salam Sahibim Xoş Gəldin Qrupa 🤖💙")
            # Emoji ve GIF eklemek için yanıt mesajına düzenleme yap
            reply_message.edit_text("salam Sahibim Xoş gəldin Qrupa 🤖💙😍")
            reply_message.reply_animation("https://telegra.ph/file/6a8b0a19556719856e279.gif")
