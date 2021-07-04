import pandas as pd

df = pd.read_csv('C:\GitHub\KeithPandas\pandas\pokemon_data.csv', delimiter=',')
# print(df)  "print dataset "

print(df.head(4))  # top 4 lines

print(df.tail(4))  # bottom 4 lines

print(df.columns)  # print list of columns

print(df['Name'][0:5])  # this command will give top 5 names from header

print(df[['Name', 'Type 1', 'Type 2']])

print(df.iloc[1:10])  # this is like limit in sql

print(df.iloc[
          2, 1])  # first value represent row and second value represent column,this command will print 2nd row first
# 1 column

for index, row in df.iterrows():
    """This will print each row in grid"""
    if index < 2:
        print(index, row)
        # to print specific column from row

# filtering the data

# with loc we can  Access a group of rows and columns by label(s) or a boolean array

print(df.loc[df['Type 1'] == "Grass"])

# this will generate descriptive statistics
print(df.describe())

# descriptive statistics for particular columns

print(df.describe()['HP']['count'])

# sorting

print(df.sort_values('Name', ascending=False))
# we need to specify the columns in the list if we need more than one column
print(df.sort_values(['Type 1', 'Name'], ascending=False))

# We can specify sorting individually

print(df.sort_values(['Name', 'Type 1'], ascending=[1, 0]))

df['Total'] = df['HP'] + df['Attack'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

print(df)

print(df.columns)
print(df.sort_values('Total', ascending=False))

# Droping column

df.drop(columns='Total')
print(df.columns)

# another way of adding
"including all the columns and from all columns take columns from 4 to 9 and then adding horizontally"

df['Total'] = df.iloc[:, 4:10].sum(axis=1)

print(df)

cols = list(df.columns.values)

df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df.head(5))

df.to_csv('C:\GitHub\KeithPandas\pandas\Result.csv', index=0)

# Filtering the data

print(df.loc[df['Type 1'] == 'Grass'])

# filtering on multiple condition

print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')])

# print(df.loc[(df['Name'] == 'Venusaur') & (df['Total'] >= 300)])
import re

print(df.loc[df['Name'].str.contains('bulbasaur|VEnusaur', flags=re.IGNORECASE)])

# conditional changes
# if type 1=Green then change Type 1 to GREEN

df.loc[df['Type 1'] == 'Grass', 'Type 1'] = 'GREEN'

print(df)

df.loc[df['Name'] == 'Venusaur', ['Legendary', 'Generation']] = 'TESTING'
# print(df.loc[df['Name'] == 'Venusaur'])

# Aggregation
# group by

print(df.groupby(['Type 1']).count())

