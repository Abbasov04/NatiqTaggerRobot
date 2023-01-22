from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AylinRobot.config import Config
from AylinRobot.Plugin import *

    START_TEXT = """
**Salam {} 👋**

**Mənim Adım  ️️️️️️{} 🙋‍♀️ Mən Azərbaycan Dilində Çox Özəllikili Telegram Botuyam Bacarıqlarımı Görmək Üçün `💠 Kömək` Buttonuna Toxun**

"""    
    HELP_TEXT = """
**{} 🙈 Əmrlərim Bunlardır  Buttonlara toxunaraq istədiyiniz əmr haqqında məlumat ala bilərsiniz**

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