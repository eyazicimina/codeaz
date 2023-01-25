import matplotlib.pyplot as plt
import sys
import pandas as pd

df = pd.read_csv("w11DR.csv")
print(df)

del df['Geography']
df['Gender'] = df['Gender'].map({'Female': 1, 'Male': 0})
from sklearn.decomposition import PCA

#df = df[ df['Balance'] < 500 ] # balance olmayanlar
print(df.shape)
pca = PCA(n_components=2)
pca.fit(df)
print(pca.explained_variance_ratio_.cumsum())


# sys.exit(1)

pcadata = pca.transform( df )
pcadata = pd.DataFrame(pcadata)
pcadata.columns = ['pca0', 'pca1']
# kmeans




df['pca0'] = pcadata['pca0']
df['pca1'] = pcadata['pca1']

print( df[ df['pca0'] < -50000 ] )
df[ df['pca0'] < -50000 ].to_csv("w11out.csv")
df[ df['pca0'] > -50000 ].to_csv("w11out2.csv")

print( df[ df['pca0'] < -50000 ].mean().to_dict() )
print( df[ df['pca0'] > -50000 ].mean().to_dict() )




plt.scatter( df['pca0'], df['pca1'] )
plt.show()




# ====================================
# ====================================
# ====================================
# ====================================
# ====================================
# ====================================

sys.exit(1)
pcadata = pca.transform( df )
pcadata = pd.DataFrame(pcadata)



print(pcadata)

pcadata.columns = ['pca0', 'pca1']
print(pcadata['pca0'].corr( pcadata['pca1']))


pcadata2 = pcadata.copy()
pcadata2['pca0-abs'] = pcadata2['pca0'].abs()
pcadata2['pca1-abs'] = pcadata2['pca1'].abs()
pcadata2['sum'] = pcadata2['pca1-abs'] + pcadata2['pca0-abs']
pcadata2.sort_values( by = ['sum'], inplace=True )
print("pcadata")
print(pcadata2)


x1 = pcadata2.iloc[0]['pca0']
y1 = pcadata2.iloc[0]['pca1']
x2 = pcadata2.iloc[20]['pca0']
y2 = pcadata2.iloc[20]['pca1']

distance = math.sqrt( math.pow(x1-x2, 2 ) + math.pow(y1-y2, 2) )


print("INVERSE MINIMUM",  pca.inverse_transform( [ [-64.590961, 1636.717186] ]  ) )
print("DATAFRAME MEAN", df.mean().to_dict())

print("EN UZAK", pca.inverse_transform([[119922.735405, 108993.779400]] ))









print("MEAN", pca.transform( [df.mean() ] ))
# MEAN [[0. 0.]]



sys.exit(1)
print(pcadata[0])

print( pca.inverse_transform( pcadata[0] ) )


# 10 feature - column
# 10 sentence ile define !


# 1 cumle ile define etmek istesem


print( pca.components_[0] )
print( pca.components_[1] )



