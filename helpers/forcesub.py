# © Naviya2

import asyncio
from AylinRobot.config import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def ForceSub(bot: Client, event: Message):

    try:
        invite_link = await bot.create_chat_invite_link(chat_id=(int(Config.PLAYLIST_ID)))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, event)
        return fix_
    except Exception as err:
        print(f"{Config.PLAYLIST_ID} kanalına məcburi abunə olmaq mümkün deyil\n\nXəta: {err}\n\nSahibimlə: 👨‍💻 @{Config.OWNER_NAME} Əlaqə Saxla")
        return 200
    try:
        user = await bot.get_chat_member(chat_id=(int(Config.PLAYLIST_ID)), user_id=event.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=event.from_user.id,
                text=f" Məndən istifadə etmək qadağandır ☹️\nSahibimlə 👨‍💻 @{Config.OWNER_NAME} Əlaqə Saxla..",
                parse_mode="markdown",
                disable_web_page_preview=True,
                reply_to_message_id=event.message_id
            )
            return 400
        else:
            return 200
    except UserNotParticipant:
        await bot.send_message(
            chat_id=event.from_user.id,
            text="<b>Salam {} 👋\n\nKanalımıza abunə olana qədər məndən istifadə edə bilməzsiniz ☹️\n\nOdur ki, aşağıdakı düymə ilə Kanalımıza qoşulun və '🙋‍♀️ Yenilə' düyməsini sıxın 😊</b>".format(event.from_user.mention),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("📣 Kanalımız", url=invite_link.invite_link)
                    ],

                    [   
                        InlineKeyboardButton("🙋‍♀️ Yenilə", callback_data="refreshme")
                    ],
                ]
            ),
        return 400
    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, event)
        return fix_
    except Exception as err:
        print(f"Nə isə səhv getdi!  Məcburi Abunə olmaq mümkün deyil.\nXəta: {err}\n\nSahibim İlə @{Config.OWNER_NAME} Əlaqə Saxla")
        return 200
