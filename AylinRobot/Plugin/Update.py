import os
import re
import sys
import asyncio
import subprocess
from asyncio import sleep
from AylinRobot import AylinRobot as app
from git import Repo
from pyrogram.types import Message
from helpers.filters import command
from pyrogram import Client, filters
from os import system, execle, environ
from git.exc import InvalidGitRepositoryError
from AylinRobot.config import Config


def gen_chlog(repo, diff):
    upstream_repo_url = Repo().remotes[0].config_reader.get("url").replace(".git", "")
    ac_br = repo.active_branch.name
    ch_log = tldr_log = ""
    ch = f"<b>updates for <a href={upstream_repo_url}/tree/{ac_br}>[{ac_br}]</a>:</b>"
    ch_tl = f"updates for {ac_br}:"
    d_form = "%d/%m/%y || %H:%M"
    for c in repo.iter_commits(diff):
        ch_log += (
            f"\n\n💬 <b>{c.count()}</b> 🗓 <b>[{c.committed_datetime.strftime(d_form)}]</b>\n<b>"
            f"<a href={upstream_repo_url.rstrip('/')}/commit/{c}>[{c.summary}]</a></b> 👨‍💻 <code>{c.author}</code>"
        )
        tldr_log += f"\n\n💬 {c.count()} 🗓 [{c.committed_datetime.strftime(d_form)}]\n[{c.summary}] 👨‍💻 {c.author}"
    if ch_log:
        return str(ch + ch_log), str(ch_tl + tldr_log)
    return ch_log, tldr_log


def updater():
    try:
        repo = Repo()
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", UPSTREAM_REPO)
        origin.fetch()
        repo.create_head("main", origin.refs.main)
        repo.heads.main.set_tracking_branch(origin.refs.main)
        repo.heads.main.checkout(True)
    ac_br = repo.active_branch.name
    if "upstream" in repo.remotes:
        ups_rem = repo.remote("upstream")
    else:
        ups_rem = repo.create_remote("upstream", UPSTREAM_REPO)
    ups_rem.fetch(ac_br)
    changelog, tl_chnglog = gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    return bool(changelog)


@Client.on_message(command(["update", f"update@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def update_repo(_, message: Message):
    chat_id = message.chat.id
    msg = await message.reply("🔄 `Akış işleniyor...`")
    update_avail = updater()
    if update_avail:
        await msg.edit("✅ Yeniləmə tamamlandı\n\n• bot yenidən işə salındı, 1 dəqiqələr ərzində yenidən aktivləşir..")
        system("git pull -f && pip3 install --no-cache-dir -r requirements.txt")
        execle(sys.executable, sys.executable, "main.py", environ)
        return
    await msg.edit(f"bot **güncel** [main]({UPSTREAM_REPO}/tree/main)", disable_web_page_preview=True)


@app.on_message(command(["restart"]) &(Config.OWNER_ID)& ~filters.edited)
async def restart_bot(_, message: Message):
    msg = await message.reply("`Botu yenidən başladın...`")
    args = [sys.executable, "AylinRobot"]
    await msg.edit("✅ bot yenidən işə salındı\n\n• indi bu botu yenidən istifadə edə bilərsiniz.")
    execle(sys.executable, *args, environ)
    return
