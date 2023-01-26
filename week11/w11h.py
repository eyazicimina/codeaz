
import pickle
import warnings
warnings.filterwarnings("ignore")
from sklearn.metrics import f1_score
import pandas as pd

df = pd.read_csv("Telecom_customer churn.csv")
df = df.select_dtypes(exclude=['object'])
df = df.fillna(df.mean())
target = 'churn'

limit = 50000
train = df[:limit]
test  = df[limit:]

train_y = train[target]
train_x = train.drop(columns = [target])

test_y = test[target]
test_x = test.drop(columns = [target])


"""

# clf = LinearDiscriminantAnalysis()
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostClassifier
clf = AdaBoostClassifier(n_estimators=100, random_state=0)
#clf = LogisticRegression()
clf.fit( train_x, train_y ) # SUPERVISED CLASSIFICATION

# clf == hem egitme kodu, algoritma
# clf == fit() cagirdiktan sonra, ayrica, MODEL olusuyor icinde!!!
pickle.dump(clf, open('w11.pickle', 'wb'))

df['rfr'] = clf.predict( df.drop(columns = [target]) )

print("f1", f1_score( test_y, clf.predict(test_x) ) )

# It took 15 minutes to train
# RUN TIME
"""

loaded_model = pickle.load(open('w11.pickle', 'rb'))
print("f1", f1_score( test_y, loaded_model.predict(test_x) ) )



