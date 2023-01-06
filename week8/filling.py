import pandas as pd
import random
import numpy as np

def randomlyDelete(df: pd.DataFrame):
  for c in df:
    R = random.random() * 0.05 # ==> [0, 0.05]
    df[c] = df[c].apply(lambda value: None if random.random() < R else value) # FAIZ 2 ==> NONE, 98 ==> value
  return df


def fillAllVariables(df: pd.DataFrame) -> pd.DataFrame:
  def fillCategoricVariables() -> pd.DataFrame:
    for c in df.select_dtypes(include=['object']).columns:
      df[c] = df[c].fillna(df[c].mode()[0])
    return df

  def fillNumericVariables():
    for c in df.select_dtypes(exclude=['object', 'datetime', 'datetime64']).columns:
      df[c] = df[c].fillna(df[c].mean())
    return df

  df = fillCategoricVariables()
  df = fillNumericVariables()
  return df



def compareDataset(df1: pd.DataFrame, df2: pd.DataFrame) -> float:
  success = []
	# CATEGORIC
  for c in df1.select_dtypes(include=['object']).columns:
    success.append(np.mean(df1[c] == df2[c])) # 95 ayni, same,
	# NUMERIC
	for c in df1.select_dtypes(exclude=['object', 'datetime', 'datetime64']):
		success.append( 1.0 - mape( df1[c], df2[c] ) )

	return np.mean(success)

df = pd.read_csv("/home/mina5/Desktop/codeacedemy/week6-quiz1.csv")
old = df.copy()
df = randomlyDelete(df)
df = fillAllVariables(df)

print( compareDataset(old, df) ) # %98.7




