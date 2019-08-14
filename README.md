# DataCleaning
Practice Data Cleaning Using Python and Pandas In this dataset I will practice cleaning methods. 

According to IBM Data Scientists will spend 80% of the time will be spent cleaning the data

Here’s some typical reasons why data is missing:
1) User forgot to fill in a field. 
2) Data was lost while transferring manually from a legacy database. 
3) There was a programming error. 
4) Users chose not to fill out a field tied to their beliefs about how the results would be used or interpreted.

This is a much smaller dataset than what you’ll typically work with on a daily basis but it highlights a lot of real-world situations that we can expect to encounter on projects.

We need to understand different types of missing data from a statistics point of view.

The type of missing data will influence how you deal with filling in the missing values.

It’s a good idea to get a general feel for the data before cleaning and then organise a plan of action.

Below are some questions that we can ask ourselves before we begin:
1) What are the features?
2) What are the expected types (int, float, string, boolean)?
3) Is there obvious missing data (values that Pandas can detect)?
4) Is there other types of missing data that’s not so obvious (can’t easily detect with Pandas)?


## Step 1 - Import the CSV File 

Below I have imported Numpy and Pandas. df is short for dataframe and is used with Pandas to store the imported CSV file. 
.head is used to select the amount of rows required. 

      # Library Import
      import numpy as np 
      import pandas as pd 

      # read the csv file into pandas as dataframe
      df = pd.read_csv("propertydata.csv")

      # Look at the data lines 0-4. This can be a good option so we can get a feel for the data.
      print(df.head(5))


## Step 2 - Standard Missing Values
Standard missing values are values that Pandas can detect. 
isNull is used to represent the output True or False while not using this will display the value and output an NA in a blank space. 

    # Standard missing values
    print (df['ST_NUM'])
    print (df['ST_NUM'].isnull())

## Step 3 - Non Standard Missing Values
Missing values can possible have different formats. Pandas will detect "NA" but wont detect non-standard missing values such as "N/A" or "-".

This issue can arise when multiple users are inputting information and preference is different, I prefer to input "NA" but outers prefer to use "--" or "N/A". 

We can easily detect these different formats by creating a list so Pandas will detect them straight away. 

      # Making a list of missing value types
      missing = ["n/a", "na", "--"]
      df = pd.read_csv("propertydata.csv" , na_values = missing)

      # Print result
      print (df['NUM_BEDROOMS'])
      print (df['NUM_BEDROOMS'].isnull())

## Step 4 

