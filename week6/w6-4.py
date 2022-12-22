import numpy as np
import pandas as pd
dx = pd.read_csv(r'/home/mina5/PycharmProjects/codeaz-python/telcochurn.csv')



# dwlltype
# #marital
"""
for i in range(len(dx)):
	row = dx.iloc[i]
	if row['ownrent'] == np.nan or pd.isnull(row['ownrent']):

		filtered = dx[  (dx['income'] == row['income']) & (dx['dwlltype'] == row['dwlltype']) & (dx['marital'] == row['marital']) ]['ownrent']
		print(row)
		print(filtered.value_counts())
"""

nulls = dx[ dx['ownrent'].isnull() ]
notnulls = dx[ dx['ownrent'].notnull() ]


for i in dx.select_dtypes(include=['object']):
	ratios = []
	# get the values
	values = dx[i].unique()
	# calculate consistancy value
	for v in values:
		# filter by value
		ownrent = dx[ dx[i] == v ]['ownrent']

		most_freq = list(dict(ownrent.value_counts().to_dict()).values())
		most_key = list(dict(ownrent.value_counts().to_dict()).keys())

		if len(most_freq) > 0:
			most_freq = most_freq[0]
			most_key = most_key[0]
			ratio = most_freq / len(ownrent)
			ratios.append(ratio)
		#print(i, values)


	print(i, v, most_key, len(ratios), np.mean(ratios))



# ownrent

