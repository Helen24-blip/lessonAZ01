import pandas as pd



df = pd.read_csv('Bitcoin_Historical_Data.csv')

print(df.head())
print(df.info())
print(df.describe())


