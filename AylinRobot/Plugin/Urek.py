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
    m = msj
    a = client.send_message(chat_id, f"💙💚💛💜🤍🤎♥️")
    time.sleep(1.6)
    w = a.edit('💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️')
    time.sleep(1.6)
    z = w.edit('💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️')
    time.sleep(1.6)
    t = z.edit('💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️')
    time.sleep(1.6)
    g = t.edit('💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️')
    #time.sleep(1.6)
    #son = g.edit('💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️\n💙💚💛💜🤍🤎♥️')
    time.sleep(0.7)
    client.delete_messages(chat_id, g.id)
    client.send_message(chat_id, f"{random.choice(urekler)}")