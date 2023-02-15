import os
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters
from AylinRobot.config import Config
import random
from pyrogram.errors import FloodWait
from AylinRobot.sorular import D_LİST, C_LİST
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# ============================ #
MOD = None

def d_or_c(user_id):
	BUTTON = [[InlineKeyboardButton(text="Doğruluq", callback_data = " ".join(["d_data",str(user_id)]))]]
	BUTTON += [[InlineKeyboardButton(text="Cəsarət", callback_data = " ".join(["c_data",str(user_id)]))]]
	return InlineKeyboardMarkup(BUTTON)

@app.on_message(filters.command("dc"))
async def _(client, message):
	user = message.from_user

	await message.reply_text(text="{} Doğruluq yoxsa cəsarət!".format(user.mention),
		reply_markup=d_or_c(user.id)
		)

# Buttonlarımızı Yetkilendirelim
@app.on_callback_query()
async def _(client, callback_query):
	d_soru=random.choice(D_LİST)
	c_soru=random.choice(C_LİST)
	user = callback_query.from_user 

	c_q_d, user_id = callback_query.data.split()

	if str(user.id) == str(user_id):
		if c_q_d == "d_data":
			await callback_query.answer(text="Siz doğruluğu seçdiz\n", show_alert=False)
			await client.delete_messages(
				chat_id=callback_query.message.chat.id,
				message_ids=callback_query.message.message_id)

			await callback_query.message.reply_text(f"**{user} doğruluq sualın gəldi!:**\n\n__{d_soru}__".format(user=user.mention, d_soru=d_soru)) # Sonra Kullanıcıyı Etiketleyerek Sorusunu Gönderelim
			return

		if c_q_d == "c_data":
			await callback_query.answer(text="Cesaret Sorusu İstediniz", show_alert=False)
			await client.delete_messages(
				chat_id=callback_query.message.chat.id,
				message_ids=callback_query.message.message_id)
			await callback_query.message.reply_text(f"Siz cəsarət seçdiz\n__{c_soru}__".format(user=user.mention, c_soru=c_soru))
			return


	else:
		await callback_query.answer(text="Bu əmri sən verməmisən!!", show_alert=False)
		return

############################
@app.on_message(filters.command("cet"))
async def _(client, message):
  global MOD
  user = message.from_user
  
  if user.id not in {Config.OWNER_ID}:
    await message.reply_text("**Sən bot sahiblsən deyilsən!!**")
    return
  MOD="cet"
  await message.reply_text("**Əlavə etmək istədiyiniz sualı yazın!!**")
  
@app.on_message(filters.command("det"))
async def _(client, message):
  global MOD
  user = message.from_user
  
  if user.id not in  {Config.OWNER_ID}:
    await message.reply_text("**Sən bot sahiblsən deyilsən!!**")
    return
  MOD="cet"
  await message.reply_text("**Əlavə etmək istədiyiniz sualı yazın!!**")

@app.on_message(filters.group)
async def _(client, message):
  global MOD
  global C_LİST
  global D_LİST
  
  user = message.from_user
  
  if user.id in {Config.OWNER_ID}:
    if MOD=="cet":
      C_LİST.append(str(message.text))
      MOD=None
      await message.reply_text("**Sən bot sahiblsən deyilsən!!**")
      return
    if MOD=="det":
      C_LİST.append(str(message.text))
      MOD=None
      await message.reply_text("**Əlavə etmək istədiyiniz sualı yazın!!**")
      return