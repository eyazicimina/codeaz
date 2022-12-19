

"""
ORDERNUMBER	QUANTITYORDERED	PRICEEACH	ORDERLINENUMBER	SALES	ORDERDATE	STATUS	QTR_ID	MONTH_ID	YEAR_ID	PRODUCTLINE	MSRP	PRODUCTCODE	CUSTOMERNAME	PHONE	ADDRESSLINE1	ADDRESSLINE2	CITY	STATE	POSTALCODE	COUNTRY	TERRITORY	CONTACTLASTNAME	CONTACTFIRSTNAME	DEALSIZE
10107	30	95.7	2	2871	2/24/2003 0:00	Shipped	1	2	2003	Motorcycles	95	S10_1678	Land of Toys Inc.	2125557818	897 Long Airport Avenue		NYC	NY	10022	USA	NA	Yu	Kwai	Small
10121	34	81.35	5	2765.9	5/7/2003 0:00	Shipped	2	5	2003	Motorcycles	95	S10_1678	Reims Collectables	26.47.1555	59 rue de l'Abbaye		Reims		51100	France	EMEA	Henriot	Paul	Small
"""
import pandas as pd
df = pd.read_csv("sales_data_sample.csv", encoding='latin-1', error_bad_lines=False)

row0 = df.iloc[0].to_dict()
row1 = df.iloc[1].to_dict()

print(row0)
print(row1)

# distance = abs(row0 - row1)
# WHY EUCLIDEAN DISTANCE HAS PROBLEMS?
# - for any distance
# - distance is small ==> rows are similar
# - distance is zero  ==> rows are identical
# - distance is high  ==> rows are not similar

# it is impossible for some variables to "get distance" between two data points

import numpy as np

def euclidean(row0: dict, row1: dict) -> float:
	distance = 0
	for i in row1:
		if (type(row0[i]) is float or type(row0[i]) is int):
			if not pd.isna(row0[i]):
				distance += np.power(row0[i] - row1[i], 2.0)   # (two reasons, 1: make it "positive", 2: when the difference gets bigger, the distance must get "bigger" exponantionaly -- EXTREMELY
	distance = np.sqrt(distance)
	return distance

def mahalanobis(row0: dict, row1: dict, df) -> float:
	distance = 0
	for i in row1:
		if (type(row0[i]) is float or type(row0[i]) is int):
			if not pd.isna(row0[i]):
				distance += np.power(row0[i] - row1[i], 2.0) / np.power(df[ i ].std(), 2.0)
	distance = np.sqrt(distance)
	return distance

print( euclidean(row0, row1) )
print( mahalanobis(row0, row1, df) )

# WARNING: sometimes, when converting from pandas to python int => np.int64, float => np.float64
# print(type(...))


# NORMALIZE !!
# MAHALANOBIS

# hamming
# jaccard
# cosine
# levenstein


# HAMMING DISTANCE
# same(0) or not(1)

# Gender = 'F', Gender = 'M' (flag variables)
# Gender = 'F', Gender = 'F'

# a, b
# gender(a) - gender(b) = ?

# age(a) = 34
# age(b) = 33
# age(c) = 100
# hamming(  age(a), age(b)   ) ===> 1
# hamming(  age(a), age(c)   ) ===> 1

# euclidean( a, b ) = 1
# euclidean( a, c ) = 66

# HAMMING ===> FLAG

# distance( country(a), country(b) ) ==> ?
# CUSTOMER ==> [age, gender, ........ country]
# CLUSTER  ==> spliting into groups
#
# CATEGORIC [country, city, size, product_line(category), status ] ==> HAMMING
#

print(df['COUNTRY'].unique())

# Manually generated MAP
dist_map = {
	('USA', 'France'): 1.0,   # VERY DIFFERENT
	('France', 'Spain'): 0.1, # VERY SIMILAR (low = similar)
	('USA', 'Japan'): 1.0     # VERY DIFFERENT
}

# Levenstein
# 2 text arasindaki benzerlik

# Can 2 text be substracted?
# distance( Amir - Emir )
# KEYSTROKE count


def levenshteinDistance(str1, str2):
    m = len(str1)
    n = len(str2)
    d = [[i] for i in range(1, m + 1)]   # d matrix rows
    d.insert(0, list(range(0, n + 1)))   # d matrix columns
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:   # Python (string) is 0-based
                substitutionCost = 0
            else:
                substitutionCost = 1
            d[i].insert(j, min(d[i - 1][j] + 1,
                               d[i][j - 1] + 1,
                               d[i - 1][j - 1] + substitutionCost))
    return d[-1][-1]


def minimumEditDistance(s1,s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    distances = range(len(s1) + 1)
    for index2,char2 in enumerate(s2):
        newDistances = [index2+1]
        for index1,char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1+1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]



print(levenshteinDistance("emir","emre"))
print(levenshteinDistance("rosettacode","raisethysword"))

# matematik +-/*
# REPLACE ( amir => emir )
# SWAP    ( fomr => form )
# DELETE  ( computers => computer )
# ADD     ( similar => similarity )


# CATEGORIC = LEVENSHTEIN  NOT WORKING


countries = ['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Brunei ','Bulgaria','Burkina Faso','Burundi','Côte d\'Ivoire','Cabo Verde','Cambodia','Cameroon','Canada','Central African Republic','Chad','Chile','China','Colombia','Comoros','Congo (Congo-Brazzaville)','Costa Rica','Croatia','Cuba','Cyprus','Czechia (Czech Republic)','Democratic Republic of the Congo','Denmark','Djibouti','Dominica','Dominican Republic','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia','Eswatini (fmr. "Swaziland")','Ethiopia','Fiji','Finland','France','Gabon','Gambia','Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Holy See','Honduras','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Mauritania','Mauritius','Mexico','Micronesia','Moldova','Monaco','Mongolia','Montenegro','Morocco','Mozambique','Myanmar (formerly Burma)','Namibia','Nauru','Nepal','Netherlands','New Zealand','Nicaragua','Niger','Nigeria','North Korea','North Macedonia','Norway','Oman','Pakistan','Palau','Palestine State','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Poland','Portugal','Qatar','Romania','Russia','Rwanda','Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines','Samoa','San Marino','Sao Tome and Principe','Saudi Arabia','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','South Korea','South Sudan','Spain','Sri Lanka','Sudan','Suriname','Sweden','Switzerland','Syria','Tajikistan','Tanzania','Thailand','Timor-Leste','Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States of America','Uruguay','Uzbekistan','Vanuatu','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe']

for c1 in countries:
	for c2 in countries:
		if c1 != c2:
			if levenshteinDistance(c1, c2) < 2:
				print(c1, c2, levenshteinDistance(c1, c2))

# WHY?

# Ahmet
# Ahmed - variation
# Ahemt - typo

# Sema
# Semah
# Semiha

# TYPO, yanlis yazim, farkli yazim

# Levensthein ===> Single word
# TEXTUAL DATA

# tweets:
# tweet1 : .......
# tweet2 : .......

# customer ---> company [messages]
complianments = [
"sizin productlar cok kotu",
"productlariniz kadar cok kotu gormedim",
"cok kotu productlar yapiyorsunuz",
"sirketiniz cok kotu productlar yapiyor",
"sizi sevmiyorum"
]
# ..... 10000

# product --> 2500 complainment
# servis (hizmet) --> 300
# not ...
# VISUALIZE


def textDistance( s1, s2 ):
	#! distance = 1 - similarity
	s1 = s1.split(" ")
	s2 = s2.split(" ")

	same = 0
	diff = 0
	for w1 in s1:
		if w1 in s2:
			same += 1
		else:
			diff += 1

	for w2 in s2:
		if w2 in s1:
			same += 1
		else:
			diff += 1

	return same / (same + diff)




def jaccardDistance( s1, s2 ):
	#! distance = 1 - similarity
	s1 = s1.split(" ")
	s2 = s2.split(" ")

	return 1.0 - len(set(s1).intersection(set(s2))) / len(set(s1).union(set(s2)))


print("DISTANCE", jaccardDistance(complianments[2], complianments[3]))
# "sizin productlar cok kotu",
# "productlariniz kadar cok kotu gormedim",


# CUSTOMER arasindaki benzerlik
# CUSTOMER !!!!! (satin aldiklari productlar)
# a = milk, egg, toilet paper .......
# b = tomatoes, milk, egg, battery,.....
# c = sirke, milk, yogurt .....

# IF THERE IS A MULTIPLE!!! CATEGORIC VARIABLE ==> jaccard
# TEXT [words] = sentence = list of words (multiple), word = categoric

# =====
# PRODUCT!!
# e-commerce
# bank
# market
# ...
# user - product similarity
# JACCARD similarity
# Ahmet [.....] = Mehmet [....]


# JACCARD_DISTANCE( Ahmet, Mehmet ) ==> [SMALL] (these two users have SIMILAR products)
# OFFER ahmet - mehmet ==> mehmet
# OFFER mehmet - ahmet ==> ahmet

# EVERY DISTANCE METRIC HAS PROBLEMS!!!
# Jaccard


ahmet = ['bread', 'water', 'banana']
mehmet = ['bread', 'water', 'battery']

#print( jaccardDistance(" ".join(ahmet), " ".join(mehmet)) )

freq = {
	# POPULARITY
	'bread': 999874,
	'water': 999998,
	'banana': 304866,
	'battery': 78995
}

def weightedJaccard( s1, s2 ):
	intersection = list(set(s1).intersection(set(s2)))
	union = list(set(s1).union(set(s2)))

	common = sum([1 / freq[i] for i in intersection])
	total = sum([1 / freq[i] for i in union])
	# TF-IDF HAS ALSO PROBLEMS
	return 1.0 - common / total


def Jaccard( s1, s2 ):
	intersection = list(set(s1).intersection(set(s2)))
	union = list(set(s1).union(set(s2)))

	common = sum([1 for i in intersection])
	total = sum([1  for i in union])

	return 1.0 - common / total

print( "DISTANCE - uzaklik: 1-sim", weightedJaccard( ahmet, mehmet ))
print( "DISTANCE - uzaklik: 1-sim", Jaccard( ahmet, mehmet ))
