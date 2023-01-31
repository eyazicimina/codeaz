import pickle
from w12d_preprocess import *

df = df.apply(lambda row: prepareRow(row), axis = 1)

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(max_depth=5, random_state=0)

y = df['Response']
x = df.drop(columns = ['Response'])
clf.fit(x, y)
file = open('model.pickle', 'wb')
pickle.dump( clf, file )

