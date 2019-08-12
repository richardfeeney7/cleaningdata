# Library Import
import numpy as np 
import pandas as pd 

# read the csv file into pandas as dataframe
df = pd.read_csv("propertydata.csv")

# Look at the data lines 0-4
print(df.head(5))

# Standard missing values
print (df['ST_NUM'])
print (df['ST_NUM'].isnull())