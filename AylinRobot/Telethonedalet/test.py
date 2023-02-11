# t.me/RoBotlarimTg | YouTube: RoBotlarimTg | t.me/EdaletSup
# t.me/aykhan_s | t.me/edalet_22
# GitHub: EdaletRoBot

from telethon import events
from telethon import TelegramClient
from telethon.tl.types import ChannelParticipantsAdmins
import random
from AylinRobot.edaletconfig import edalet

edalet = TelegramClient('edalet', API_ID, API_HASH).start(BOT_TOKEN=BOT_TOKEN)


#@edalet_22 terefindən @RoBotlarimTg üçün yazilib silmədən istifadə edin
@edalet.on(events.NewMessage(pattern="^/idid ?(.*)"))
async def id(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_id = previous_message.sender_id
        chat_id = event.chat_id
        if event.is_private:
            return await event.reply(f"**Sizin Telegram id:** `{user_id}`")
        else:
            return await event.reply(f"**İstifadəçi id:** `{user_id}`\n**Qrup id:** `{chat_id}`")


#@edalet_22 terefindən @RoBotlarimTg üçün yazilib silmədən istifadə edin
    else:
        user_id = event.sender_id
        chat_id = event.chat_id
        if event.is_private:
            return await event.reply(f"**Sizin Telegram id:** `{user_id}`")
        else:
            return await event.reply(f"**İstifadəçi id:** `{user_id}`\n**Qrup id:** `{chat_id}`")

print(">> Bot işləyir narahat olmayın. @edalet_22 Məlumat almaq üçün <<")
client.run_until_disconnected()
