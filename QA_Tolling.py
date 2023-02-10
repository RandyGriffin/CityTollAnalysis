#!/usr/bin/env python
# coding: utf-8

# In[93]:


import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from scipy.stats import pearsonr,spearmanr
import warnings
warnings.filterwarnings('ignore') 


# In[94]:


df = pd.read_excel('Quality_Analyst_Tolling_Data_1.xlsx') #Import clean data
df.head()


# In[95]:


df2 = pd.read_excel('Tolling_entry_exit.xlsx')
df2.head()


# In[96]:


df.dtypes #Checks the data types for each column


# In[97]:


df2.dtypes


# In[98]:


df.describe() #Calculates the summary statistics of the numerical columns


# In[99]:


df['Date'] =  pd.to_datetime(df['Date'])
df['Day of Week'] =df['Date'].dt.strftime('%A')
df.head()


# In[ ]:





# In[100]:


#Visualization
df['Fee'].plot(kind="hist", title="Frequency of Fees")


# In[101]:


from sklearn.preprocessing import OneHotEncoder
object_cols = ['Vehicle Type']
OH_encoder = OneHotEncoder(sparse=False)
OH_cols = pd.DataFrame(OH_encoder.fit_transform(df[object_cols]))
OH_cols.index = df.index
OH_cols.columns = OH_encoder.get_feature_names()
df_final = df.drop(object_cols, axis=1)
df = pd.concat([df_final, OH_cols], axis=1)


plt.figure(figsize=(12, 6))
sns.heatmap(df.corr(),
            cmap='BrBG',
            fmt='.2f',
            linewidths=2,
            annot=True)


# In[102]:


plt.figure(figsize=(12,6))
sns.heatmap(df.corr(),linewidths=1)


# In[ ]:





# In[103]:


#Calculates the total revenue for each toll plaza
df['Fee'].sum()


# In[104]:


#Group data by Facility and calculate the mean
df.groupby('Facility')['Fee'].mean()


# In[105]:


#Group data by Direction, calculates total number of transactions per group
df.groupby('Direction').size()


# In[ ]:




