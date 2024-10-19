import pandas as pd

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

lst1 = train.head(1)

lst2 = test.head(1)

print(lst1)
print(lst2)