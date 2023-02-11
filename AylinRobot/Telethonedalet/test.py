# t.me/RoBotlarimTg | YouTube: RoBotlarimTg | t.me/EdaletSup
# t.me/aykhan_s | t.me/edalet_22
# GitHub: EdaletRoBot

from telethon import events, Button
from telethon import TelegramClient
from telethon.tl.types import ChannelParticipantsAdmins
import random
from AylinRobot.config import Config
from telethon import TelegramClient
# Config məlumatları



@client.on(events.NewMessage(pattern="^/test$"))
async def start(event):
  if event.is_private:
     await event.reply(f"Test dəf kimi işləyir", buttons=(
        [Button.url("👤 Sahib", url="https://t.me/edalet_22")],
    ), 





print(">> Bot işləyir narahat olmayın. @edalet_22 Məlumat almaq üçün <<")
client.run_until_disconnected()
