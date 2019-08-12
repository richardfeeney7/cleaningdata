# DataCleaning
Practice Data Cleaning Using Python and Pandas In this dataset I will practice cleaning methods. According to IBM Data Scientists will spend 80% of the time will be spent cleaning the data

Here’s some typical reasons why data is missing:
User forgot to fill in a field. Data was lost while transferring manually from a legacy database. There was a programming error. Users chose not to fill out a field tied to their beliefs about how the results would be used or interpreted.
This is a much smaller dataset than what you’ll typically work with on a daily basis but it highlights a lot of real-world situations that we can expect to encounter on projects.

## Step 1 - Import the CSV File 

      # Library Import
      import numpy as np 
      import pandas as pd 

      # read the csv file into pandas as dataframe
      df = pd.read_csv("propertydata.csv")

      # Look at the data lines 0-4
      print(df.head(5))

## Step 2 - Standard Missing Values
Standard missing values are values that Pandas can detect. isNull is used to represent the output True or False

    # Standard missing values
    print (df['ST_NUM'])
    print (df['ST_NUM'].isnull())

