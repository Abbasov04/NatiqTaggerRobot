import os
from LeoSongDownloaderBot.translation import Translation
import config
from pyrogram import Client
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from LeoSongDownloaderBot import LeoSongDownloaderBot as app

@app.on_callback_query()
async def cb_data(client, message):
    if message.data == "home":
        await message.message.edit_text(
            text=Translation.START_TEXT.format(message.from_user.mention),
            reply_markup=Translation.START_BUTTONS,
            disable_web_page_preview=True,
        )
    elif message.data == "help":
        await message.message.edit_text(
            text=Translation.HELP_TEXT.format(message.from_user.mention),
            reply_markup=Translation.HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "about":
        await message.message.edit_text(
            text=Translation.ABOUT_TEXT,
            reply_markup=Translation.ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "aboutdev":
        await message.message.edit_text(
            text=Translation.ABOUT_DEV_TEXT,
            reply_markup=Translation.ABOUT_DEV_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "info":
        await message.message.edit_text(
            text=Translation.INFO_TEXT.format(username=message.from_user.username, first_name=message.from_user.first_name, last_name=message.from_user.last_name, user_id=message.from_user.id, mention=message.from_user.mention),
            reply_markup=Translation.INFO_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "refreshme":
        if config.UPDATES_CHANNEL:
            invite_link = await client.create_chat_invite_link(int(config.UPDATES_CHANNEL))
            try:
                user = await client.get_chat_member(int(config.UPDATES_CHANNEL), message.message.chat.id)
                if user.status == "kicked":
                    await message.message.edit(
                        text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/leosupportx).",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await message.message.edit(
                    text="<b>Hey</b> {},\n\n<b>You still didn't join our Updates Channel ☹️ \nPlease Join and hit on the 'Refresh 🔄' Button</b>".format(message.from_user.mention),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Join Our Updates Channel 🗣", url=invite_link.invite_link)
                            ],
                            [
                                InlineKeyboardButton("Refresh 🔄", callback_data="refreshme")
                            ]
                        ]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await message.message.edit(
                    text="Something went Wrong. Contact my [Support Group](https://t.me/leosupportx).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        await message.message.edit(
            text=Translation.START_TEXT.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=Translation.START_BUTTONS,
        )
    else:
        await message.message.delete()
