import pickle
from w12d_preprocess import *


yeni_gelen_row = {'Gender':'Male',
'Age':44,
'Driving_License':1,
'Region_Code':28,
'Previously_Insured':0,
'Vehicle_Age':'> 2 Years',
'Vehicle_Damage':'Yes',
'Annual_Premium':40454,
'Policy_Sales_Channel':26,
'Vintage':217}

yeni_gelen_row = prepareRow( yeni_gelen_row )
print(yeni_gelen_row)
yeni_gelen_row = list( yeni_gelen_row.values() )

file = open('model.pickle', 'rb')
# dump information to that file
model = pickle.load(file)

# close the file
file.close()

sonuc = model.predict( [yeni_gelen_row] )
sonuc = sonuc[0]
print("sonuc", sonuc)

