from AylinRobot import AylinRobot as app
from AylinRobot.config import Config


db = Database(Config.MONGODB_URI, Config.BOT_USERNAME)
mongo_db_veritabani = MongoClient(Config.MONGODB_URI)
dcmdb = mongo_db_veritabani.handlers


delcmdmdb = dcmdb.admins

async def delcmd_is_on(chat_id: int) -> bool:
    chat = await delcmdmdb.find_one({"chat_id": chat_id})
    return not chat


async def delcmd_on(chat_id: int):
    already_del = await delcmd_is_on(chat_id)
    if already_del:
        return
    return await delcmdmdb.delete_one({"chat_id": chat_id})


async def delcmd_off(chat_id: int):
    already_del = await delcmd_is_on(chat_id)
    if not already_del:
        return
    return await delcmdmdb.insert_one({"chat_id": chat_id})



@app.on_message(filters.command("delcmd") & ~filters.private)
async def delcmdc(bot: Client, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("Bu komutu kullanmak için komutunuzun yanına 'off' ya da 'on' yazınız.")
    durum = message.text.split(None, 1)[1].strip()
    durum = durum.lower()
    chat_id = message.chat.id

    if durum == "on":
        if await delcmd_is_on(message.chat.id):
            return await message.reply_text("Komut Silme Zaten Açık.")
        else:
            await delcmd_on(chat_id)
            await message.reply_text("Bu sohbet için Komut Silme özelliği başarıyla etkinleştirildi.")

    elif durum == "off":
        await delcmd_off(chat_id)
        await message.reply_text("Bu Sohbet için Komut Silme özelliği başarıyla devre dışı bırakıldı.")
    else:
        await message.reply_text("Bu komutu kullanmak için komutunuzun yanına 'off' ya da 'on' yazınız.")