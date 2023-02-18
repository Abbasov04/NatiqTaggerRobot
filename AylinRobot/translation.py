# @AylinRobot
#@MusicAzBot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
╔═════════════════
║▻ **🙋‍♀️ Salam {}**
║
║▻ 🙎‍♀️ Mənim Adım  ️️️️️️{} Mən 
║▻ 🇦🇿 Azərbaycan Dilində Çox Özəllikili 
║▻ 💌 Telegram Botuyam Bacarıqlarımı Görmək Üçün
║▻ `📚 Kömək` Buttonuna Toxun
╚═════════════════
👨‍💻 **Sahibim** ♒️ @{}

"""    


    GSTART_TEXT = """
╔═════════════════
║▻ 🙋‍♀️ {} 
║
║▻ 🙎‍♀️️️️️️️ {} {} Grupunda Super İşləyir 🥳
╚═════════════════
👨‍💻 **Sahibim** ♒️ @{}

"""    

    GHELP_TEXT = """
╔═════════════════
║▻ 🙋‍♀️ {} 
║
║▻ 💁‍♀️ {}-Un Əmrləri ini  Görmək Üçün ♒️ Kömək Buttonuna Toxun ⤵️
╚═════════════════
"""    

   PMHELP_TEXT = """
   {}
"""
    HELP_TEXT = """
╔═════════════════
║▻ **🙋‍♀️ Salam {} 
║
║▻ 💁‍♀️ {} - Un  
║▻ 📚 Əmrləri  Bunlardır Aşağıdakı 
║▻ 🖲 Buttonlara Toxunaraq istədiyiniz
║▻ ✔️ Əmr Haqqında Məlumat Ala Bilərsiniz 
╚═════════════════
"""

### Bot Haqqında Ümumi Məlumat

    BH_TEXT = """
╔═════════════════
║▻ **🙋‍♀️ Salam {} 
║
║▻ 🙎‍♀️ {} 🇦🇿 Azərbaycan Dilində Çox Özəllikli Telegram Botudur...**
║
║▻ ✨ Bot Versiyası: v0.7.0
║▻ 🍀 Pyrogram Versiyası: 2.0.97
║▻ ✨ Python Versiyası: 3.11.1
║▻ ⚙️ Server [Heroku](https://heroku.com)
║▻ 👨‍💻 Mənim Sahibim @{}
║▻ 📆 Botun İstifadəyə Verilmə Tarixi `20.11.2022` 
╚═════════════════
╔═════════════════
║▻ **⚠️ Qeyd Botun Qrupunuzda İşləməsi 
║▻ Üçün Admin Əmirlərindən Sadəcə 
║▻ 💬 Mesajları Silmə 🚫 Yetkisi Verin**
╚═════════════════
"""


    SAHIB_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /stats
║▻ 📃 Açıqlama: Bot haqqında ümumi məlumat verər.
║
║▻ 🔮 Istifadə: /broadcastall
║▻ 📃 Açıqlama: Qrupa Və Şəxsiyə Yayım Edər.
║
║▻ 🔮 Istifadə: /gcast
║▻ 📃 Açıqlama: Qruplarda yayım edər.
║
║▻ 🔮 Istifadə: /broadcast_pin
║▻ 📃 Açıqlama: Qruplarda yayım edər və pinləyər.
║
║▻ 🔮 Istifadə: /dyno
║▻ 📃 Açıqlama: Heroku Dyno Miqdarını Ölçər.
╚═════════════════
"""

    MUSIC_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /song 
║▻ 🧩 Nümunə: /song Rei - Ah Canım Sevgilim
║▻ 📃 Açıqlama: Musiqi yükləyir.
║
║▻ 🔮 Istifadə: /video
║▻ 🧩  Nümunə:/video Rei - Ah Canım Sevgilim
║▻ 📃 Açıqlama: Video yükləyir.
║
║▻ 🔮 Istifadə: /lyrics 
║▻ 🧩 Nümunə: /lyrics Rei - Ah Canım Sevgilim
║
║▻ 📃 Açıqlama: Musiqinin sözlərini tapır.
╚═════════════════
"""

    TELEGRAPH_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /tgm
║▻ 📃 Açıqlama: Şəkil, video və ya GIF göndərərək link ala bilərsiniz.
╚═════════════════
"""

    SEHID_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /sehid 
║▻ 📃 Açıqlama:  Bu əmr vaistəsiylə sizə **Şəhid** adları göndərəcəm
╚═════════════════
╔═════════════════
║▻ 🥀 **Allah bütün Şəhidimizə rəhmət eləsin**
║▻ 🤲 Qazilərimizə şəfa versin 
║▻ 😔 Başın sağolsun Azərbaycan 🇦🇿
║▻ 🇦🇿 Bazada **2881** Şəhid adı mövcuddur
╚═════════════════
""" 
    OYUN_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /zer
║▻ 📃 Açıqlama: zər atar
║
║▻ 🔮 Istifadə: /top
║▻ 📃 Açıqlama: top atar
║
║▻ 🔮 Istifadə: /bowling
║▻ 📃 Açıqlama: bowling atar
║
║▻ 🔮 Istifadə: /ox
║▻ 📃 Açıqlama: ox atar
║
║▻ 🔮 Istifadə: /jackpot
║▻ 📃 Açıqlama: jackpot atar
║
║▻ 🔮 Istifadə: /basket
║▻ 📃 Açıqlama: basket atar
╚═════════════════
"""

    EYLENCE_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /soxri 
║▻ 📃 Açıqlama: Rondom 16+ Şəkillər Atar.
║
║▻ 🔮 Istifadə: /pisik
║▻ 📃 Açıqlama: Rondom Pişik Şəkili Atar
║
║▻ 🔮 Istifadə: /anime
║▻ 📃 Açıqlama: Rondom Anime Şəkili Atar
║
║▻ 🔮 Istifadə: /masin
║▻ 📃 Açıqlama: Rondom Maşın Şəkili Atar
║
║▻ 🔮 Istifadə: /masin2
║▻ 📃 Açıqlama: Rondom Maşın Videosu Atar
║
║▻ 🔮 Istifadə: /tema
║▻ 📃 Açıqlama: Rondom Telegram Teması Atar
║
║▻ 🔮 Istifadə: /pp
║▻ 📃 Açıqlama: Rondom Profil Şəkili Atar
║
║▻ 🔮 Istifadə: /sevgi
║▻ 📃 Açıqlama: Hazır Sevgi Yə Aid Sözlər Atar.
║
║▻ 🔮 Istifadə: /bio
║▻ 📃 Açıqlama: Hazır Bio Nuz Üçün Sözlər Atar.
║
║▻ 🔮 Istifadə: /ship
║▻ 📃 Açıqlama: Qrupda  Rondom  Bir Cütlük Seçər.
╚═════════════════
"""


    ELAVELER_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /carbon
║▻ 📃 Açıqlama: Yazdığınız mesajı şəkilə çevirin
║
║▻ 🔮 Istifadə: /id
║▻ 📃 Açıqlama: İstifadəçinin ID alın.
║
║▻ 🔮 Istifadə: /info
║▻ 📃 Açıqlama: İstifadəçi haqqında məlumat verər
║
║▻ 🔮 Istifadə: /alive
║▻ 📃 Açıqlama: Botun işlək olduğunu yoxlayar.
║
║▻ 🔮 Istifadə: /bots
║▻ 📃 Açıqlama: Qrupunuzda Olan Botları Göstərər.
║
║▻ 🔮 Istifadə: /alist
║▻ 📃 Açıqlama: Qrupunuzda Olan Adminləri Göstərər.
╚═════════════════
"""


    AXTARIS_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /github 
║▻ 🧩 Nümunə: /github HesenovHuseyn
║▻ 📃 Açıqlama: Github Axtarışı Edər.
║
║▻ 🔮 Istifadə: /search
║▻ 🧩 Nümunə: /search Rei - Ah Canım Sevgilim
║▻ 📃 Açıqlama: YouTube axtarış üçün istifadə edə bilərsiniz.
╚═════════════════
"""

    TAGGER_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /tag
║▻ 📃 Açıqlama: İstifadəçiləri  Səbəbsiz Tag Edər.
║ 
║▻ 🔮 Istifadə: /cancel
║▻ 📃 Açıqlama: Tag Prosesini  Dayandırar.
║
║▻ 🔮 Istifadə: /tektag
║▻ 📃 Açıqlama:  İstifadəçiləri Tək-Tək Tag Edər.
╚═════════════════
"""


class LAN(object):

    STATS_STARTED = """
{} **Zəhmət olmasa gözləyin, bilgiləri gətirirəm!**
"""
    STATS = """
**@{} Məlumatları**\n\n**İstifadəçiləri;**\n» **Ümumi söhbətlər:** `{}`\n» **Ümumi qruplar: `{}`\n» **Ümumi PM's: `{}`\n\n**Disk İstifadəsi;**\n» **Disk'in Sahəsi:** `{}`\n» **İstifadə edilən:** `{}({}%)`\n» **Boş qalan:** `{}`\n\n**🎛 Ən yüksək istifadə dəyərləri;**\n» **CPU:** `{}%`\n» **RAM:** `{}%`\n**Versiyalar;**\n» **Pyrogram:** {}
"""