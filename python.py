# Library Import
import numpy as np 
import pandas as pd 



# read the csv file into pandas as dataframe
df = pd.read_csv("propertydata.csv")

# Look at the data lines 0-4
#print(df.head(5))

# Standard missing values
#print (df['ST_NUM'])
#print (df['ST_NUM'].isnull())

# Look at num_bedrooms column
#print (df['NUM_BEDROOMS'])
#print (df['NUM_BEDROOMS'].isnull())

# Detecting numbers 
cnt=0
for row in df['OWN_OCCUPIED']:
    try: # exception handling
        int(row) # change the entry to an integer

        # .loc is the preferred Pandas method for modfiying entries in place
        df.loc[cnt, 'OWN_OCCUPIED']=np.nan # If we can change the entry to a missing value using Numpy’s np.nan.
        
    except ValueError: #  exception handling
        pass # If we cant change the entry to a missing value using Numpy’s np.nan then pass
    cnt+=1

    # Total missing values for each feature
print (df.isnull().sum())
