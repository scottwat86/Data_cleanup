## linkedin tutorial 
## source https://www.linkedin.com/learning/data-cleaning-in-python-essential-training/why-is-clean-data-important
# Date: 11/11/2021

## Notes
'''
Cleaning up your data in Python

Bad Data

Null or missing values
duplicates
bad values, wrong type, extreme/unrealistic values

'''

## NULL VALUES
import pandas as pd
df = pd.read_csv('cart.csv', parse_dates=['date']) # loads and parses the data

df.types
df['amount'].astype('Int32') # amount column is float but csv only has integers because there are missing values
df.isnull() # Generate a boolean mask indicating missing values
df.isnull().any(axis=1) # mask for every row

df.dropna() # Return a filtered version of data, dropping whole row 
df.fillna(0) # replaces all Nulls with 0


## BAD VALUE DETECTION
# load data and sample 10 roms
df = pd.read_csv('metrics.csv', parse_dates=['time']) 
df.sample(10)

# group by and then describe with STD/Mean/min/25/50
df.groupby('name').describe()  

# counts each category, great way to find problems with categorical data
df['name'].value_count()  

# graphing to spot problems
df.pivot(index='time', columns='name').plot(subplots=True) 

# defining a query to find values that are bad based on criteria
df.query('name == "cpu" & (value < 0 | value > 100') #

## OUTLIERS
# Standard score , Z-Score, distance from mean in teams of standard deviation
# https://en.wikipedia.org/wiki/Standard_score

# finds outliers that are more than 2 standard deviations outside of mean
mem = df[df['name'] == 'mem']['value']
z_score = (mem - mem.mean())/mem.std() 
bad_mem = mem[z_score.abs() > 2]

## DUPLICATES
# load data
df = pd.read_csv('cart.csv', parse_date=['date'])

# finds duplicate for every row
df.duplicated()
df.duplicated(['date', 'name'])


