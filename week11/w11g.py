import warnings
warnings.filterwarnings("ignore")
import random
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt
import sys
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("Telecom_customer churn.csv")
df = df.select_dtypes(exclude=['object'])
df = df.fillna(df.mean())
target = 'churn'

"""
pca0 = PCA()
pca0.fit( df[df[target] == 0].drop(columns = [target]))

pca1 = PCA()
pca1.fit( df[df[target] == 1].drop(columns = [target]))

randomrow = [ df.drop(columns=[target]).iloc[5066] ]
pca0.transform( randomrow )
pca1.transform( randomrow )
"""

limit = 50000
train = df[:limit]
test  = df[limit:]

train_y = train[target]
train_x = train.drop(columns = [target])

test_y = test[target]
test_x = test.drop(columns = [target])

# clf = LinearDiscriminantAnalysis()
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostClassifier
clf = AdaBoostClassifier(n_estimators=100, random_state=0)
#clf = LogisticRegression()
clf.fit( train_x, train_y ) # SUPERVISED CLASSIFICATION
df['rfr'] = clf.predict( df.drop(columns = [target]) )

print("f1", f1_score( test_y, clf.predict(test_x) ) )



# PCA is UNSUPERVISED - NO TARGET VARIABLE!!
# LDA is SUPERVISED, TARGET VARIABLE!!

# LDA where is it used?
# TOO MUCH FEATURES, CLASSIFICATION (BINARY)
# NOT VERY SUITABLE FOR TOO COMPLEX PROBLEMS
# BUT IT IS USEFUL AND EFFECTIVE
# LDA IS A STATISTICAL APPROACH


# LOGISTIC REGRESSION IS "CLASSIFICATION" OF A REGRESSION WITH USING SIGMOID FUNCTION




import numpy as np
from sklearn.neural_network import BernoulliRBM
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])

"""
[
	[0.35210201 0.35157149]
  [0.27092641 0.27225275]
  [0.2786373  0.28112499]
  [0.23457579 0.23810905]
]
"""

model = BernoulliRBM(n_components=2)
model.fit(X)

print( model.transform(X) )

# PCA [8-10 useless columns] 1 new feature: point of view -- unsupervised [first component is the most important]
# RBM [8-10 useless columns] 2 new feature: point of view -- unsupervised [equally important vectors]
# LDA [8-10 useless columns] 3 new feature: point of view -- supervised
