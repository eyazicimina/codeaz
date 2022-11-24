
print("main3")

# isim - yas
# 1. grup neferler
grup1 = {
    'ahmet': 24, 'aysel': 23, 'mehmet': 30
}
grup2 = {
    'ali': 22, 'salala': 21
}

# Merge? - Birlestirme
print(grup1)
grup1.update(grup2)                     # Variable based assignment
grup1.update({'ali': 22, 'salala': 21}) # Value based assignment
print(grup1)


ikigrubunisimleri = list(grup1.keys())
print(ikigrubunisimleri, type(ikigrubunisimleri))

d = {}
d[ 'Baku', 'Istanbul' ] = 'Ucak Seferi-1'  # FLIGHT NUMBER
d[ 'Paris', 'Baku' ] = 'Ucak Seferi-2'     # FLIGHT NUMBER

print(d)

a = 'Baku', 'Istanbul'
print(a)


# HAVA SICAKLIGINI, FAHRENHEIT'TAN CELCIUS'A CEVIR
def fahrenheitToCelcius( derece: float ):
    celcius = (derece - 32) / 1.8
    mesaj = ""

    if celcius < 10:
        mesaj = "soguk"
    elif celcius < 20:
        mesaj = "normal"
    elif celcius < 30:
        mesaj = "sicak"
    elif celcius >= 30:
        mesaj = "cok sicak"

    return celcius, mesaj

print(fahrenheitToCelcius(100))


notlar = {'emre': 75, 'ahmet': 90, 'mehmet': 45}

def getMaximumScore( scores: dict ):
    maximum = 0
    maxitem = None
    for isim in scores:
        if scores[isim] > maximum:
            maximum = scores[isim]
            maxitem = isim
    return maxitem, maximum

result = getMaximumScore(notlar)
print(result, type(result))


def predict( bilgiler ):

    return True, 0.75


print(predict({"tenure": 32, "age": 40, "balance": 30000}))


sehirler = ['Istanbul', 'Baku', 'London', 'Paris']
mesafeler = {}

# istanbul baku = 1758
# istanbul londra = 2501
# baku london = 3980
# baku paris = XXXX
# istanbul paris = 2256
# londra paris = 344

mesafeler[ 'Istanbul', 'Baku' ] = 1758
mesafeler[ 'Baku', 'Istanbul' ] = 1758
mesafeler[ 'Istanbul', 'Londra' ] = 2501
mesafeler[ 'Londra', 'Istanbul' ] = 2501
mesafeler[ 'Londra', 'Baku' ] = 3980
mesafeler[ 'Baku', 'Londra' ] = 3980

print(mesafeler)

"""
{
    ('Istanbul', 'Baku'): 1758, 
    ('Baku', 'Istanbul'): 1758, 
    ('Istanbul', 'Londra'): 2501, 
    ('Londra', 'Istanbul'): 2501, 
    ('Londra', 'Baku'): 3980, 
    ('Baku', 'Londra'): 3980
}
"""


isimler = ['ahmet', 'mustafa', 'canan', 'temel']

# UNIQUE 2li kombinasyon
# TENIS oynayacaklar, (ahmet, mustafa), (mustafa, canan), (mustafa, ahmet) XXX


for i1 in isimler:
    for i2 in isimler:
        if i1 < i2:
            print(i1, i2)

"""

# Kombinasyon!!!
C( N, R ) 
C( 4, 2 ) = 4*3 / 2!

mustafa ahmet
mustafa canan
canan ahmet
temel ahmet
temel mustafa
temel canan
"""

# Recursive functions

# factorial
# 4! = 4x3x2x1
# 4! = 4 x 3!
# 3! = 3 x 2!
# 2! = 2 x 1!
# 1! = 1

def factorial( n: int ) -> int:
    r = 1
    for i in range(1, n + 1):  # start - end
        r = r * i
    #for i in range(n): # end
    #    r = r * (i+1)

    return r

print(factorial(4))


def factorial2( n: int ):
    # 4! = 4 x 3!
    # N! = N x (N-1)!
    if n == 1: return 1
    return n * factorial2( n-1 )


print(factorial2(4))





mesafeler = {}
mesafeler[ 'Istanbul', 'Baku' ] = 1758
mesafeler[ 'Baku', 'Istanbul' ] = 1758
mesafeler[ 'Istanbul', 'Londra' ] = 2501
mesafeler[ 'Londra', 'Istanbul' ] = 2501
mesafeler[ 'Londra', 'Baku' ] = 3980
mesafeler[ 'Baku', 'Londra' ] = 3980
mesafeler[ 'Istanbul', 'Paris' ] = 2256
mesafeler[ 'Paris', 'Istanbul' ] = 2256
mesafeler[ 'Paris', 'Londra' ] = 344
mesafeler[ 'Londra', 'Paris' ] = 344



def rotaBul( baslangic: str, bitis: str, devam_eden_rota = "" ):
    # paris, baku,
    if (baslangic, bitis) in mesafeler:
        return f"{devam_eden_rota}, {baslangic}, {bitis}"

    for m in mesafeler:
        if m[0] == baslangic:
            r = rotaBul( m[1], bitis, devam_eden_rota + " " + m[0] )
            if r != None:
                return r
    return None

print(rotaBul('Paris', 'Baku'))


import math

def isPrime( n: int ) -> bool:
    limit = int(math.sqrt( n ))
    for c in range(2, limit):
        if n % c == 0:  # TAM BOLUNUYORSA, MOD = Kalan == 0 ise
            return False
    return True

# Prime number formul (asal sayi) = (kendisi ve 1 disinda)
# baska hic bir sayiya bolunmeyenler
numbers = [24,56,55,17,29,33,101,670,497,405,223,229]
for n in numbers:
    print(n, isPrime(n))

# a = b x c
# 101 = b x c (tam sayi) (101 asal sayi)
# sqrt(80) = 8,94427191 ==> int(8,94427191) = 8
# 10.0012
# 2,3,4,5,6,7,8,9,10,....79
# 8 = KUCUK CARPAN


population = {
    'Baku': 2400000,
    'Ankara': 2600000,
    'Amsterdam': 1700000
}


# KOTU YONTEM
# population['xxxx']
# IYI YONTEM
print(population.get('Istanbul'))
# DAHA IYI YONTEM
print( population.get('Istanbul', 1000000) )



isimler = ['ahmet', 'mehmet', 'canan']
yaslar = [34, 23, 45]

# iki listeyi, keys and values seklinde, bir dictionary yapma
isim_yas = dict( zip( isimler, yaslar ) )
print(isim_yas)

isimler = list(isim_yas.keys())
print(isimler)

yaslar = list(isim_yas.values())
print(yaslar)

# PARAMETRELERI, disaridan okumak

# Epoch / Iteration
# Kac defa, kac kere, kac kez, tekrar ogrensin!!
# parametre1 = input()
# print("parametre1", parametre1)


a = [40, 456, 21,23,45,677,89]

print(sum(a) / len(a))
# print(avg(a))

print(max(a), min(a))

# RANGE !!
print(max(a) - min(a))

# Ngram
# N = 1,2,3,4,5,.....
# unigram - monogram = (1 gram)
# bigram (2 gram)
# trigram (3 gram)

# BIR SONRAKI KELIMEYI TAHMIN EDECEGIZ!!!!
# BIR SONRAKI ALINACAK URUNU TAHMIN EDECEGIZ


# en guzel
# kredi karti
# bank atmsi
# belediye binasi
# aksam saati
# yemek vakti









