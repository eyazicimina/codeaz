path = "/home/mina5/PycharmProjects/codeaz-python/w12/"
import pickle
import pandas as pd
from sklearn.neural_network import BernoulliRBM
from sklearn.decomposition import PCA


df = pd.read_csv(path + "week6-quiz1.csv")
df = df.sample(n = 100000)
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df['Vehicle_Damage'] = df['Vehicle_Damage'].map({'No': 0, 'Yes': 1})
del df['Vehicle_Age']

print(df.shape)
pca = PCA(n_components=1)
pca = BernoulliRBM(n_components=3)
pca.fit(df)

pickle.dump( pca, open(path + "w12pickle.pickle", "wb") )
pd.DataFrame(pca.transform(df)).to_csv(path + "w12dr.csv")



dprojected = pd.read_csv(path + "w12dr.csv")
if 'Unnamed: 0' in dprojected.columns:
	del dprojected['Unnamed: 0']
pca = pickle.load( open(path + "w12pickle.pickle", 'rb') )
print(dprojected.shape)
print(dprojected)

print( pca.inverse_transform( dprojected ) )


