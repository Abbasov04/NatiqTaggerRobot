import time
from asyncio import sleep
from time import time
from random import choice
from AylinRobot import AylinRobot as app
from pyrogram import filters
from pyrogram import Client, filters




@app.on_message(filters.command("urek"))
async def startFunc(client, msj):
    chat_id = msj.chat.id
    urekler = ['💙','💚','💛','💜','🤍','🤎','♥️']
    m = await msj
    a = await client.send_message(chat_id, f"💙💚💛💜🤍🤎♥️")
    await sleep(1.6)
    w = await a.edit('💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️')
    await sleep(1.6)
    z = await w.edit('💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️')
    await sleep(1.6)
    t = await z.edit('💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️')
    await sleep(1.6)
    g = await t.edit('💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️')
    #time.sleep(1.6)
    #son = g.edit('💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️')
    await sleep(0.7)
    client.delete_messages(chat_id, g.id)
    client.send_message(chat_id, f"{random.choice(urekler)}")