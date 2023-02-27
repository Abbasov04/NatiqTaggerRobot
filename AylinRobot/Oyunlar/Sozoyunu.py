from AylinRobot import AylinRobot as app
from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from AylinRobot.Oyunlar import oyun
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
        







from pyrogram import Client
from pyrogram import filters
from random import shuffle
from AylinRobot.config import Config
from pyrogram.types import Message
from kelime_bot.helpers.keyboards import *
from helpers.kelimeler import kelime_sec



@app.on_message(filters.command("stop") & ~filters.private & ~filters.channel)
async def stop(c:Client, m:Message):
    global oyun
    
    siralama = []
    for i in oyun[m.chat.id]["oyuncular"]:
        siralama.append(f"{i}   :   {oyun[m.chat.id]['oyuncular'][i]} Bal")
    siralama.sort(reverse=True)
    siralama_text = ""
    for i in siralama:
        siralama_text += i + "\n"     
    
    await c.send_message(m.chat.id, f"**👤 {m.from_user.mention}** Tərəfindən Oyun Sonlandırıldı\n\nYeni Oyuna Başlamaq Üçün /oyna Əmrindən İsdifadə Edin !\n\n 🏆 Xallar səyfəsi  :\n\n{siralama_text}")
    oyun[m.chat.id] = {}
    
