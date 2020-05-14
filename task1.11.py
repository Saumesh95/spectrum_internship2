import pandas as pd 



my_file = pd.read_csv('diamonds.csv')

print(f'the duplicate rows of the file are : {my_file.duplicated().sum()}')