
from sklearn.ensemble import IsolationForest
import pandas as pd
path = "/home/mina5/PycharmProjects/codeaz-python/w12/Telecom_customer churn.csv"
df = pd.read_csv(path)
df = df.select_dtypes(exclude=['object'])
df = df.fillna(0)

from sklearn import svm
df = df.sample(n = 2000)
clf =  svm.OneClassSVM(nu = 0.01)
clf.fit(df)
r = clf.predict(df)


#clf = IsolationForest(random_state=0, n_estimators = 50).fit(df)
#r = clf.predict(df)


r = list(r)
from collections import Counter
print(Counter(r))



