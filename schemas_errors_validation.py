## Linkedin Tutorial - Cleaning up data
# Source: https://www.linkedin.com/learning/data-cleaning-in-python-essential-training/finding-missing-data
#  Date: 11/17/2021
'''
Sources of error
machine errors
clock accuracy
faulty network transfer
corrupted data

Design errors
UI for collecting data
system design 
be precise in definitions


SCHEMA
define constraints on data
without a schema, constraints and requirement will be dispersed

JSON does not have formal schema 
Protocol Buffers has schema

VALIDATION
libraries to validate date in python
pydantic & marshmallow

pandera - statistical validation in pandas

techniques to avoid error
most errors are caused by humans
data validation and good gui can ensure good data
Country -> drop down
card number -> break out into a series of 4 digits to make it easier to spot errors
amount - only numbers
Date - drop down
Validate data before allowing form to proceed

'''

import pandas as pd
import pandera as pa
df = pd.read_csv('ships.csv')

# defines a schema
schema = pa.DataFrame({
	'name': pa.Column(pa.String),
	'lat':  pa.Column(pa.Float, nullable = True),
	'lon':  pa.Column(pa.Float, nullable = True),
})

# pandaera by default does not allow NULL values
schema.validate(df)


df = pd.read_csv('ships.csv')
df[df[.isnull().any(axis=1)]
