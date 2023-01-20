from AylinRobot.config import Config
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from pyrogram import idle, filters
from AylinRobot.config import Config
from pyrogram import Client, filters


@app.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(Config.BOT_USERNAME):
            await msg.reply(
                f'''`Salam` {msg.from_user.mention} `məni` {msg.chat.title} `qrupuna əlavə etdiyiniz üçün təşəkkürlər🥰`**''')

        elif str(new_user.id) == str(Config.OWNER_ID):
            await msg.reply('Sahibim indi qrupa qoşuldu😍\nxoş gəldin aramıza Sahibim, Necəsən?🥰')

            buttons = [[InlineKeyboardButton("➕ Qrupa Əlavə Et ➕",url="http://t.me/Rahid_Tag_Bot?startgroup=a"),
                    InlineKeyboardButton("🙇🏻 Sahib", url="https://t.me/Rahid_7"),
                    InlineKeyboardButton("🔮 Rəsmi", url="https://t.me/Rahid_44")]]
