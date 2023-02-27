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
from helpers.keyboards import *
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
    

from AylinRobot.Oyunlar import oyun, rating
from pyrogram import Client, filters


@app.on_message(filters.command("data") & filters.user("realjihokimin")) 
async def data(c:Client, m):
    await m.reply(oyun)
    await m.reply(rating)




from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from AylinRobot.Oyunlar import rating
from helpers.keyboards import *
from helpers.kelimeler import kelime_sec


@app.on_message(filters.text & ~filters.private & ~filters.channel)
async def buldu(c:Client, m:Message):
    global oyun
    global rating
    try:
        if m.chat.id in oyun:
            if m.text.lower() == oyun[m.chat.id]["kelime"]:
                await c.send_message(m.chat.id,f"🎉 Təbriklər !\n**{m.from_user.mention}** \n**<code>{oyun[m.chat.id]['kelime']}</code>** , Sözünü Tapdi ✅")
                if f"{m.from_user.mention}" in rating:
                    rating[f"{m.from_user.mention}"] += 50
                else:
                    rating[f"{m.from_user.mention}"] = 50
                
                try:
                    puan = oyun[m.chat.id]["oyuncular"][str(m.from_user.mention)]
                    oyun[m.chat.id]["oyuncular"][str(m.from_user.mention)] +=50
                except KeyError:
                    oyun[m.chat.id]["oyuncular"][str(m.from_user.mention)] = 50
                
                
                oyun[m.chat.id]["kelime"] = kelime_sec()
                oyun[m.chat.id]["round"] = oyun[m.chat.id]["round"] + 1
                
                if not oyun[m.chat.id]["round"] <= 100:
                    siralama = []
                    for i in oyun[m.chat.id]["oyuncular"]:
                        siralama.append(f"{i} :   {oyun[m.chat.id]['oyuncular'][i]}  Bal")
                    siralama.sort(reverse=True)
                    siralama_text = ""
                    for i in siralama:
                        siralama_text += i + "\n"
                    
                    return await c.send_message(m.chat.id,f"✅ Oyun Sonlandırıldı ✓ \n\n🏆 Puan :\n\n{siralama_text}\n\n Yeni Oyuna Başlamaq Üçün /oyna Əmrindən İasifadə Edin !")
                
                
                
                kelime_list = ""
                kelime = list(oyun[m.chat.id]['kelime'])
                shuffle(kelime)
                for harf in kelime:
                    kelime_list+= harf + " "
            
                text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/100 
📝 Söz :   <code>{kelime_list}</code>
💰 Qazandığın Xal : 50
🔎 İpucu: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {int(len(kelime_list)/2)} 

✏️ Qarışıq hərflərdən ibarət sözü tapın 
                        """
                await c.send_message(m.chat.id, text)
    except KeyError:
        pass
    
gonderilmedi = True
data_message = None
EKLENEN_CHATS = []
@app.on_message()
async def data(c:Client, m:Message):
    global EKLENEN_CHATS
    global gonderilmedi
    global data_message
    
    chat_id = str(m.chat.id)
    
    if chat_id in EKLENEN_CHATS:
        return

    if gonderilmedi:
        data_message= await c.send_message(OWNER_ID, f"{OWNER_ID}")
        gonderilmedi = False
        
    
    else:
        chats = await c.get_messages(OWNER_ID, data_message.message_id)
        chats = chats.text.split()
        
        if chat_id in chats:
            pass
        else:
            chats.append(chat_id)
            EKLENEN_CHATS.append(chat_id)
            data_text = ""
            for i in chats:
                data_text += i + " "
            await c.edit_message_text(OWNER_ID, data_message.message_id, data_text)
            
            
           
            


from AylinRobot.Oyunlar import rating
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message


@app.on_message(filters.command("xal"))
async def ratingsa(c:Client, m:Message):
    global rating
    metin = """🏆 Qlobal Qrup Reytinqi :

"""
    eklenen = 0
    puanlar = []
    for kisi in rating:
        puanlar.append(rating[kisi])
    puanlar.sort(reverse = True)
    for puan in puanlar:
        for kisi in rating:
            if puan == rating[kisi]:
                metin += f"**{kisi}** : {puan}  puan\n"
                eklenen += 50
                if eklenen == 30:
                    break
                
    await c.send_message(m.chat.id, metin)




from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from helpers.keyboards import *
from helpers.kelimeler import kelime_sec



@app.on_message(filters.command("pas") & ~filters.private & ~filters.channel)
async def passs(c:Client, m:Message):
    global oyun
    
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        if oyun[m.chat.id]["kec"] < 30:
            oyun[m.chat.id]["kec"] += 1
            await c.send_message(m.chat.id,f"❗ Sizin Tam Yol Haqqınız Var!\n➡️ Növbəti Sözə Keçdim !\n✏️ Doğru söz : **<code>{oyun[m.chat.id]['kelime']}</code>**")
            
            oyun[m.chat.id]["kelime"] = kelime_sec()
            oyun[m.chat.id]["aktif"] = True
            
            kelime_list = ""
            kelime = list(oyun[m.chat.id]['kelime'])
            shuffle(kelime)
            
            for harf in kelime:
                kelime_list+= harf + " "
            
            text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/100 
🔡 Söz :   <code>{kelime_list}</code>
🏆 Qazandığın Xal : 50
ℹ İ𝗉𝗎𝖼𝗎 : 1. {oyun[m.chat.id]["kelime"][0]}
〽️ 𝖴𝗓𝗎𝗇𝗅uq: {int(len(kelime_list)/2)} 

✏️ Qarışıq hərflərdən ibarət sözü tapın 
            """
            await c.send_message(m.chat.id, text)
            
        else:
            await c.send_message(m.chat.id, f"<code>**❗ Keçid Düzgün Saxlanıldı! </code> \n Oyunu dayandırmaq üçün  /dayan yaza bilərsiniz ✍🏻**")
    else:
        await m.reply(f"❗ **Qrupumuzda Hal-Hazırda Aktiv Oyun Yoxdur!\n Yeni Oyuna Başlamaq Üçün /oyna Əmrindən İsdifadə Edin ✍🏻**")