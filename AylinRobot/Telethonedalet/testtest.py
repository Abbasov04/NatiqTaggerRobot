# t.me/RoBotlarimTg | YouTube: RoBotlarimTg | t.me/EdaletSup
# t.me/aykhan_s | t.me/edalet_22
# GitHub: EdaletRoBot
from telethon import events
from telethon import TelegramClient
from telethon.tl.types import ChannelParticipantsAdmins
import random
from AylinRobot.config import Config


edalet = TelegramClient('edalet', API_ID, API_HASH).start(bot_token=bot_token)

@edalet.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
     await event.reply(f"Salam, men hüsnü")

  if event.is_group:
    return await client.send_message(event.chat_id, f"Salam, men hüsnü",)




print(">> Bot işləyir narahat olmayın. @edalet_22 Məlumat almaq üçün <<")
edalet.run_until_disconnected()
