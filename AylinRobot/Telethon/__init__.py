from telethon import events, Button
from telethon import TelegramClient
from telethon.tl.types import ChannelParticipantsAdmins
import random
from AylinRobot.config import Config
from telethon import TelegramClient

@client.on(events.NewMessage(pattern="^/test$"))
async def start(event):
  if event.is_private:
     await event.reply(f"Test dəf kimi işləyir", buttons=(
        [Button.url("👤 Sahib", url="https://t.me/edalet_22")],
    ), 
