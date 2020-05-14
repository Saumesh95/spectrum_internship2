import pandas as pd 
my_file = pd.read_csv('diamonds.csv')
sample = my_file.sample(frac=0.75, random_state=99)
print("the 75 percent of the sample data frame without replacement is : ")
print(sample)
remaining = my_file.loc[~my_file.index.isin(sample.index), :]
print('the remaining dataframe is : ')
print(remaining)
