

#! <preprocess>

# rebalancing
ones = df[ df['target'] == 1].sample(frac = 0.5)
zeros = df[ df['target'] == 0]
pd.concat( [ones,  zeros] )

# target normalization
df['price'] = df['price'] - df['price'].mean()


# algortihm selection
# voting
# parameter variations
# threshold
# cost matrix
# ....
# save model to pickle

