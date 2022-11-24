

# Python programlama dili
# -- Scripting dili, Compile edilmeyen
# -- Avantajlari, hizli derleme, exe'ye cevirme veya program yapma gerekli degil
# -- Dezavantaji, biraz daha yavas calisir!

# COMPILED:  Code --> Binary --> Run (FAST)
# SCRIPTING: Code --> Run (SLOW)

# Python -- LATE BINDING (bir type atamasi sart degil!)

# Atomic data types: int, str, float, bool
a1: int = 3
a2 = 3
b1 = "test"
b2 = 'test'
c = False
d = 3.14
print(a1, b1, c, d)

print(type(a1))
print(type(a2))
print(type(b1))
print(type(c))
print(type(d))

# int: memory'de ne kadar yer kaplar? = 4 byte
# float: = 8 byte
# bool: = 1 (1/0)
# str:  = minimum 2,   (kac karakter varsa), "emre" --> 4 karakter --> 4 byte
# char: = 1

s = "aysel"
b1 = f"selam {s}" # value ! (regex gibi ozel karakterleri destekliyor)
b2 = 'selam s' # value !
print(b1, b2)

# Raw Text --> 'tek tirnak' single quote

# =============================
# (#) comment, not read this line, bu satiri okuma


# a = 3
# b = 5


"""
Yorum - Comment - Ignore
a = 3 
b = 5
asfa;dfkds;f kasd;fkads; kf;dskf ;sdkfds 

"""

# Special characters!!

a = "emre" \
    "yazici"

a = "emre\nyazici\nburaya\ngeldi\nsonra\ngitti\nmerhaba"
# ==> \n special character (newline) yeni satir olusturur
print(a)

a = """
emre
yazici
buraya
geldi
sonra
gitti
merhaba
"""

print(a)

# HTML
# SQL
# Javascript

sql = """
SELECT *
FROM TABLE
WHERE ....
""" # 3 tirnak!!

sql = '''
selam
'''


"""
S
adskjf;ldsjfdsflksjlks
"""

# Complex data types

a = [11, 22, 33]
# -- ! listeler istenilen sayida item alabilir (0, 1, 2, N)
# -- ! listelerin icindeki itemlara, INDEX ile ulasilir (INDEX bir integer)
print(type(a))
print(a[0])

#! Indexler her zaman SIFIRDAN baslar

# len(a) = bir listenin uzunlugu, adetini verir!!
# len(a) = 3
# a[3] ?
print(a[len(a)-1])

a = ["deneme", "test", "selam", "merhaba", "nasilsin"]
#       0         1       2         3          4
#       -5       -4      -3        -2         -1
print(a[ len(a)-2 ])
print(a[ -2 ])
print(a[-1])


# RANGE!!
print(a[0:2])
# listvariable[ start : end ]
# colon, iki nokta ust uste --> RANGE
# Eger START verilmezse, 0 olarak kabul edilir
# Eger END verilmezse, son (end) olarak kabul edilir

print("a", a)
print("a[:2]", a[:2])
print("a[1:]", a[1:])
print("a[1:-1]", a[1:-1])
print("!!!", a[1:-1])

#! error, warning!
#? acaba burada dogru mu yaptik?
#* en son kaldigim yer!!
## normal
#

# COK BENZER: list =~ str
# string == a line of characters

a = "aysel"
print(a)
print(a[-1])
print(a[1:3])

print(a, list(a))

# CAST (convert) etmek
# type parantezine aliriz
a = str(3)
print(a, type(a))
print("emre", list("emre"))

# List
l = list()
l = ['emre', 'ahmet']
l = []

l.append( "turkiye" )
l.append( "azerbaycan" )

# Pop, index, indexteki veriyi siler!!
l.pop(0)
print(l)

l = list("ABCDEFGHI")
#l = ['A', 'B'....]
l.extend(['J','K','L'])  # BIRDEN FAZLA item eklemek istedigimizde, Extend kullaniyoruz
print(l)

# F yi cikarmak istiyorum
# 1. yontem: l.remove('F')
# 2. yontem: del l[5]
# 3. yontem: l.pop(5)
# 4. yontem: l = l[:5] + l[6:]

print(l)

a = (3, 5) # Tuple
# koordinat,
lokasyon = (34.56, 33.67) # Koordinatlar

print(tuple(l)[2])
# ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L')
#       (name,    gender,  age)
salih = ('salih', 'male', '33')
print(salih)

print(l)
l.insert( 1, 'X')
print(l)

l = [
    ('emre', 38),
    ('mustafa', 56),
    ('aysel', 23)
]
print(l)

print( l[1][1] )

a = ( "Cihan", ["futbol", "basketbol"] )
print(a[1][1])

a = ()  # constructor, initialize
a = tuple(['e', 'x', '3']) # convert, cast

# ============
# Dictionary
# ============
# TERIM (term): TANIM (definition), WIKIPEDIA
# KEY         : VALUE
a = {
    "age": 32,
    "gender": "male",
    "name": "emrah",
    "job": "engineer",
}


pi = 3.14
pi = 3.0
pi = 22.0/7.0

print(float("3.5"))

def metnisifrele( metin: str ) -> str:
    sfkjafkfksfj




metnisifrele("3")



# Dictionary ozellikleri:
# - Sirasi onemli degil!!

# ['a','b','c'][2] --> listenin ITEM ina ulasmak

print( a['name'], a['age'] )
print( a )

# KEYS must be unique

a = {
    'name': 'mustafa',
    'name': 'erdem'
}

print(a)

a = {
    "age": 32,
    "gender": "male",
    "name": "emrah",
    "job": "engineer",
}

# YENI BIR ITEM EKLEME!!!
a['married'] = True # yazmak icin, (OVERWRITE - WRITE)
a['age'] = 35
print(a['married']) # to access, to read, okumak icin

del a['job']
print(a)


print(list(a.keys()))

for i in a:  # list(a.keys())
    print("KEY =", i, "VALUE =", a[i])

# elastic
# ekleme, cikarma, degistirme update cok kolay

a = {
    "isim": "emrah",
    "araba": ["bmw", "mercedes", "ferrari"],
    "cocuklar": [
        ["Ahmet", 3],
        ["Mustafa", 1]
    ]
}

# JSON
# LISTE, DICTIONARY ==> JSON
# JSON NOT SUPPORTS TUPLE !!

import json # eger birden fazla, cok adet fonksiyon kullanacaksak!
print( json.dumps(a) )  # json.dumps ==> metinsel olarak gostermeye yariyor.

# modulename.functionname( arguments )

import json as j # j ismiyle, nickname ile , alias ile bu kutuphaneyi import et

print( j.dumps(a) )

# Json kutuphanesinden, sadece !!! loads fonksiyonunu yukle.
from json import dumps

print(a)
print( dumps( a ) )

# dumps ==> objeji, metne ceviriyor
# loads ==> metni, objeye ceviriyor
from json import dumps, loads
print( loads( dumps( a ) ), type(loads( dumps( a ) )) )

with open("sample.json", "w") as outfile:
    outfile.write(dumps(a))

# VERI ICIN
# AYAR - SETTING - CONFIGURATION - PARAMETER - CONSTANT
"""
import json

import json
json.loads()

import json as j
j.loads()

from json import loads
loads()
"""

from json import *


f = open('text.json')
data = json.load(f)
print(data)

print( data['tr']['hello'] )
# SABIT DEGERLER
# QUERYLER
# CONFIG
# CODE DOSYASINA YAZMAYALIM!!

config = json.load(open('config.json'))
print(config)


# YAML == men: [John Smith, Bill Jones]                 # daha az yer kapliyan format
# JSON == {"men": ["John Smith", "Bill Jones"]}         # kontrollu, hata olmayan



a = 3


personel = ['emre', 'ahmet', 'mustafa']

"""
for (int i = 0; i < personel.length; i++){
    
}
"""

for p in personel:
    print(p)

# len(personel) = 3
for i in range(3):
    print(i, personel[i])

# 0 -- 10'a kadar
# 0 -- N'e kadar

a = {
    "age": 32,
    "gender": "male",
    "name": "emrah",
    "job": "engineer",
}

for i in a:
    print(i, a[i])

# EACH, HER BIR, HEPSI, .... For kullanabiliyoruz.


# KONUSMA DILINDE BIR IFADE: "HER BIR ELEMAN ICIN, SKOR HESAPLA"
# PYTHON DILINE            :   !  ==> FOR

"""
for(int i = 0; i < 10; i++){
asfdsfsfadfdsfsd
}
"""

for i in a:
    print(i)
print("xxx")

a = 101

if a == 10:
    print("a 10'a esittir")
    print("merhaba")
print("selam")

"""
if(a == 10){
}
"""

i = 0
while i < 10:
    if i % 2 == 0:
        print(i)
    i = i + 1

# AYNI DOSYAYI, FARKLI 2 editorde acmayin
# TAB yapacak
# 4 space, KARISACAK, hata verecek


def method( argument ):
    return argument + 1

def method2( argument ):
    pass

# sub routine, method, function

# definition of the method
# abs: absolute (sayi) eger negatifse, -1 ile carpilmis halini
def abs( sayi ):
    if sayi < 0:
        return -1 * sayi
    else:
        return sayi


def dosyalariSil():
    # 1. dosyayi sil
    # 2. dosyayi sil
    # 3. dosyayi sil
    pass

def temizle( dataFrame ):
    # ... process ...
    # ... process ...
    return dataFrame


# Sayi degiskeni (variable), bir integer
def abs2( sayi: int ):
    if sayi < 0:
        return -1 * sayi
    else:
        return sayi

# Sayi degiskeni (variable), bir integer
def abs3( sayi: int ) -> int:
    if sayi < 0:
        return -1 * sayi
    else:
        return sayi


# DEFAULT VALUE
def cevreHesapla( r: float, pi: float = 3.1415 ) -> float:
    return 2 * pi * r

print(cevreHesapla( 10 ))
print(cevreHesapla( 10, 3.1415 ))
print(cevreHesapla( 10, 3 ))
print(cevreHesapla( 10, 22.0/7.0 ))

import math # Python kendi kutuphanesi
print(cevreHesapla( 10, math.pi ))


# yaricap = r
# cap = 2r
def cevreHesapla( yaricap: float = None, cap: float = None, pi: float = 3.1415 ) -> float:
    if yaricap != None:
        return 2 * pi * yaricap
    elif cap != None:
        return pi * cap
    else:
        print("HATA VAR")

print(cevreHesapla( cap = 10, pi = 3 ))

f = open("demofile.txt")
f = open("demofile.txt", 'r')
f = open("demofile.txt", 'r',encoding = "utf-8")
f = open("demofile.txt", mode='r',encoding = "utf-8")

# UTF-8
# ISO-8859-9

# import utility
from utility import *

print(ortalama([1,2,3,4,5]))
print(ortalama([5]))
print(alanHesapla(100))
# print(ortalama([]))

"""
i = 0
try:
    print(12 / i)
except:
    print("hata yakalandi")
"""

i = 0
try:
    math.sqrt(-2)
    print(12 / i)
except ValueError:
    print("NEGATIF SAYILARIN KOKU OLMAZ")
except ZeroDivisionError:
    print("SAYILAR SIFIRA BOLUNEMEZ")
except Exception as e:
    print("hata yakalandi", e)


def hesapAc(isim, yas):

    assert yas >= 18
    assert len(isim) > 2


    # database e kayit et
    # .....
    pass


hesapAc("E", 19)


# if, def, try, while, for, with

with open("sample.json", "w") as outfile:
    outfile.write(dumps(a))
#! outfile.write("xx")



# PYTHON COK GENIS !!
l = ['emre', 'ahmet', 'canan', 'aysel', 'fatma', 'burak', 'burak', 'aysel', 'aysel']
l.sort()
print(l)

print(l.count('aysel'))
# ne gibi komutlari var

#! l.clear()
# print(dir(l))
print(l)

print(len(l))

a = {
    "age": 32,
    "gender": "male",
    "name": "emrah",
    "job": "engineer",
}

print(dir(a))
print(a.items())

# ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

"""
3.10
def greeting(language):
    chosen_language = language.capitalize()
    match chosen_language:
        case 'English':
            print('Hello')
        case 'German':
            print('Hallo!')


greeting('english')
"""

# kumeler, sets
s = {"key": "value"}
s = [1, 2, 3, 3]
s = {1, 2, 3}  # must be unique


s = [1, 2, 3, 3, 1, 0 ,1 , 1, 34, 45, 5, 3,5,3,3,4]
print(set(s))


# userlarin aldigi, productlar
user1 = {'iphone6', 'lenovo computer', 'samsung watch'}
user2 = {'iphone6', 'hp computer', 'xiami watch', 'lenovo computer'}

s = [1, 2, 3, 3, 1, 0 ,1 , 1, 34, 45, 5, 3,5,3,3,4]
print(list(set(s)))
print(dir(user1))

# how similary user1 and user2

print("simliarity")
print(2 * len(user1.intersection(user2)) / (len(user1) + len(user2))) # SIMILARITY (data science)

# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

# bu 2 user in aldigi productlar (toplam - hepsi - all)
print(user1.union(user2))

print( len(user1.intersection(user2)) / len(user1.union(user2))  )

"""


# list icindeki itemlarin HER birine bir islem uygulamak istiyorsam!!
lines = [l for l in lines]

# yukaridaki ifade ile asagidaki ifade ayni

for i in range(len(lines)):
    lines[i] = lines[i]


lines = [l.strip() for l in lines]

# for l in lines ==> lines in icindeki her bir "l" icin
# l for l in lines
# 1     2
# 2. l sabit !! degistirmiyoruz, CONSTANT
# for l in lines ==> lines in icindeki her bir "l" icin, loop for
# 1. l

print(lines)

# 9.964 bytes
# Azaltmak, daha az  yer kaplasin, ziplensin
"""












lines = None
with open('haber.txt') as f:
    lines = f.readlines()
print(lines)

fullpath = "C:\\Users\\ruhangizag\\Desktop\\haber.txt"

