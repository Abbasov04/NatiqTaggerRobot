import random
from time import time
from random import choice
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from AylinRobot import LOGGER
from pyrogram import idle, filters
from AylinRobot.config import Config



photolist = ["https://telegra.ph/file/f935b760951d3169e0984.jpg","https://telegra.ph/file/9d6acaa24e41b2b599cc7.jpg","https://telegra.ph/file/88a086c49ca1f02a22e1a.jpg","https://telegra.ph/file/9366471ebff1f5f28123a.jpg","https://telegra.ph/file/c00e51dbd5d1976bd77dc.jpg","https://telegra.ph/file/56d97c2958df366498aa1.jpg","https://telegra.ph/file/09dd6be50d92591207f0e.jpg","https://telegra.ph/file/153481a7d1c175a720237.jpg","https://telegra.ph/file/72a68f343a74a84ce99e2.jpg","https://telegra.ph/file/dcb98afdb299ceefbffcf.jpg","https://telegra.ph/file/aa7ee03073bbbd18f06a2.jpg","https://telegra.ph/file/d8b0c106545daf8988503.jpg","https://telegra.ph/file/a55fdc67245639883fb39.jpg","https://telegra.ph/file/1b5265a0a693df115580e.jpg","https://telegra.ph/file/ffc7b86a1cdf39eefb1ac.jpg","https://telegra.ph/file/ec84ed1dede587311d36c.jpg","https://telegra.ph/file/3de3c9ded52b52cba4044.jpg","https://telegra.ph/file/a12960f0c99069c9dc041.jpg","https://telegra.ph/file/8b3040442bd20d7aaa626.jpg","https://telegra.ph/file/f9a8ec4174b482538f2b4.jpg","https://telegra.ph/file/3bc2bd856a7e6f64b6184.jpg","https://telegra.ph/file/a62274e6688bb98e76af0.jpg","https://telegra.ph/file/ba1dc43eff20e17715fa6.jpg","https://telegra.ph/file/2fdd10c8bfded3730c8ac.jpg","https://telegra.ph/file/f4de94bd8cca9bc2ace34.jpg","https://telegra.ph/file/de54a224dfd797d2b4068.jpg","https://telegra.ph/file/d50d0a5754a870dec9063.jpg","https://telegra.ph/file/815d1bc20c154333a167f.jpg","https://telegra.ph/file/596f631957c0b9be63ea4.jpg","https://telegra.ph/file/05478068474f5c79d6e13.jpg","https://telegra.ph/file/0bb59cf85a8c2332f07e6.jpg","https://telegra.ph/file/d877f9ed5a46affb63399.jpg","https://telegra.ph/file/263a5ae2d5d2877a831e8.jpg","https://telegra.ph/file/863f4571222bf505646cc.jpg","https://telegra.ph/file/c5533fa38ec8855f368e5.jpg","https://telegra.ph/file/d62d808a5e0e3f636dc0d.jpg","https://telegra.ph/file/17da4b99cf4210d4f2adf.jpg","https://telegra.ph/file/96245f89c6c6fec865689.jpg","https://telegra.ph/file/93b0960b7cb385fadc3eb.jpg","https://telegra.ph/file/9a4ca6745d61707ef3cb6.jpg","https://telegra.ph/file/eb2bd4eca88a4b69aa47e.jpg","https://telegra.ph/file/c1677ef08e960c008ea1d.jpg","https://telegra.ph/file/352e670aa873dc35eb13e.jpg","https://telegra.ph/file/f45ef4d09e18b47c5eb40.jpg","https://telegra.ph/file/6eefc38a1468554027355.jpg","https://telegra.ph/file/0f6d5c01652fa4db2f9aa.jpg","https://telegra.ph/file/b5b1bb5e6db2422cc7798.jpg","https://telegra.ph/file/d582f25fb5ba251d1bd8d.jpg","https://telegra.ph/file/952fc4d9e2db2a4e10396.jpg","https://telegra.ph/file/c35678c0f51e25c319c2e.jpg","https://telegra.ph/file/0022c541ab1eafd052808.jpg","https://telegra.ph/file/512c2655d6818146a77b6.jpg","https://telegra.ph/file/aca1a231ea6458ee078d3.jpg","https://telegra.ph/file/460d9671ec16c5085d038.jpg","https://telegra.ph/file/76d5dbeaa368e64f3bccf.jpg","https://telegra.ph/file/5c0a3e97e131189b34cc1.jpg","https://telegra.ph/file/b59c08f4c207cc574e54a.jpg","https://telegra.ph/file/0221dbdbd5937dff94cf7.jpg","https://telegra.ph/file/17bbcec651dd62658a9e7.jpg"] 



@app.on_message(filters.command("wallpaper") & ~filters.edited)
async def test_bot(bot: app, m: Message):
    start = time()
    replymsg = await m.reply_text("**❤ Rondom wallpaper Seçilir...**")
    end = round(time() - start, 2)
    photo = random.choice(photolist)
    text = f"❤️ **{Config.BOT_USERNAME} Sizin Üçün wallpaper Şəkil Seçdi**"
    await bot.send_photo(m.chat.id, photo=photo, caption=text)
    await replymsg.delete()