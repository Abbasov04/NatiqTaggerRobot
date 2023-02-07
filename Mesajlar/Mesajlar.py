from pyrogram.types import Message
from pyrogram import idle, filters
from AylinRobot import AylinRobot as app
from AylinRobot import LOGGER

active_chats = []

@app.on_message(filters.text)
async def start(_, msg: Message):
    global active_chats
    text = msg.text.lower()
    chat_id = msg.chat.id
    if msg.chat.id not in active_chats:
        return
    if "salam" in text:
        await msg.reply_text(f"{random.choice(salam)}")
    if "necəsən" in text or "necesen" in text or "netersen" in text:
        await msg.reply_text(f"{random.choice(necesen)}")
    if "sagol" in text or "sağol" in text or "saqol" in text:
        await msg.reply_text(f"{random.choice(sagol)}")
    if "getdim" in text or "gedim" in text or "gedirəm" in text or "gedirem" in text:
        await msg.reply_text(f"{random.choice(getdim)}")
    if "geldim" in text or "gəldim" in text or "gəl" in text or "gəlirəm" in text:
        await msg.reply_text(f"{random.choice(geldim)}")
    if "ban" in text or "mute" in text or "purge" in text or "gban" in text:
        await msg.reply_text(f"{random.choice(ban)}")








salam = (
"Salam",
"Salam Kişi",
"Salam Balam",
"Salamdaa",
"Uşş balama salam",
"Salam Cənab 🫶",
"Salam Lələ 🔥",
)

necesen = (
"Saol",
"Həkimsən ?",
"Ə belədana 😂",
"What",
"İyyim aşkım sen ?",
"yaxşı olmağa çalışıram",
"Mən başımı buraxe sən necəsən 😂",
)

sagol = (
"Salam Sağol",
"Hara gedsən",
"Yatıram demə🥲",
"Sağolunnn yenə gözləyəriyy🙈",
"Uşş balam Sağol",
"Sağol canım benim 🫶",
"Sağol Kişi 🔥",
)

getdim = (
"Hara",
)

geldim = (
"Xoş Gəldin ❤️",
)

nermin = (
"Haycannn",
"Haycannn, Quzu kəsime sənə",
"Bəliii🫶",
"Nə gözəl deyirsəne, birdə de",
)

ban = (
"Vəhşii",
"Həri Vəhşii",
"Vəhşi Panteramm kimə ban atdın",
"Havada ban kokusu var",
)