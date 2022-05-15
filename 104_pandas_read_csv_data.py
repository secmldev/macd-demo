#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:


pd.read_csv('AAPL.csv')


# In[3]:


data = pd.read_csv('data/AAPL.csv')


# In[5]:


data.describe()


# In[6]:


data.plot()


# In[7]:


data['Open'].plot()


# In[11]:


data.info()


# In[9]:


data.columns


# In[10]:


data.dtypes


# In[14]:


data.describe()


# In[ ]:





# In[ ]:





# In[15]:


data.info()


# In[16]:


data.describe


# In[17]:


data.info


# In[ ]:




