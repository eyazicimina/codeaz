
import pandas as pd
import json
import pickle

path = "/home/mina5/PycharmProjects/codeaz-python/w12/archive(3)/"

prices = pd.read_csv(path + "hotel_price_min_max - Formula.csv")
print(prices)
attrs = pd.read_csv(path + "w12RoomAttributes.csv")
print(attrs)
details = pd.read_csv(path + "w12Details.csv")


df_merged = pd.merge(prices, attrs, on='hotelcode')

details = details.rename( columns={'hotelid': 'hotelcode'})

df_merged = pd.merge(df_merged, details, on='hotelcode')

"""
merged_df = pd.concat([df1, df2], axis=0)
merged_df = pd.merge(df1, df2, on='column_name')
merged_df = df1.join(df2, lsuffix='_df1', rsuffix='_df2')
merged_df = pd.merge(df1, df2, left_on='column_name_df1', right_on='column_name_df2')
"""

df_merged['average'] = (df_merged['max'] + df_merged['min']) / 2

df_merged.to_csv(path + "w12merged.csv")


df_merged.corr().to_csv(path + "w12corr.csv")

