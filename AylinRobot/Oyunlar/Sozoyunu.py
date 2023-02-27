from AylinRobot import AylinRobot as app
from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from AylinRobot import oyun
from helpers.kelimeler import *
from helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import Message


@app.on_message(filters.command("game")) 
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**❗ Qrupunuzda Hak-Hazırda Oyun Artıq Davam Edir ✍🏻 \n Oyunu Sonlandırmaq Üçün /dayan Əmrindən İsdifadə Edin")
    else:
        await m.reply(f"**👤 {m.from_user.mention}** Tərəfindən! \nOyun Başladıldı .\n\nUğurlar !", reply_markup=kanal)
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["kec"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/100 
🔡 Söz :   <code>{kelime_list}</code>
🏆 Qazandığın Xal: 50
ℹ İpucu: 1. {oyun[m.chat.id]["kelime"][0]}
〽️ Uzunluq : {int(len(kelime_list)/2)} 

✏️ Qarışıq hərflərdən ibarət sözü tapın 
        """
        await c.send_message(m.chat.id, text)
        
