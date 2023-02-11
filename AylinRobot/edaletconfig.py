from telethon import TelegramClient
# Config məlumatları

# Telegram Client (Telethon)
API_ID = 8953338
API_HASH = "fe21f223cb02d8f7c1cbda651f553a45"
bot_token = "5910888289:AAHOmBFyKIwc4XtbiZnkOQWk2-EZtx6BrT8"

edalet = TelegramClient('edalet', API_ID, API_HASH).start(bot_token=bot_token)
