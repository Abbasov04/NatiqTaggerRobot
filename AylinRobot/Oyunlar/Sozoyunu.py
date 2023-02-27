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


# Oyunu başlat. 
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
        await m.reply("**❗ Oyun Onsuzda Qrupnuzda Davam edir ✍🏻 \n Oyunu dayandırmaq üçün /stop yazabilərsiniz")
    else:
        await m.reply(f"**{m.from_user.mention}** Tarafından! \nKelime Bulma Oyunu Başladı .\n\nHər birinizə uğurlar ❤️✨ !",reply_markup=kanal) 
        
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
🎯 Raund : {oyun[m.chat.id]['round']}/20 
📝 Tapılacaq Söz :   <code>{kelime_list}</code>
💰 Yığdınız Xal: 1
🔎 İlk Hərf: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {int(len(kelime_list)/2)} 

✏️ Qarışıq Həriflərdən düzgün sözü tapın.
        """
        await c.send_message(m.chat.id, text)
        
        
from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from helpers.keyboards import *
from helpers.kelimeler import kelime_sec



@app.on_message(filters.command("kec") & ~filters.private & ~filters.channel)
async def passs(c:Client, m:Message):
    global oyun
    
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        if oyun[m.chat.id]["kec"] < 3:
            oyun[m.chat.id]["kec"] += 1 
            await c.send_message(m.chat.id,f"😑 Maksimum 3 keçmə haqqınız var!\n➡️ Söz uğurla keçildi !\n✏️ Düzgün Söz : **<code>{oyun[m.chat.id]['kelime']}</code>**")
            
            oyun[m.chat.id]["kelime"] = kelime_sec()
            oyun[m.chat.id]["aktif"] = True
            
            kelime_list = ""
            kelime = list(oyun[m.chat.id]['kelime'])
            shuffle(kelime)
            
            for harf in kelime:
                kelime_list+= harf + " "
            
            text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/20 
📝 Tapılacaq Sözlər :   <code>{kelime_list}</code>
💰 Qazandığın Xal : 1
🔎 İlk hərf : 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 𝖴𝗓𝗎𝗇𝗅uq: {int(len(kelime_list)/2)} 

✏️ Qarışıq həriflərdən düzgün sözü tapın.
            """
            await c.send_message(m.chat.id, text)
            
        else:
            await c.send_message(m.chat.id, f"<code>**❗ Keçiş Düzgün Qeydedildi! </code> \n Oyunu dayandırmaq üçün yazıb /cancel dayandıra bilərsiniz ✍🏻**")
    else:
        await m.reply(f"❗ **Qrupunuzda aktiv oyun oynanılır!\n Yeni bir oyuna başlamaq üçün /oyun yazabilərsiniz✍🏻**")
        