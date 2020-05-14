import pandas as pd

my_file = pd.read_csv('diamonds.csv')

print('count, minimum and maximum price for each cut are : ')
print(my_file.groupby('cut').price.agg(['count','min','max']))