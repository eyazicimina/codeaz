"""
import sys
import pandas as pd

from fitter import Fitter, get_common_distributions, get_distributions
path = "/home/mina5/PycharmProjects/codeaz-python/Online Retail_1000.csv"
df = pd.read_csv(path)
f = Fitter(df['UnitPrice'], distributions=get_common_distributions())
f.fit()
#print(len(get_distributions()))
print(f)
print(f.hist())
print(f.summary())


d = f.get_best(method='sumsquare_error')
print(d)
dk = list(d.keys())

d = {"name": dk[0], "params": d[dk[0]]}

"""




import io
path = "/home/mina5/PycharmProjects/codeaz-python/"
f = io.open(path + 'corpus.txt' , mode="r", encoding="utf-8")

text = f.read()
text = text.replace('\n', ' ')
text = text.lower()
text = text.split(" ")
text = list(set(text))
text = [t for t in text if len(t) > 0]

def transliterate( t: str ) -> str:
	m = {
		'ə': 'e',
		#'q': 'k',
		'ş': 's',
		'ç': 'c',
		'ı': 'i',
		'ö': 'o',
		'ü': 'u',
		'ğ': 'g',
	}
	return "".join( [m[i] if i in m else i for i in t] )

text = [ transliterate(t) for t in text]

print(text[45])
# 3-GRAM = [bugun] [hava] [cok]

olasilik = {}


for t in text:
	for i in range(len(t) - 2):
		key = t[i:i+3]
		if key not in olasilik:
			olasilik[key] = 0
		olasilik[key] += 1


print(len(olasilik), olasilik)

def testEt( testMetni: str ) -> float:
	total = 0
	for i in range(len(testMetni) - 2):
		key = testMetni[i:i+3]
		if key in olasilik:
			total += olasilik[ key  ]

	return total

import random

LETTERS = "abcdefghijklmnoprstuvyzqxw"
def randomText(length: int) -> str:
	s = ""
	for i in range(length):
		s += random.choice(LETTERS)
	return s

import pandas as pd

df = pd.DataFrame( columns = ['word', 'type', 'test', 'length'] )
for _ in range(2000):
	w = random.choice( text )
	r = randomText( len(w) )

	df.loc[ len( df) ] = [ w, 'word', testEt(w), len(w) ]
	df.loc[ len( df) ] = [ r, 'random', testEt(r), len(r) ]

dfrandom = df[ df['type'] == 'random' ]
dfword = df[ df['type'] == 'word' ]

dfrandom = dfrandom.groupby('length').agg( {'test': 'mean'} ).reset_index()
dfword = dfword.groupby('length').agg( {'test': 'mean'} ).reset_index()

dfword.to_csv(path + 'dfword.csv')
dfrandom.to_csv(path + 'dfrandom.csv')


for t in range(1100, 1300, 10):
	hipotez_above = df[ (df['test'] > t) & (df['length'] == 7) ]
	hipotez_below = df[ (df['test'] < t) & (df['length'] == 7) ]

	hipotez_above = hipotez_above['type'].value_counts().to_dict()
	hipotez_below = hipotez_below['type'].value_counts().to_dict()

	h1 = hipotez_above['word'] / sum( list(hipotez_above.values()) )
	h2 = hipotez_below['random'] / sum( list(hipotez_below.values()) )

	h = h1 * 0.4 + h2 * 0.6
	print(t, h)


print(testEt( 'yaziciemre' )) # 15 yil
print(testEt( 'elmargarayev' )) # 5 yil
print(testEt( 'xaqani.qasimov.2002' )) # 7 yil
print(testEt('r.qurbanova1997')) #  7 yil
print(testEt('vefa.ibrahimovaa')) #  7 yil
print(testEt('ulviyyaallahverdieva')) #  2 yil
print(testEt('heyder432')) #  10 yil
print(testEt('sh.kamilla99')) #  6 yil



