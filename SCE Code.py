#!/usr/bin/env python
# coding: utf-8

# In[74]:


#Import everything we need
import pandas as pd
import numpy as np
import math
from datetime import datetime, timedelta
from pytz import timezone
import pytz

#Display the full dataframe
pd.set_option("display.max_rows", None, "display.max_columns", None)

#Read in the Excel File
df = pd.read_excel (r'/Users/reid/Downloads/test 2021-05-06 start.xlsx')


# In[75]:


#Create new columns
df["Timestamp flag"] = " "
df["data qc flag VTWS_AVG"] = " "


# In[76]:


#While loop that marks columns without VTWS_AVG as Erroneous
x=0
while x<len(df):
    if math.isnan(df["VTWS_AVG"].values[x]):
        df.at[x,"data qc flag VTWS_AVG"]="Erroneous"
        x+=1
    else:
        x+=1


# In[77]:


#This function checks for NaN values in columns that are type string
def isNaN(string):
    return string != string


# In[78]:


#Creates new rows to fill in where there are missing timestamps
df['time'] = pd.to_datetime(df['time'],utc=True)
df['time'] = df['time'].dt.tz_convert('US/Central')

df = df.set_index('time').asfreq('1H')


# In[79]:


#Adds in the missing ids, and flags the newly added columns
x=0
while x<len(df):
    if isNaN(df["data qc flag VTWS_AVG"].values[x]) is True:
        df.iloc[x,0]=df.iloc[x-1,0]+1
        df.iloc[x,6]='missing from original input dataset'
        df.iloc[x,7]='Erroneous'
        x+=1
    else:
        x+=1


# In[80]:


#Can see outcome, scroll to id 801 to see the code work
df


# In[ ]:




