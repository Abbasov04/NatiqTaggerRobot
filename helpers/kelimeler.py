import random

kelimeler = ["gözəl ","bilmək ","sual","sağalmaq ","getmək","zaman","su","yarmaq","dəli","görmək",

             "yenidən", "çox", "fakt", "pul", "oynamaq", "çiçək", "şəhər", "yüksəlmək", "döyüş", "varlıq", "etmək",

             "güvən", "lazım", "müalicə", "bir", "rahat", "soyuq", "orası", "kitab", "paylaşmaq", "hesap", "bədən",

             "torpaq", "üzəri", "sistem", "xoş", "çəkilmək", "texnik", "yaxınlaşmaq", "ilbiz", "tarix", "kəsir", "bacı",

             "incə", "deyər", "oyda", "qarşılıqlı","vermək", "sahib", "artıq", "kişi", "diyar", "dönəm", "yenə", "bunlar",

             "kitab", "xəta", "tapmaq", "siz", "dövlət", "qabaq", "enerji", "baxmaq", "xiyar", "oyun", "baş", "başlamaq",

             "tutmaq", "birbiri", "heçbir", "yatmaq", "su", "ürək", "hal", "doğru", "orta", "başqa", "böyük", "etmək",

             "yeni", "çoxlu", "soruşmaq", "onlar", "açmaq", "həmin", "həsən", "sükan", "ağlamaq", "dəli", "saat", "fəsil",

             'birlik', 'veteran', 'olmak', 'buzlu', 'içki', 'onuncu', 'bibar', 'demək', 'çox', 'yaşıl', 'aylıq', 'kimi', 'daha', 'almaq',

             'final', 'yalnız', 'gəlmək', 'illik', 'vermək', 'baba', 'sonra', 'qədir', 'yer', 'ata', 'insan', 'deyil', 'hər',

             'istəmək', 'ilan', 'çıxmaq', 'görmək', 'gün', 'biz', 'getmkə', 'iş', 'ölüm', 'axtarmaq', 'eltun', 'bilmək', 'əl', 'zaman',

             'yarasa', 'uşaq', 'ilkin', 'baxmaq', 'işləmək', 'içində', 'böyük', 'yox', 'başlamaq', 'yol', 'düzgün', 'feil', 'siz',

             'söz', 'yaradmaq', 'yaxşı', 'qadın', 'evli', 'demək', 'tapmaq', 'demək', 'gözlük', 'lazımlı', 'dünya',

             'baş', 'vaxt', 'məclis', 'getmək', 'sən', 'onlar', 'yeni', 'öncə', 'başqa', 'hell', 'orta', 'susuz', 'girmək', 'ölkə',

             'yemək', 'heçnə', 'oxumaq', 'necə', 'bütün', 'qarşı', 'tapmaq', 'evli', 'yaşamaq', 'yuxari', 'güzgü', 'içmək', 'ancaq',

             'kişi', 'bunlar', 'ağrı', 'ilk', 'göre', 'qabaq', 'son', 'biri', 'şəkil', 'önemli', 'yüz', 'həmin', 'göstərmək', 'etmək',

             'qızıl', 'gətirmək', 'işlətmək', 'çünkü', 'tərəf', 'kimdi', 'adam', 'onun', 'ciyar', 'artıq', 'ütüntə', 'səs', 'könül',

             'düzgün', 'dayanmaq', 'qız', 'hamsı', 'süd', 'zəng', 'pullu', 'başadüşməy', 'nanə', 'qoşqar', 'bazar', 'baba', 'həyat',

             'sadece', 'balaca', 'çox', 'bilgi', 'an', 'soruşma', 'bunun', 'qoyun', 'yemək', 'sağalmaq', 'kəsir', 'eynək', 'diş',

             'üzmək', 'yəni', 'vaxt', 'qayıtmaq', 'açmaq', 'oturmaq', 'salmaq', 'buraxmaq', 'həmən', 'saat', 'yaş', 'xəta', 'dövlət',

             'sahib', 'sıra', 'yazmağ', 'yüzdə', 'ayan', 'çalmaq', 'tutmaq', 'burun', 'qəza', 'yarı', 'qulaq', 'söz', 'gözəl',

             'sevmek', 'biraz', 'çətin', 'çıxmaq', 'suni', 'qoymaq', 'tək', 'sistem', 'toplu', 'vergi', 'kim', 'incimək', 'gənc',

             'qapı', 'kitab', 'üstün', 'burada', 'gecə', 'alan', 'bərbər', 'içki', 'gizli', 'uzun', 'kainat', 'bugün', 'fokus',

             'dost', 'soyad', 'aile', 'üç', 'oxumaq','kişi', 'hərkəs', 'güc', 'bəlmək', 'doğru', 'tam', 'gecə', 'Riyad',

             'çevrə', 'köhnə', 'zəng', 'yaşma', 'əhali', 'yaxın', 'yol', 'bəy', 'tarix', 'özellik', 'bölüm', 'şəxsi', 'ağıl',

             'kimsə', 'pak', 'baş', 'gerek', 'yaxın', 'anlamaq', 'yuxarı', 'banka', 'infakt', 'ayağ', 'daşımaq', 'geri', 'toplu',

             'maşın', 'maddə', 'Azərbaycan', 'qəlyan', 'görüldü', 'hava', 'sayı', 'başqa', 'qrup', 'otaq', 'bacı', 'dolmaq', 'xəbər',

             'allah', 'ayrıca', 'gələn', 'çin', 'sual', 'arxa', 'qazanmaq', 'yazı', 'dərs', 'açıq', 'öyrənmək', 'sürmək',

             'dil', 'şirkət', 'qaynaq', 'bitmək', 'program', 'dəvamətmək', 'hərəkət', 'rəng', 'açılmaq', 'hak', 'inanmaq',

             'çalmaq', 'zaman', 'mahnı', 'qazet', 'yaratmaq', 'yaxşı', 'dəyər', 'tanımaq', 'kley', 'doxdur', 'gəlir',

             'hərbiçi', 'zəfər', 'dünya', 'kino', 'üzere', 'satıcı', 'zolaq', 'telefon', 'aydın', 'dəniz', 'ikinci',

             'qalxmaq', 'düzgün', 'qarlı', 'gəlir', 'keçən', 'boyun', 'düşüncə', 'milyon', 'oynamaq', 'dəyişmək', 'tütün',

             'yaratmaq', 'xallı', 'fikir', 'keçmək', 'söyüş', 'qurmaq', 'fakt', 'buna', 'rəsim', 'ışıq', 'içmək',

             'xanım', 'xəstə', 'ehtiyac', 'nöktə', 'yönlü', 'xəta', 'oyun', 'artmağ', 'yenidən', 'şar', 'qısa', 'asta',

             'şan', 'qan', 'əsla', 'ağıl', 'orada', 'diqqət', 'uzaq', 'bilgisayar', 'gələcək', 'görünmək',

             'şəkil', 'oğul', 'dinləmək', 'uyğun', 'manat', 'passiv', 'dəqiq', 'unutmaq', 'cəld', 'eynək', 'pis',

             'maşın', 'ağız', 'dünya', 'uygulamak', 'xala', 'nümunə', 'azlıq', 'baxmaq', 'dərəcə', 'mümkün', 'dondurma',

             'divar', 'onsuz', 'sənə', 'ana', 'xəstəlik', 'şagird', 'televizor', 'kino', 'stul', 'ölmək', 'taksi', 'üst',

             'baş', 'mahnı', 'sevgi', 'enerji', 'Universtet', 'qaçmağ', 'hərşey', 'cansız', 'balta', 'soyuducu', 'ölüm',

             'dərdli', 'sağlam', 'inək', 'banan', 'hissetmek', 'nənə', 'sabah', 'internet', 'texnik', 'dondurma',

             'mərkəz', 'orta', 'yerinə', 'düz', 'kənd', 'yorulmaq', 'aşağı', 'cavab', 'yatmaq', 'torpaq', '', 'axşam',

             'sarı', 'götürmek', 'qatılmaq', 'yoxsul', 'qurmaq', 'ödəmək', 'sanki', 'qarın', 'xəstə', 'şəhər', 'qalxmaq',

             'qara', 'qaynaq', 'həftə', 'işığ', 'hesab', 'lətif', 'başqa', 'davranış', 'mətbəx', 'kənd', 'bazar',

             'vacib', 'ayrı', 'qiymət', 'hakkında', 'qaldırmaq', 'kola', 'tək', 'hazırlamaq', 'Şüşə', 'sonunda', 'yavaş',

             'lazım', 'dəyər', 'arvad', 'yallı', 'varlı', 'tar', 'arı', 'təkcə', 'satış', 'içəri', 'qoğal', 'məhkum',

             'şənlik', 'acı', 'xeyir', 'qorumaq', 'qat', 'ekonomi', 'hamı', 'bildirmək', 'şəkər', 'heyvan', 'sarğı',

             'yumurta', 'alma', 'plan', 'istəmək', 'kərim', 'kriz', 'birlik',

             'qapanmaq', 'Kənan', 'Kəmalə', 'Nilay', 'Əli', 'Elməddin', 'Zeynəb', 'Zəhra', 'Qruz',

             ]

def kelime_sec():

    return random.choice(kelimeler)
