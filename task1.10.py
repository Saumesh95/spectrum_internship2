import pandas as pd 
my_file = pd.read_csv("diamonds.csv")

print(f"the no.of rows and colummns are {my_file.shape} respectively")

missing = my_file.isnull().sum()
print(f'missing values in each of the rows of  each column are : {missing}')
removed = my_file.dropna(how='any').shape
print(f'no of rows after removing the rows with empty files are : {removed}')