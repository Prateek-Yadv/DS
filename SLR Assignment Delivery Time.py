#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import statsmodels.formula.api as smf
Dt = pd.read_csv('C:/Users/prate/Downloads/Assignment/SLR/delivery_time.csv')
Dt.head()


# In[2]:


Dt.info()


# In[3]:


Dt.corr()


# In[4]:


import seaborn as sns
sns.distplot(Dt['Delivery Time'])


# In[5]:


import seaborn as sns
sns.distplot(Dt['Sorting Time'])


# Fitting a Linear Regression Model

# In[18]:


sns.regplot(x="dt", y="st", data=Dt);


# In[10]:


import statsmodels.formula.api as smf


# In[22]:


model = smf.ols("dt~st",data = Dt).fit()


# In[20]:


Dt.rename(columns={'Delivery Time':'dt','Sorting Time':'st'},inplace= True)


# In[21]:


Dt.head()


# In[24]:


model.params


# In[25]:


(model.tvalues, '\n', model.pvalues)


# In[26]:


(model.rsquared,model.rsquared_adj)


# In[32]:


model.predict(Dt)


# In[33]:


#crosschecking manually
6.58+1.64*9 #sorting time=10


# In[ ]:




