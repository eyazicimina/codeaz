import matplotlib.pyplot as plt
import pandas as pd
#: Load tthe dataset
df = pd.read_csv("/home/mina5/Desktop/codeacedemy/week6-quiz1.csv")
#: Shrink the dataset
df = df.sample(5000)
#: Transform the features into numeric
df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})
df['Vehicle_Age'] = df['Vehicle_Age'].map({'> 2 Years': 2, '1-2 Year': 1, '< 1 Year': 0})
df['Vehicle_Damage'] = df['Vehicle_Damage'].map({'Yes': 1, 'No': 0})


#: Split the data set to [input and output]
y = df['Response']
x = df.drop(columns=['Response'])
print(x)
print(y)

# CLASSIFICATION PROBLEM

from sklearn import tree

#: Create an algorithm
clf = tree.DecisionTreeClassifier(max_depth = 4)
#: Train the algorithm to produce a "model"
# fit = train, egitmek
clf.fit( x, y )


for i in range(len(x.columns)):
  print(i, x.columns[i], clf.feature_importances_[i])

# FEATURE IMPORTANCE <=> CORRELATION
"""
0 Gender 0.0
1 Age 0.23255975104067847
2 Driving_License 0.0
3 Region_Code 0.0
4 Previously_Insured 0.07456200918035183
5 Vehicle_Age 0.0
6 Vehicle_Damage 0.6781676584076746
7 Annual_Premium 0.0
8 Policy_Sales_Channel 0.013071652342915364
9 Vintage 0.0016389290283797136
"""


df = pd.read_csv("/home/mina5/PycharmProjects/codeaz-python/Telecom_customer churn.csv")
df = df.select_dtypes(exclude=['object'])
df = df.fillna(0)

df = df['months'] > 10


clf = tree.DecisionTreeClassifier(max_depth = 4)
y = df['churn']
x = df.drop(columns = ['churn'])
clf.fit(x, y)

for i in range(len(x.columns)):
  print(i, x.columns[i], clf.feature_importances_[i])

# FEATURE IMPORTANCE IS A PROPORTION OF ALL VARIABLES

"""
0 rev_Mean 0.028757795909818588
1 mou_Mean 0.06302782056930356
2 totmrc_Mean 0.05906763297482365
9 change_mou 0.039284615381206374
48 months 0.27707937307204955
52 totmou 0.007202133574466707
66 hnd_price 0.03948104902256579
76 eqpdays 0.4798170878034525
"""