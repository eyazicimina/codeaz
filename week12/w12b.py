import pandas as pd
df = pd.read_csv("/home/mina5/PycharmProjects/codeaz-python/w12/archive(3)/Hotel_Room_attributes.csv")
print(df)
print(df.columns)
print(df.shape)

all_list=[]
for v in df['roomamenities'].values:
	v = str(v).split(";")
	v = [i.replace(':', '').strip() for i in v if len(i) > 0]
	for i in v:
		all_list.append(i)
roomamenities =list(set(all_list))
print(roomamenities)



cleanup = lambda value: [v.replace(':', '').strip() for v in str(value).split(";")]

df['roomamenities'] = df['roomamenities'].apply(cleanup)
#df['roomamenities'] = df['roomamenities'].apply(lambda value: cleanup(value))


for i in roomamenities:
	df[i] = df['roomamenities'].apply(lambda value: 1 if i in str(value) else 0)


del df['roomamenities']
df.to_csv("/home/mina5/PycharmProjects/codeaz-python/w12/archive(3)/w12.csv")
