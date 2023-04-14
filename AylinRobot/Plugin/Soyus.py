from pyrogram import Client, filters

# Kaba kelimeler listesi
bad_words = ['göt', 'sikim', 'peysər', 'cındır', 'sikim', 'sik', 'cindir', 'peyser', 'məki', 'amcığ', 'blət', 'blə', 'qəhbə']


users = {}

# Mesajları filtreleme işlemi
@app.on_message(filters.text & ~filters.private)
async def filter_bad_words(client, message):
    for word in bad_words:
        if word in message.text.lower():
            # Mesajı atan kişinin kimliğini alın
            user_id = message.from_user.id
            # Küfür sayısını arttırın veya yeni bir kullanıcı ekleyin
            if user_id in users:
                users[user_id] += 1
            else:
                users[user_id] = 1
            # Küfür eden kişiye özel mesaj gönderin
            await client.send_message(chat_id=user_id, text="Küfür etmek uygun değil. Lütfen dikkatli olun. Toplam küfür sayınız: {}".format(users[user_id]))
            # Küfür içeren mesajı silin
            await message.delete()
            # Küfür eden kişiye qrupda sildiğini bildirin
            await client.send_message(chat_id=message.chat.id, text="{} isimli kullanıcının küfürlü mesajı silindi.".format(message.from_user.first_name))
