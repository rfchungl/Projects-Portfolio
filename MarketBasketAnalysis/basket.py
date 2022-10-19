import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

#path to Bread Basket csv
bread = pd.read_csv(r"/Users/RuKai/Desktop/basket.csv")
df = bread.groupby(['Transaction','Item']).size().reset_index(name='count')
breadbasket = (df.groupby(['Transaction', 'Item'])['count']
          .sum().unstack().reset_index().fillna(0)
          .set_index('Transaction'))

#transform values into dataframe
def df(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1
dataset = breadbasket.applymap(df)
frequent_itemsets = apriori(dataset, min_support=0.01, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift")
rules.sort_values('confidence', ascending = False, inplace = True)
rules.head()
print(rules)
