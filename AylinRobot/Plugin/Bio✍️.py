# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os, random
from random import choice
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from pyrogram import idle
from AylinRobot.config import Config
from pyrogram import Client, filters
from helpers.filters import command, other_filters

liste = [
"`Sana burada ekmek yok!`",
"`Beni tehdit eden yaşamadı.`",
"`Yaşamak yalvarmaya değecek bir şey değildir.`",
"`Köpek doğduysan köpek ölürsün; insan doğduysan insan ölürsün. Her ne olursan ol ölürsün.`",
"`Görevinive haddini aşan yerde susmayı öğren.`",
"`Tek kurşun beni öldürmeye yetmez.`",
"`Bu kapıya aç giren çok olur, aç çıkan hiç olmaz.`",
"`Terörle mücadele başka, teröristle mücadele başkadır.`",
"`Başımı itlere yediririm, sözümü kimseye yedirmem.`",
"`Kim sokakta ayakta kalmak istiyorsa sırtını sana dayayacak.`",
"`Geç gelen adalet, adalet değildir`",
"`Adam gör ki adam ol!`",
"`Yılanın başı dururken, solucanlarla mı uğraşacaksın.`",
"`İkimizin ortak olduğu bir işe üçüncüsü ancak azrail olur.`",
"`Bir insanı sevmem için beni sevmesi yetmez mi?`",
"`Hainin ne anası vardır ne babası...`",
"`İhaneti alkışlayamam, haini asla affedemem`",
"`Senin dostun bir ömür dostum, düşmanın bir ömür hasmımdır.`",
"`Gittiğim yerde ne zalim olsun, ne zulüm...`",
"`Bir taşta üç kuş vurmayacaksan, taşı hiç kaldırmayacaksın!...`",
"`Derdinle dertlenme, paylaş!`",
"`İhtiyar aslanla yaralı kurttan korkacaksın! Çünkü onlar hiç bir şeyden korkmaz.`",
"`Bu kadar ağır ceza kesersen, kimse seni hakem bellemez.`",
"`Söz bazen öyle faydasız oluyor ki insana hiç verilmese de olurdu.`",
"`Siyasetin konuşmadığı yer de silah konuşur.`",
"`Her şeye gücüm var kaderi değiştirecek gücüm yok...`",
"`Bu aleme girmek kolay çıkmak zordur.`",
"`Dostun dostumdur, düşmanın düşmanım.`",
"`Ben senin canın için ömrümü bir kibritin kavında tutuştururum. Ama benim yanmam senin gönlündeki ateşin sönmesini sağlamaz...`",
"`Bir yerde küçük insanların büyük gölgeleri oluşuyorsa, orada güneş batıyor demektir.`",
"`Her zaman mutluluğun doruğundayken gülünmez, bazen sırf hayata gıcıklık olsun diye uçurum kenarındayken bile gülümseyeceksin!`",
"`Benim hayatımda her şey yalan! Tek gerçek sensin.`",
"`Eğer birisi seni aldatmışsa bu onun suçudur. Eğer o kişi seni pek çok kere aldatmışsa bu senin suçundur.`",
"`Asla birilerinin umudunu kırma, belki de sahip oldukları tek şey o´dur.`",
"`Aynı dili konuşanlar değil, aynı duyguyu paylaşanlar anlaşabilir.`",
"`Hırs adamı dağıtır, böler. Büyütmez!`",
"`Hayatta edindiğim tecrübeler, yediğim kazıkların toplamıdır.`",
"`Yaşamak için yalvarmadık, ölmek için yalvarmayız`",
"`Ölenin arkasından ağlama ki, sen öldükten sonrada arkandan ağlıyan bırakma!!`",
"`Dağ kimi arxandayam deyib,Yarpax kimi əsənləridə çox gördük 🖤🍃`","`Allahdan qeyrisinə ümidvar olanı Allah elə onun ümidinə buraxar.(Hz. İmam Cavad)`","`susмuş вir qadın üçün...вiтмiş вir adaмsan.! 🖤`","`ᴛɪᴍᴇ ɴᴇᴠᴇʀ ᴄᴏᴍᴇs ᴀɢᴀɪɴ.⌛️`","`İ Do not Care😎`","`susмuş вir qadın üçün... вiтмiş вir adaмsan.! 🖤`","`You know my name , not my story`","ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sʜɪɴᴇ ʟɪᴋᴇ ᴛʜᴇ ᴍᴏᴏɴ, ғɪʀsᴛ ᴄᴏᴏʟ ʟɪᴋᴇ ᴛʜᴇ ᴍᴏᴏɴ. 🌘","ʙəʟᴋə ʜᴇç ᴋɪᴍ ᴏʟᴍᴀʏᴀᴄᴀǫ səɴɪɴ ᴋɪᴍɪ; ᴀᴍᴍᴀ səɴ ᴅə ᴏʟᴍᴀʏᴀᴄᴀǫsᴀɴ əᴠᴠəʟᴋɪ ᴋɪᴍɪ...✨","Makiyaj və üz boyalarınıza güvənməyin. Yollar da gözəldir, lakin altından kanalizasiya keçir.👋😉","`Kimsenin ilacı olmayın çünki insanlar iyileşince ilaç kullanmazlar..🍃`","ᴀɴʟᴀᴍᴀʏᴀɴ üçüɴ ᴄüᴍʟəʟəʀɪɴɪ, ǫəʟʙɪ ᴏʟᴍᴀʏᴀɴ üçüɴ ʜɪssʟəʀɪɴɪ ʏᴏʀᴍᴀ✨","Llove was a silence that only the one who loves you could understand🤍","`Sevgi yalnız səni sevənin anlaya biləcəyi bir sükut idi🤍`","`Çok güzel olduğum yetmezmiş gibi bir de çok zekiyim❤️‍🔥`","`Sizə mane olmağa çalışanlar, ən çox uğur qazana biləcəyinizə inananlar`","•𝙼𝚊𝚟𝚒 𝚋𝚒𝚛 𝚛𝚎𝚗𝚔𝚝𝚎𝚗 𝚏𝚊𝚣𝚕𝚊𝚜ı 𝚋𝚎𝚗𝚌𝚎, 𝚜𝚘𝚗𝚞 𝚘𝚕𝚖𝚊𝚢𝚊𝚗 𝚋𝚒𝚛 𝚐ö𝚔𝚢ü𝚣ü.𝚄𝚖𝚞𝚝 𝚍𝚘𝚕𝚞 𝚋𝚒𝚛 𝙳𝚎𝚗𝚒𝚣💙","`I don't want to need you. Because I know you can't be mine🌻`","`•My mind is a mess that I can't escape•🧠`","-ʜᴀʏᴀᴛ ᴋüçüᴋ şᴇʏʟᴇʀᴅᴇɴ ᴏʟᴜşᴜʀ, ᴇğᴇʀ sᴇɴ sᴇᴠᴇʀsᴇɴ ʙüʏüᴋ ᴏʟᴜʀʟᴀʀ.🤍🍃","𝙸'𝚖 𝚜𝚘 𝚝𝚑𝚊𝚗𝚔𝚏𝚞𝚕 𝚊𝚕𝚕 𝚝𝚑𝚎 𝚙𝚎𝚛𝚜𝚘𝚗 𝚠𝚑𝚘 𝚜𝚊𝚒𝚍 𝚖𝚎 𝚗𝚘, 𝙱𝙲 𝚘𝚏 𝚝𝚑𝚎𝚖 𝙸 𝚍𝚒𝚍 𝚒𝚝 𝚖𝚢𝚜𝚎𝚕𝚏🌚🌝","Herkesi kendim gibi sanamam, çünkü kimse ben gibi olamaz","`Hər gözəl qadın tərbiyəli ola bilməz. Hər tərbiyəli qadın gözəldi 🍂🧡`","𝐃𝐞𝐧𝐢𝐳𝐢 𝐌𝐚𝐯𝐢 𝐠ö𝐬𝐭𝐞𝐫𝐞𝐧 𝐠ö𝐤𝐲ü𝐳ü𝐝ü𝐫 𝐲𝐚 𝐡𝐚𝐧𝐢, 𝐛𝐞𝐧𝐢 𝐝𝐞 𝐦𝐮𝐭𝐥𝐮 𝐠ö𝐬𝐭𝐞𝐫𝐞𝐧 𝐬𝐞𝐧𝐬𝐢𝐧..💙","ʙᴇᴋʟᴇᴍᴇᴋ ʟᴀᴢɪᴍ...ɢöɴʟü ʜᴏş ᴛᴜᴛᴀɴɪ , ɢöɴüʟᴅᴇ ʏᴇʀ ᴛᴜᴛᴀɴɪ , ʙᴀşᴋᴀ ɢöɴüʟᴅᴇ ɢöᴢü ᴏʟᴍᴀʏᴀɴɪ.🤍✨","нəʀ ԍüɴ мəɴə sᴀʙᴀнιмsᴀɴ ᴅᴇʏəʀᴅιɴ ᴅüɴəɴιɴəм ᴅᴀнᴀ мəɴι ԍözʟəмə🥀","𝖲𝖾𝗏𝗆𝖾𝗄 𝗓𝖺𝗆𝖺𝗇 𝖺𝗒ı𝗋𝗆𝖺𝗄𝗍ı𝗋. 𝖡𝗈𝗌‌ 𝗓𝖺𝗆𝖺𝗇 𝖽𝗈𝗅𝖽𝗎𝗋𝗆𝖺𝗄 𝖽𝖾𝗀‌𝗂𝗅.🤍","`atacak kemiğin varsa, gelecek köpeğin çok olur..!😉`","`Güzel seven bütün insanlar yine yanlış kalplere kanacaklar💔😒☄️`","`Bir Duvara Bile Yankılanan Ses,İnsanın Yüreğine Değmiyor Bazen.🍂🖤`","`Senin bakışın! benim mirasım🗝`️","Sana bir kez baktım.Gözlerim başka bahçe görmez oldu..🍁🍂","Her Kese Bir Sinirim Vardı Ama Seni Görünce Gülerdim❤☘","aç dua sonra gelirsin bilmem ama ben ellerimi gökyüzüne feda ettim♥️","Gönlümün Muradı Olsun Yastığım Taştan Olsun..🕊🔐","`Benim hayelerim kelebeğin ömrü kadar yaşar 💔🥀`","İnsanı yaşı değil, yaşadıkları büyütür🖇️🍃","İNSANLARI TANIDIKÇA YALNIZLIĞI SEVDİM..🙂","SUSKUNLUĞUM NAMLUDAN ÇIKAN İLK MERMİ KADAR ACIMASIZ OLACAK","Acı Mühim Değilde Umut Yoruyor İnsanı....😒💔","Mesafe Dediğin Nedir ki Biz Allah'i Görmeden Sevmedik Mi 🕊","Başka Bedenlerde Terleyip Peşime Düşme Üşürsün.🌌","Ezan ile çağırana gitmezsen, dua ile çağırdığın sana gelir mi hiç✨","Allah'ım Ya Kavuşdur Yada Unutdur...🥀","Hayran'ım Hem Haddini Hem Rabbini Bilene...","Şu Dünyada Payıma Düşen En Güzel Şeysin..❤","Biz Sevmekle Yükümlüyüz Kavuşmak mı? Onu Allah Bilir..🌿","Pişman değilim, o gülüşü görsem yine yenik düşerim🍂🌒","`Ruhları Sevin Bedenler Çüreyecek...🍂🍂`","İnancımız Şudur: Dünya Yük Allah Büyük...","`Ben sekiz milyar insan içinde seni buldum sen ise 78 organımın içinde kalbimi bulamadınya o çok koyuyor be..🙂`","`kimseye hatır borcum yok ben zaten kahve sevmem..!🖤`","`Hep O Yapmaz Dediklerimiz Yüzünden Asla Yapmayacak Olanlara Da Güvenme`","`Allah bizi sevmeyenlerden değil, seviyomuş gibi yapanlardan korusun. 🐆`","`Hayalleri sana, seni duaya, duayı da Allah'a emanet ettim. 🔐❤️`","...αrαmízdα nє σlurѕα σlѕun. ѕєní tαnımıѕ̧ σlmαnın gєtírdíğí вαhαrı unutmαm...","Uyusak rüyalar kandırıyor uyansak insanlar🕊","`Kimseye güvenmiyorum güzel yazıyorlar güzel konuşuyorlar dil başka yürek başka`","Uçmayı Öğrenmeden Göçmeye Mecbur Kalmış Bir Kuş Gibi Kalbimiz.","`Zaman herşeyin ilacı değil, bunu bir mezara çiçek diktiğinde anlıyorsun...🥀`","`Güzel şeyler zaman alır dedik zaman güzel şeyleri aldı*` ","`Hayatta sahip olamayacağın şeye ikinci kez bakma şimdi profilden çıkabilirsin`","Herkese Aynı Değilim Beni Kimden Dinledin...🥀","Karanliktaysan gölgen bile seni yanlız bırakır.🖤🌙","`İyi Olan Herşey unutulur Sen beni Kötü Hatırla...🚬🥀`","`Güzeli güzel yapan edeptir edep ise güzeli sevmeye sebeptir🌼`","`Bir kurşun kalbimde senden daha onurlu durur`","`Ne Diyordu Şair Her Gecenin Yıldızına Dilek Tutulmaz...🕊`","`Ve sonra dediki kuru yaprak dala unutma yeşil günlerimizi 🍀`","Canımı Allah’ın alacağını biliyordum fakat kulunun nefesimi keseceği bilmiyordum","`Gecenin Karanlığını Aydınlatacak Kadar Parlak Hayatımız Olmadı..😏🍷🥂`","`Farklı olmak için degil, Mutlu olmak için yaşıyorum...🌹🙂`","`dönüşün umrumda bile değil benim derdim gidişindi...😒`","`♤...♡...♤ her saniyemiz ölüme giderken kolumuzdaki saatin fiyat'ının ne farkı var ♤...♡...♤`","unutma ki! senin küle çevirdiğin kalbe bir başkası üfleyerek can verdi 🥀🕊","Güçlüyüm... Çünkü başka seçeneğim yok düşersem tutanım olmayacak biliyorum...🚬","`Geçici insanlar kalıcı dersler verir🥀`","`Bu hayatta seni uzeni çıkartacasinki seni sevene yer açılsın 🔥🤍`","`Her sey görüldüğü gibi olsaydı eline aldığın deniz suyu mavi olurdu, kimse anlamadı susmayı tercih ettim`","İnsanları memnun etmek ulaşılmaz bir hedeftir, Allahı razı etmek ise terk edilmemesi gereken bir hedeftir","Hayaller de güzeldi yaşanabilseydi","`Dünya Hassas Kalpler İçin, Sadece Bir Cehennemdir🥀`","`Tüm şehri verseler umursamam da, o sokaktan geçerken duraksarim`","`Belki şair olamayacağım ama yaşadığım en güzel şiir sen olacaksın 🍁🌹`","`Soğuk kalpten güzel söz çıkmaz, beklemeyin incinirsiniz...🥀`","`UMARIM TERCİH ETTİKLERİN VAZGEÇTİKLERİNE DEĞER..!`","`Güzel çiçek açardıkda yanlış toprağa gömüldük`","`Affetdiklerimi ben yapsaydım,affetmezlerdi🙂`","`Çay içmek bile yoktu nasibimizde,Biz kalktık sevdalandık...🍂`","Bırak giden gitsin,silen silsin","`There s just too much that time cannot erase`","`Never lose you inner child`","`Hate is easy,love takes courage`","`Pain changes people`","`Life is empty`","`Time never comes again`","`Where there is love there is life`","`Love is the beauty of the soul`","ᴍᴇᴍᴏʀɪᴇs ʟᴀsᴛ ғᴏʀᴇᴠᴇʀ.✨","всегда есть выбор. 🐋","не доверяй никому.🐝","ɴᴇᴠᴇʀ ɢɪᴠᴇ ᴜᴘ. 👑","ᴛɪᴍᴇ ɴᴇᴠᴇʀ ᴄᴏᴍᴇs ᴀɢᴀɪɴ.⌛️","ʟᴀ ᴘᴀɪx ᴄᴏᴍᴍᴇɴᴄᴇ ᴀᴠᴇᴄ ᴜɴ sᴏᴜʀɪʀᴇ.","ᴇᴠᴇʀʏᴛʜɪɴɢ ʏᴏᴜ ᴄᴀɴ ɪᴍᴀɢɪɴᴇ ɪs ʀᴇᴀʟ.","ɪ ɴᴇᴠᴇʀ ʟᴏsᴇ.🗽","ᴅᴏɴ’ᴛ ᴅʀᴇᴀᴍ, ʟɪᴠᴇ ʏᴏᴜʀ ᴅʀᴇᴀᴍ. 🐊","ɪ ɴᴇᴠᴇʀ ʟᴏsᴇ.🗽sɪʟᴇɴᴄᴇ ɪs ʙᴇᴛᴛᴇʀ ᴛʜᴀɴ ʟɪᴇs.🕊","ᴀᴅᴠᴇɴᴛᴜʀᴇs ғɪʟʟ ʏᴏᴜʀ🪐","ʟ’ɪᴍᴍᴀɢɪɴᴀᴢɪᴏɴᴇ ᴛɪ ᴘᴏʀᴛᴇʀà ᴏᴠᴜɴǫᴜᴇ.🎡","sɪʟᴇɴᴄᴇ ɪs ᴛʜᴇ ʟᴀɴɢᴜᴀɢᴇ ᴏғ ɢᴏᴅ, ᴀʟʟ ᴇʟsᴇ ɪs ᴘᴏᴏʀ ᴛʀᴀɴsʟᴀᴛɪᴏɴ. ☔️","ʟɪᴠᴇ ᴛᴏɢᴇᴛʜᴇʀ, ᴅɪᴇ ᴀʟᴏɴᴇ.🤍","ᴅᴏɴ’ᴛ ʙᴇ sᴄᴀʀᴇᴅ ᴏғ ʏᴏᴜʀ sʜᴀᴅᴏᴡ, ʏᴏᴜ ᴄᴀɴ’ᴛ ʜɪᴅᴇ ғʀᴏᴍ ʏᴏᴜʀ sᴏʀʀᴏᴡ.🌒","ғɪɴᴄʜé ᴄ’è ᴠɪᴛᴀ ᴄ’è sᴘᴇʀᴀɴᴢᴀ.🐞","ʟᴇ ғᴀɪʙʟᴇ ɴᴇ ᴘᴇᴜᴛ ᴊᴀᴍᴀɪs ᴘᴀʀᴅᴏɴɴᴇʀ.🦦","ᴛᴏ ᴋᴇᴇᴘ ʏᴏᴜʀ ʙᴀʟᴀɴᴄᴇ, ʏᴏᴜ ᴍᴜsᴛ ᴋᴇᴇᴘ ᴍᴏᴠɪɴɢ. ⚖️","ʟɪғᴇ ɪs ᴛʜᴇ sᴜᴍ ᴏғ ᴀʟʟ ʏᴏᴜʀ ᴄʜᴏɪᴄᴇs. 🌊","ᴀʟᴡᴀʏs ɢɪᴠᴇ ʏᴏᴜʀ ʙᴇsᴛ ɴᴇᴠᴇʀ ᴡᴏʀʀʏ ғᴏʀ ʀᴇsᴜʟᴛs.⚡️","ᴅᴏɴ’ᴛ ᴡᴀsᴛᴇ ʏᴏᴜʀ ᴛɪᴍᴇ ᴡɪᴛʜ. 💦","`Tell the truth and then run.🌞`","`Time never comes again.`","`Keep your eyes on the stars, and your feet on the ground.💫`","`Silence is the most powerful scream.`","`If you fell down yesterday, stand up today`","`It’s hard to beat a person who never gives up.`","`Heyf ki, gerçək hiss’ləri yanlış insan’larda yaşadıq.🌓`","`Gəl, yaralarımı sar,ama məlhəmi sevgin olsun..🌓`","Çiçəklərə aşağıdan baxmağa gedirəm..➰","Bir nəfəs qədər uzaqda..","ʜᴀʀᴀ ɢᴇᴛᴅɪʏɪɴɪ ʙɪʟᴍɪʀsəɴsə,ʜᴀɴsɪ ʏᴏʟᴅᴀɴ ɢᴇᴛᴍəʏɪɴɪɴ əʜəᴍɪʏʏəᴛɪ ʏᴏxᴅᴜ.➰","Mən susum, Sən anla..,olar mı.. ?✨","Yuxuya sənin səsin’lə getmək varkən,neynirəm musiqini.. 🤍🌚","Acı hiss edilmək istər.. ✨","ʜəʏᴀᴛɪᴍɪᴢ ɴᴀɢɪʟʟᴀʀᴅᴀᴋɪ ᴋɪᴍɪ ɪᴅɪ.ᴀᴍᴍᴀ ʙɪᴢ ɴᴀɢɪʟʟᴀʀɪɴ.. əꜱʟ ʜᴇᴋᴀʏəʟəʀɪɴɪ ʙɪʟᴍɪʀᴅɪᴋ. 🪄","Səni anlayıram.. deyənlərə not:Hissedəmədiyin şeyi anlaya bilməzsən. ➰","ƏƏgər Sevgi yalandırsa,Acısı nədən bu qədər gerçək.. ¿ ➰","Önəmli olan İlk dəfə deyil də, Son dəfə sevə bilmək..➰","Ruhum qaranlıq.➰","Hərkəs bir şəkildə yoluna davam edir,Mən yol’u tapa bilmirəm","Biri’nin huzuruna sarılmaq.. 🤍","Yorğun ruhuma huzur’Sən..💜","Hər şey keçər..Amma heç bir şey keçməyəcək. 🐡","ümidin bitdiyi yerdə deyil də, acıların başladığı yerdə çiçəklər açar.. ✨","Hiss edilən hər şeyə cümlə qurmaq olmur.. 🪐","Bəzən pis şeylər tez bitər,daha pis şeylər başlasın deyə.. ☄️","`Bəzi şeylər bitər,Amma xatirələr sonsuzadək qalar.`","`Kəlimələrdən daha ağırdır,Səssizliyin yükü..`","Mənim içimdəki çiçəklər artıq bir başqasına açamayacaq qədər soldu..➰","Yarına kalır, yanına kalmaz. ➰"]

@app.on_message(command("bio") & ~filters.edited)
async def bio(bot: Client, msg: Message):
    await msg.reply(random.choice(liste))