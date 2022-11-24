

# Isim/Soyisim	R	I	A	S	E	C
neferler = {
    "Ulviyya Allahverdiyeva":[4,7,4,2,2,2],
    "Selale Tahirzade":[3,7,3,5,4,3],
    "Aysel Cabbarova":[2,6,3,4,6,7],
    "Emir Elekberli":[4,6,3,5,2,4],
    "Xaqani Qasimov":[0,7,6,5,5,3],
    "Elmar Qarayev":[3,2,0,3,1,2],
    "Vefa Ibrahimova":[1,6,2,5,2,3],
    "Lale Memmedova":[5,6,3,6,4,3],
    "Lamiye Agayeva":[2,5,3,4,4,4],
    "Kamilla Salbazova":[2,7,4,5,4,5],
    "Musfiq Ibazade":[3,5,3,3,4,4],
    "Ruhangiz Qurbanova":[4,7,5,5,3,3],
    "Murad Eleddinzade":[5,6,2,5,5,4]
}

def benzerlik( nefer1, nefer2 ):
    #birinci = [4, 6, 3, 5, 2, 4]
    #ikinci =  [5, 2, 5, 5, 2, 4]

    total = 0
    for i in range(6):
        #FARKLILIK_DISTANCE_DIFFERENCE = abs(nefer1[ i ] - nefer2[ i ])
        FARKLILIK_DISTANCE_DIFFERENCE = 1 if nefer1[i] != nefer2[i] else 0

        total = total + FARKLILIK_DISTANCE_DIFFERENCE

    if total == 0: return 1000000
    return 1 / total

for i1 in neferler:
    for i2 in neferler:
        if i1 != i2:
            print(i1, i2, benzerlik( neferler[i1], neferler[i2] ))




haber = """

Paytaxtda sıxlıq olan küçə və prospektlər açıqlanıb.

Nəqliyyatın İntellektual İdarəetmə Mərkəzindən verilən xəbərə görə, sıxlıq olan yollar aşağıdakılardır:

1. Bakı-Sumqayıt şosesi, “20 Yanvar” metro stansiyası istiqamətində;

2. Binəqədi şosesi, “Azadlıq Prospekti” metro stansiyası istiqamətində;

3. Ziya Bünyadov prospekti, Müzəffər Nərimanov küçəsi ilə kəsişmədən “20 Yanvar” metro stansiyası istiqamətində;

4. Əbdülvahab Salamzadə küçəsi, Ziya Bünyadov prospekti istiqamətində;

5. “20 Yanvar” dairəsində;

6. Tbilisi prospekti, “20 Yanvar” metro stansiyasından mərkəz istiqamətində;

7. Koroğlu Rəhimov küçəsi, Gülarə Qədirbəyova küçəsindən Akademik Həsən Əliyev küçəsi istiqamətində;

8. Heydər Əliyev prospekti, “Koroğlu” Paytaxtda sıxlıq metro stansiyasının qarşısı əsas və köməkçi yol, mərkəz istiqamətində;

9. Üzeyir Hacıbəyli küçəsi, Cavanşir körpüsündən Azadlıq prospekti ilə kəsişməyə qədər;

10. Afiyəddin Cəlilov küçəsi, Yusif Səfərov küçəsi istiqamətində;


11. Babək prospekti, mərkəz istiqamətində.
Şimali Atlantika Alyansının təyyarəsi Polşa ərazisinə düşən raketlərin trayektoriyasını izləyə bilib.

Kəşfiyyat məlumatları NATO və Polşaya təqdim edilib. Lakin raketlərin buraxılış yeri barədə məlumat verməyib.

Raketləri izləyən təyyarə çərşənbə axşamı Ukrayna ərazisi ətrafında müntəzəm kəşfiyyat uçuşu həyata keçirib və Polşa ərazisi üzərində uçub.

Polşa Xarici İşlər Nazirliyi çərşənbə axşamı ölkənin şərqindəki Pşevoduv kəndi ərazisinə Rusiya istehsalı olan raketlərin düşməsi nəticəsində iki nəfərin həlak olması ilə bağlı məlumat yayıb.

Eyni zamanda, respublika Prezidenti Andjey Dudanın sözlərinə görə, sursatların hara aid olduğu hələ müəyyən edilməyib. Öz növbəsində ABŞ Prezidenti Co Bayden qeyd edib ki, Polşaya düşən raketlərin Rusiyadan atıldığı barədə iddiaları təkzib edən ilkin məlumatlar var. Onun sözlərinə görə, trayektoriya nöqteyi-nəzərindən onun Rusiyadan buraxılması ehtimalı azdır.
Futbol üzrə Azərbaycan milli komandası bu gün yoldaşlıq oyunu keçirəcək.

Oxu.Az xəbər verir ki, 2024-cü il Avropa çempionatının seçmə mərhələsinə hazırlıq xarakteri daşıyan matçda rəqib Moldova yığması olacaq.

Kişineudakı “Zimbru” stadionunda oynanılacaq görüş Bakı vaxtı ilə saat 21:00-da başlayacaq. Qarşılaşmanı ukraynalı FIFA referisi Denis Şurman idarə edəcək.

Bu, iki kollektiv arasında sayca 12-ci oyun olacaq. Əvvəlki 11 görüşün 2-də Azərbaycan, 4-də Moldova qələbə qazanıb. 5 matçda isə qalib müəyyənləşməyib.

Yoldaşlıq oyunu

16 noyabr

21:00. Moldova - Azərbaycan

Hakimlər: Denis Şurman, Aleksandr Jukov, Viktor Nijnik, Roman Jitari (Ukrayna)

Kişineu, “Zimbru” stadionu

Qeyd edək ki, Azərbaycan millisi noyabrın 20-də isə Şimali Makedoniyanın qonağı olacaq.
Noyabrın 15-i saat 21:40-da Ermənistan silahlı qüvvələrinin bölmələri Basarkeçər rayonunun Yuxarı Şorca yaşayış məntəqəsi istiqamətində yerləşən mövqelərindən Ordumuzun Kəlbəcər rayonunun Mollabayramlı yaşayış məntəqəsi istiqamətində yerləşən mövqelərini atıcı silahlardan atəşə tutub.

Bununla bağlı Azərbaycan Müdafiə Nazirliyi məlumat yayıb.

Bundan başqa, Azərbaycan Ordusunun Ağdam rayonu ərazisində yerləşən mövqeləri də noyabrın 16-sı saat 00:50-də Rusiya sülhməramlılarının müvəqqəti yerləşdiyi Azərbaycan ərazisindəki qeyri-qanuni erməni silahlı dəstəsinin üzvləri tərəfindən atəşə tutulub.

Azərbaycan Ordusunun qeyd olunan istiqamətlərdə yerləşən bölmələri tərəfindən adekvat cavab tədbirləri görülüb.
“15 noyabr 2022-ci il tarixində Fransa Senatında qəbul edilmiş “Azərbaycana qarşı sanksiyaların tətbiqi və onun Ermənistan ərazisindən dərhal geri çəkilməsi, 9 noyabr 2020-ci il tarixli atəşkəs razılaşmasına riayət etməsi tələbi və iki ölkə arasında dayanıqlı sülhün bərqərar olmasına yönəlmiş bütün təşəbbüslərin təşviq edilməsi” adlı qətnamə tamamilə həqiqətdən uzaqdır, yalan və iftira dolu müddəaları əks etdirir və açıq təxribat xarakteri daşımaqla Azərbaycanla Ermənistan arasında münasibətlərin normallaşması prosesinə xələl gətirilməsinə xidmət edir”.

Azərbaycan Xarici İşlər Nazirliyindən (XİN) verilən məlumatda bildirilir ki, Senat tərəfindən qəbul edilən və hər hansı hüquqi qüvvəyə malik olmayan bu qətnamə, sülh prosesinə öz töhfəsini vermək niyyətini bəyan etmiş ölkə kimi Fransanın növbəti dəfə qərəzli və birtərəfli siyasi mövqeyini bariz şəkildə nümayiş etdirir.

“Ümumiyyətlə, qətnamədə qeyd edilən və reallıqlardan uzaq iddialar onun müəlliflərinin tarixi faktlardan və bölgədəki hazırkı vəziyyətdən xəbərsiz olmasını göstərir.

Təəssüflə vurğulayırıq ki, Fransa parlamentinin yuxarı palatasının qətnaməsində növbəti dəfə Azərbaycanın ərazilərinin 30 ilə yaxın bir müddətdə Ermənistan tərəfindən işğalı, mülki əhaliyə qarşı törədilmiş qırğınlar, şəhər və kəndlərin talan edilməsi, yüzminlərlə məcburi köçkünlərin hüquqlarının qəddarcasına tapdanması, Ermənistanın Azərbaycanın tarixi torpaqlarında etnik təmizləmə siyasəti həyata keçirməsi, habelə 2020-ci il Vətən müharibəsindən sonra Azərbaycanın sülh quruculuğu, bərpa və yenidənqurma işləri ilə bağlı faktlar göz ardına alınır.

Qətnamədə “Dağlıq Qarabağ” adlandırılan qondarma qurumla bağlı cəfəng fikirlərlə əlaqədar senatorlara bir daha xatırladırıq ki, Azərbaycanın beynəlxalq səviyyədə tanınan ərazisi olan Qarabağ bölgəsi Azərbaycanın ayrılmaz tərkib hissəsidir, bu bölgədə yaşayan erməni əsilli əhalinin hüquqları və təhlükəsizliyi Azərbaycanın daxili məsələsidir və bunlar Azərbaycan Respublikasının Konstitusiyasına uyğun olaraq təmin ediləcək.

Senatın bu qətnaməsi Ermənistandakı revanşist qüvvələri həvəsləndirməklə, bölgədə sülh, sabitlik və tərəqqiyə xidmət etmir və qətnamənin adında qeyd olunduğu “dayanıqlı sülhün təşviq edilməsindən” çox uzaqdır.

Fransa Senatı tərəfindən qəbul edilmiş bu növbəti qətnaməni qətiyyətlə rədd edirik”, - deyə XİN-dən bildirilib.
FİFA 2022-ci ildə Qətərdə keçiriləcək Dünya Çempionatı üçün bütün milli komandaların heyətlərini təsdiqləyib.

Qarşıdan gələn Dünya Çempionatının ən yaşlı oyunçusu Meksika millisinin hazırda 40 yaşı olan qapıçısı Alfredo Talavera olacaq.

Mundialın ən yaşlı futbolçuların ilk beşliyi aşağıdakı adlardan ibarətdir:

1. Alfredo Talavera - 40 yaş (18.09.1982), Meksika millisi;

2. Atiba Hatçinson - 39 yaş (02/08/1983), Kanada millisi;

3. Pepe - 39 yaş (26.08.1983), Portuqaliya millisi;

4. Kavaşima - 39 yaş (20.03.1983), Yaponiya millisi;

5. Dani Alveş - 39 yaş (05.06.1983), Braziliya millisi.

Yaşlılarla yanaşı, qarşıdan gələn Dünya Çempionatının ən gənc oyunçuları da bəlli olub. Siyahıya Almaniya millisindən Yusuf Mukoko başçılıq edir. O, 20 noyabr 2004-cü ildə anadan olub. 2022-ci il Dünya Çempionatının başladığı gün futbolçunun 18 yaşı tamam olacaq.

Həmçinin, siyahıda Avstraliya milli komandasının hücumçusu Qaranq Kuol (doğum tarixi - 15 sentyabr 2004-cü il) və İspaniya milli komandasının yarımmüdafiəçisi Qavi (6 avqust 2004-cü il) də yer alıb.
MAVEN orbital aparatı Marsda eyni vaxtda iki növ qütb parıltısı qeydə alıb.

Təbiət hadisəsi günəş küləyinin yüklü hissəciklərinin təsiri altında atmosferin yuxarı təbəqələrinin işıqlandırılması nəticəsində baş verib. O, Yerdə olduğu kimi, digər planetlərdə də qeydə alınır.

NASA-nın MAVEN-1 aparatının qeydə aldığı son qütb parıltısı cihazın bütün 8 illik fəaliyyəti ərzində ən parlaq parıltı olub. O, avqustun 27-də Günəşdə müşahidə olunan partlayış nəticəsində yaranıb.

Məhz bu partlayış nəticəsində eyni vaxtda iki növ parıltı meydana çıxıb. Birinci növ Marsın gündüz tərəfində müşahidə edilən proton axını olub. Eyni zamanda, planetin gecə tərəfində diffuz qütb parıltısı əmələ gəlib.


Password” (ingiliscədən tərcümədə açar söz – red.) insanların 2022-ci ildə hesablarını qorumaq üçün istifadə etdikləri ən populyar parol olub.

Bu barədə 30 ölkədə parolları təhlil edən parol meneceri “NordPass”ın hesabatında deyilir.

Məlumata görə, bu söz ən çox Avstraliya, Böyük Britaniya və Hindistanda istifadə olunub.

İkinci ən populyar seçim 123456 olub və son iki il ərzində dünyanın ən zəif parollarının siyahısında ilk yeri tutub. Belə parol bu il Braziliya, İndoneziya, İtaliya, Çili, Kanada, Kolumbiya, Macarıstan, Malayziya və bir sıra digər ölkələrdə ən populyar olaraq qalıb.

Rəqəmlərin daha mürəkkəb kombinasiyası olan 123456789 ilk üçlüyü qapayır. “Lakin bu, daha etibarlı deyil. Belə parolun sındırılması xüsusi kompüter proqramları üçün bir saniyədən az vaxt aparır”, - hesabatda deyilir.

ABŞ-da ən populyar parol “guest” (ingiliscədən tərcümədə qonaq – red.) sözü olub. O, dünyada dördüncü ən populyar kod sözü mövqeyində qərarlaşıb. Beşinci yerdə duran “qwerty” ingilis klaviatura düzümündə ardıcıl hərflərin birləşməsidir. Ondan sonra 12345678, 111111, 12345 kimi müxtəlif sadə ədəd birləşmələri gəlir.
"""

haber = haber.replace("\n", " ")
haber = haber.strip()
haber = haber.replace("   ", " ")
haber = haber.replace("  ", " ")
mylist = haber.split(" ")
mylist2 = []

i = 0
cnt = 1
while i < len(mylist)-1:
    cons = str(mylist[i])+' '+str(mylist[i+1])
    mylist2.append(cons)
    i += 1


kelime_frekans = {}

for k in list(set(mylist)):
    kelime_frekans[k] = mylist.count(k)

"""
for i in range(len(mylist) - 1):
    cons = str(mylist[i]) + ' ' + str(mylist[i + 1])
    print(cons)
    mylist2.append(cons)
"""


mylist2 = [ i for i in mylist2 if len(i) > 0 ]
# mylist2 icindeki her bir i icin, i'lerin uzunluklarinin (len) sifirdan buyuk oldugu
print( mylist2 )


mydic = {}
for i in list(set(mylist2)):
    intersection = mylist2.count(i)
    kelimeler = i.split(" ")
    mydic[i] =  intersection / (  kelime_frekans[ kelimeler[0] ] + kelime_frekans[ kelimeler[1] ]  )

print(mydic)


# (a n b) / (a u b)



"""
max_value = max(mydic.values())
result = ''
sorted_dic = {
    key: value for key, value in sorted(
    mydic.items(), key=lambda item: item[1], reverse=True)}

print(sorted_dic)
"""


#



s = "Şimali Atlantika Alyansının təyyarəsi Polşa ərazisinə düşən raketlərin trayektoriyasını izləyə bilib."
s = list(s)
print(s)

sonraki_harf = {
    'a': {'a': 0, 'b': 0, 'c': 0},
    'b': {'a': 0, 'b': 0, 'c': 0},
    'c': {'a': 0, 'b': 0, 'c': 0},
}

















