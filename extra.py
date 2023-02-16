


data = pd.read_csv("..")

pca = PCA(n_components=2)
pca.fit(x)




print(pca.explained_variance_ratio_)
[0.60... 0.40...]

pca.inverse_transform( [random.random()] )


row1 = data.iloc[26]
row2 = data.iloc[9906]

transform1 = pca.transform( [row1] )[ 0 ]
transform2 = pca.transform( [row2] )[ 0 ]

sum(transform1 * transform1) > THRESHOLD ==> ANOMALY


def weightedEuclidean(transform1, transform2, weights):
    distance = 0
    for i in range(len(transform1)):
        distance += np.power(transform1[i] - transform2[i], 2.0) * weights[i]
    return np.sqrt(distance/sum(weights))


weightedEuclidean( transform1, transform2, pca.explained_variance_ratio_)



1- dimension reduction
    1a- [target low correlated variable] [ 10 tane variable, low correlated 0.02, 0.05, 0.10]
2- anomaly detection [!!]
3- distance
4- visualization
5- [model oncesi] ==> [classification, regression, clustering]
6- how complex a dataset is!!!
7- data generation





SELECT *
CASE
    WHEN RANDOM() > 0.40 THEN 'TRAIN'
    ELSE 'TEST'
END AS HangiKume
FROM OrderDetails; 
