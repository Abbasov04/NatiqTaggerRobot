import os, wget, speedtest
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters
from pyrogram.types import Message
from AylinRobot.config import Config

def bytes(size: float) -> str:
    """humanize size"""
    if not size:
        return ""
    power = 1024
    t_n = 0
    power_dict = {0: " ", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        t_n += 1
    return "{:.2f} {}B".format(size, power_dict[t_n])


@app.on_message(filters.command("speedtest") & filters.user(Config.OWNER_ID))
async def statsguwid(_, message):
    m = await message.reply_text("⚡️ Sürət testi")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = await m.edit("⚙️ Sürət Testini yükləyin")
        test.download()
        m = await m.edit("🔄 Yükləmə Sürət Testi işləyir")
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        return await m.edit(e)
    m = await m.edit("📥 SpeedTest Nəticələrinin Paylaşılması")
    path = wget.download(result["share"])

    output = f"""**📊 Speedtest Nəticələri**
    
<u>**Müştəri:**</u>
**__ISP:__** {result['client']['isp']}
**__Ölkə:__** {result['client']['country']}
  
<u>**Server:**</u>
**__Ad:__** {result['server']['name']}
**__Ölkə:__** {result['server']['country']}, {result['server']['cc']}
**__Sponsor:__** {result['server']['sponsor']}
**__Gecikmə:__** {result['server']['latency']}  
**__Ping:__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=path, caption=output
    )
    os.remove(path)
    await m.delete()
