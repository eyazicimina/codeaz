import numpy as np
from sklearn import tree
import graphviz
import matplotlib.pyplot as plt
import pandas as pd
#: Load tthe dataset
df = pd.read_csv("/home/mina5/Desktop/codeacedemy/week6-quiz1.csv")
#: Shrink the dataset
df = df.sample(100000)
# FACTOR 1: Dataset kucukse, dataset cok kucuk bir parca ise bizi yaniltabilir!
# In datascience, YOU DO NOT NEED TO USE ALL YOUR DATASET if it is too big

#: Transform the features into numeric
df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})
df['Vehicle_Age'] = df['Vehicle_Age'].map({'> 2 Years': 2, '1-2 Year': 1, '< 1 Year': 0})
df['Vehicle_Damage'] = df['Vehicle_Damage'].map({'Yes': 1, 'No': 0})
#: Shuffle
df = df.sample(frac = 1.0)
#: Split into train/test randomly
limit = int(len(df) * 0.70) # FAIZ 70, 30 ==> train  (80, 20)
TRAIN = df[:limit]
TEST = df[limit:]

#: Split the data set to [input and output]
y = TRAIN['Response']
x = TRAIN.drop(columns=['Response'])


test_y = TEST['Response']
test_x = TEST.drop(columns=['Response'])


#: Create an algorithm
from sklearn.ensemble import RandomForestClassifier
#clf = tree.DecisionTreeClassifier(max_depth = 6)
clf = RandomForestClassifier(max_depth=6, random_state=0)

#: Train the algorithm to produce a "model"
# fit = train, egitmek
clf.fit( x, y )

prediction = clf.predict( x )
a = prediction == y
print( "TRAIN ACCURACY",  np.mean( a ) ) # .8791

test_prediction = clf.predict( test_x )
b = test_prediction == test_y
print( "TEST ACCURACY",  np.mean( b ) ) # .8779

test_x[ 'pred' ] = test_prediction
test_x[ 'Response' ] = test_y

test_x['Result'] = test_x['pred'] == test_x['Response']
test_x['Result'] = test_x['Result'].astype(int)
test_x['TP'] = test_x.apply(lambda row: 1 if row['pred'] == 1 and row['Response'] == 1 else 0 , axis = 1)
test_x['FP'] = test_x.apply(lambda row: 1 if row['pred'] == 1 and row['Response'] == 0 else 0 , axis = 1)
test_x['TN'] = test_x.apply(lambda row: 1 if row['pred'] == 0 and row['Response'] == 0 else 0 , axis = 1)
test_x['FN'] = test_x.apply(lambda row: 1 if row['pred'] == 0 and row['Response'] == 1 else 0 , axis = 1)


test_x.to_csv("w8_test_x.csv")

# IF THEY ARE TOO CLOSE, THERE IS NO OVERFITTING!

# Accuracy? How good my model is?

# MEMORIZE, EZBERLEME, OVERFITTING


# UNDERFIT = HENUZ TAM OGRENMEDI, VEYA OGRENEMIYOR

### ==============================
# WHAT ARE THE FACTORS OF ACCURACY
# HOW DO WE INRCEASE ACCURACY?

### ==============================












import sys
sys.exit(1)
# CLASSIFICATION PROBLEM


#: Create an algorithm
clf = tree.DecisionTreeClassifier(max_depth = 4)
#: Train the algorithm to produce a "model"
# fit = train, egitmek
clf.fit( x, y )


for i in range(len(x.columns)):
  print(i, x.columns[i], clf.feature_importances_[i])


# ==================================================================
text_representation = tree.export_text(clf, feature_names=list(x.columns))
print(text_representation)

# ==================================================================
fig = plt.figure(figsize=(35,27))
_ = tree.plot_tree(clf,
                   feature_names=x.columns,
                   class_names=['churn', 'no churn'],
                   filled=True)

plt.show()

# ==================================================================
# Draw tree to a file
dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=x.columns,
                                class_names=['churn', 'no churn'],
                                filled=True)

# Draw graph
graph = graphviz.Source(dot_data, format="png")
graph.render("decision_tree_graphivz")
# ==================================================================






"""
|--- Vehicle_Damage <= 0.50
|   |--- Policy_Sales_Channel <= 4.00
|   |   |--- Age <= 54.50
|   |   |   |--- Region_Code <= 38.50
|   |   |   |   |--- class: 0
|   |   |   |--- Region_Code >  38.50
|   |   |   |   |--- class: 1
|   |   |--- Age >  54.50
|   |   |   |--- class: 1
|   |--- Policy_Sales_Channel >  4.00
|   |   |--- Previously_Insured <= 0.50
|   |   |   |--- Policy_Sales_Channel <= 161.50
|   |   |   |   |--- class: 0
|   |   |   |--- Policy_Sales_Channel >  161.50
|   |   |   |   |--- class: 0
|   |   |--- Previously_Insured >  0.50
|   |   |   |--- class: 0
|--- Vehicle_Damage >  0.50
|   |--- Age <= 26.50
|   |   |--- Policy_Sales_Channel <= 137.50
|   |   |   |--- Age <= 24.50
|   |   |   |   |--- class: 0
|   |   |   |--- Age >  24.50
|   |   |   |   |--- class: 0
|   |   |--- Policy_Sales_Channel >  137.50
|   |   |   |--- Annual_Premium <= 84450.00
|   |   |   |   |--- class: 0
|   |   |   |--- Annual_Premium >  84450.00
|   |   |   |   |--- class: 1
|   |--- Age >  26.50
|   |   |--- Age <= 52.50
|   |   |   |--- Previously_Insured <= 0.50
|   |   |   |   |--- class: 0
|   |   |   |--- Previously_Insured >  0.50
|   |   |   |   |--- class: 0
|   |   |--- Age >  52.50
|   |   |   |--- Age <= 60.50
|   |   |   |   |--- class: 0
|   |   |   |--- Age >  60.50
|   |   |   |   |--- class: 0

"""







import sys
sys.exit(1)
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


