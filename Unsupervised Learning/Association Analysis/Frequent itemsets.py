from mlxtend.preprocessing import TransactionEncoder

te = TransactionEncoder()
te_ary = te.fit_transform(dataset)
# convert the dataset into binary vectors where each element indicates the presence of absence of a specific item

import pandas as pd

df = pd.DataFrame(te_ary, columns=te.columns_)
# turn it into a pd table

from mlxtend.frequent_patterns import apriori

frequent_itemsets = apriori(df, min_support=0.6)
# get all frequent itemsets that have support higher than the min_support

frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
# use real names to represent the items

frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x)) 
# length of each frozenset

support = {}
for _, row in frequent_itemsets.iterrows():
    support[row['itemsets']] = row['support']

itemset = frozenset(['Onion', 'Eggs'])
print('Itemset: {0}. Support: {1}.'.format(itemset, support[itemset]))
# create a dict that maps the frequent itemset to its support
