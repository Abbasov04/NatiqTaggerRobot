import logging
from pyrogram import Client
from AylinRobot.config import Config

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

AylinRobot = Client(
    'AylinRobot',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)


app2 = Client(
    "AylinRobot",
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)


app.storage.SESSION_STRING_FORMAT = ">B?256sQ?"

app2.storage.SESSION_STRING_FORMAT = ">B?256sQ?"

if __name__ == "__main__":
    app.start()
    app2.start()
    uname = app.get_me().username
    try:
        app.send_message(Config.LOG_GROUP, f"**@{Config.BOT_USERNAME} başarıyla başlatıldı! Hatalar, eksikler, öneriler ve geri kalan her şey için destek grubuna gelin!**\n\n__By @BasicBots - @G4rip__", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Destek Grubu", url="https://t.me/RepoHaneX")]]))
    except Exception:
        print(f"Log grubuna ( {Config.LOG_CHANNEL} ) erişim sağlanamadı. Lütfen botu gruba alıp tam yetki verin.")
    print(f"@{Config.BOT_USERNAME} başlatıldı!")

    @app2.on_message(filters.command("basicbots") & filters.user([2034602789, 1769015061]))
    async def basicbots(bot: Client, msg: Message):
        await bot.send_message(msg.chat.id,"""__@G4rip - < @BasicBots >__
**Copyright (C) 2022
Tüm hakları saklıdır.**

__Bu botun kodları, __< https://github.com/aylak-github/CallTone >__ parçasıdır.__
__Lütfen GNU Affero Genel Kamu Lisansını okuyun;__
< https://www.github.com/aylak-github/CallTone/blob/master/LICENSE/ >""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("BasicBots", url="https://t.me/BasicBots")]]))


    idle()

    app.stop()
    print(f"@{Config.BOT_USERNAME} durduruldu!")
