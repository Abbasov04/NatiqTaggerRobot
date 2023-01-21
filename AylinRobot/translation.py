from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AylinRobot.config import Config

class Translation(object):

    START_TEXT = """
**Salam {} 👋**

**Mənim Adım  ️️️️️️{} 🙋‍♀️ Mən Azərbaycan Dilində Çox Özəllikili Telegram Botuyam Bacarıqlarımı Görmək Üçün `💠 Kömək` Buttonuna Toxun**

"""    
    HELP_TEXT = """
**{} 🙈 Əmrlərim Bunlardır  Buttonlara toxunaraq istədiyiniz əmr haqqında məlumat ala bilərsiniz**

"""

GROUPSTART_TEXT = """
{} Salam {} - Un Əmrlərini Görmək Üçün

"""


   KOMEK_TEXT = """
Aşağıdakı buttona

"""

    SAHIB_TEXT = """

🔮 Istifadə: /stats
📃 Açıqlama: Bot haqqında ümumi məlumat verər.

🔮 Istifadə: /broadcast
📃 Açıqlama: Şəxsidə Yayım Edər.

🔮 Istifadə: /gcast
📃 Açıqlama: Qruplarda yayım edər.

🔮 Istifadə: /broadcast_pin
📃 Açıqlama: Qruplarda yayım edər və pinləyər.

🔮 Istifadə: /broadcastall
📃 Açıqlama: Qrupa Və Şəxsiyə yayım edər.



"""

    MUSIC_TEXT = """
🔮 Istifadə: /song 
🧩 Nümunə: /song Rei - Ah Canım Sevgilim
📃 Açıqlama: Musiqi yükləyir.

🔮 Istifadə: /video
🧩  Nümunə:/video Rei - Ah Canım Sevgilim
📃 Açıqlama: Video yükləyir.

🔮 Istifadə: /lyrics 
🧩 Nümunə: /lyrics Rei - Ah Canım Sevgilim
📃 Açıqlama: Musiqinin sözlərini tapır.

🔮 Istifadə: /search
🧩 Nümunə: /search Rei - Ah Canım Sevgilim
📃 Açıqlama: YouTube axtarış üçün istifadə edə bilərsiniz.
"""

    TELEGRAPH_TEXT = """

🔮 Istifadə: /tgm
📃 Açıqlama: Şəkil, video və ya GIF göndərərək link ala bilərsiniz.

"""

    SEHID_TEXT = """

🔮 Istifadə: /sehid 
📃 Açıqlama:  Bu əmr vaistəsiylə sizə *Şəhid* adları göndərəcəm

*Allah bütün Şəhidimizə rəhmət eləsin*
Qazilərimizə şəfa versin 
Başın sağolsun Azərbaycan 🇦🇿
Bazada *2881* Şəhid adı mövcuddur

""" 
    OYUN_TEXT = """

🔮 Istifadə: /zer
📃 Açıqlama: zər atar

🔮 Istifadə: /top
📃 Açıqlama: top atar

🔮 Istifadə: /bowling
📃 Açıqlama: bowling atar

🔮 Istifadə: /ox
📃 Açıqlama: ox atar

🔮 Istifadə: /jackpot
📃 Açıqlama: jackpot atar

"""

    EYLENCE_TEXT = """

🔮 Istifadə: /soxri 
📃 Açıqlama: Rondom 16+ Şəkillər Atar.

🔮 Istifadə: /pisik
📃 Açıqlama: Rondom Pişik Şəkili Atar

🔮 Istifadə: /anime
📃 Açıqlama: Rondom Anime Şəkili Atar

🔮 Istifadə: /masin
📃 Açıqlama: Rondom Maşın Şəkili Atar

🔮 Istifadə: /masin2
📃 Açıqlama: Rondom Maşın Videosu Atar

🔮 Istifadə: /tema
📃 Açıqlama: Rondom Telegram Teması Atar

🔮 Istifadə: /pp
📃 Açıqlama: Rondom Profil Şəkili Atar

🔮 Istifadə: /sevgi
📃 Açıqlama: Hazır Sevi Yə Aid Sözlər Atar.

🔮 Istifadə: /bio
📃 Açıqlama: Hazır Bio Nuz Üçün Sözlər Atar.

"""


    ELAVELER_TEXT = """

🔮 Istifadə: /carbon
📃 Açıqlama: Yazdığınız mesajı şəkilə çevirin

🔮 Istifadə: /id
📃 Açıqlama: İstifadəçinin s ID alın.

🔮 Istifadə: /info
📃 Açıqlama: İstifadəçi haqqında məlumat verər

🔮 Istifadə: /alive
📃 Açıqlama: Botun işlək olduğunu yoxlayar.

"""





    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("👾 Botlist", url=f"https://t.me/{Config.BOTLIST}"),
        InlineKeyboardButton("📢 Kanal", url=f"https://t.me/{Config.SUPPORT}"),
        ],[                  
        InlineKeyboardButton('💠 Kömək', callback_data='help'),
        ],[        
        InlineKeyboardButton('➕ Məni Qrupa Əlavə Et ➕', url=f"https://t.me/{Config.BOT_USERNAME}?startgroup=true"),
        ],[                
        InlineKeyboardButton('Sahibim🧑‍💻',  url=f"https://t.me/{Config.OWNER_NAME}"),
        InlineKeyboardButton("🎵 Playlist", url=f"https://t.me/{Config.PLAYLIST_NAME}"),
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🎵 Musiqi', callback_data='musıc'),
        InlineKeyboardButton('⭐ Telegraph', callback_data='tg')
        ],[
        InlineKeyboardButton('🎮 Oyunlar', callback_data='oyun'),
        InlineKeyboardButton('🇦🇿 Şəhidlər', callback_data='sehıd'),
        ],[        
        InlineKeyboardButton('🌀 Əyləncə', callback_data='eylence'),
        InlineKeyboardButton('Əlavələr', callback_data='elave'),
        ],[
        InlineKeyboardButton('👨‍💻 Sahib Əmrləri', callback_data='sahib'), 
        ],[        
        InlineKeyboardButton('↪️ Geri Qayıt', callback_data='home'),
        ]]
    )
    
    KOMEK_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("👾 Botlist", url=f"https://t.me/{Config.BOTLIST}"),
        InlineKeyboardButton("📢 Kanal", url=f"https://t.me/{Config.SUPPORT}"),
        ],[                  
        InlineKeyboardButton('💠 Kömək', callback_data='help'),    
    
    
    
    
    
    
    MUSIC_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),
        ]]
    )
    TELEGRAPH_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),
        ]]
    )
    SEHID_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),
        ],[
        InlineKeyboardButton('Close ❎', callback_data='close')      
        ]]
    )        
    OYUN_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),
        ]]
    )
    EYLENCE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),
        ]]
    )     
    SAHIB_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),
        ]]
    )
    ELAVE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),
        ]]
    ) 
    