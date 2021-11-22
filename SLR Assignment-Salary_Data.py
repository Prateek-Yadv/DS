#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import statsmodels.formula.api as smf
salary = pd.read_csv('C:/Users/prate/Downloads/Assignment/SLR/Salary_Data.csv')
salary.head()


# In[5]:


salary.info()


# In[7]:


salary.corr()


# In[8]:


import seaborn as sns
sns.distplot(salary['Salary'])


# In[12]:


import seaborn as sns
sns.distplot(salary['YearsExperience'])


# Fitting a Linear Regression Model

# In[14]:


sns.regplot(x="Salary", y="YearsExperience", data=salary);


# In[15]:


import statsmodels.formula.api as smf


# In[16]:


model = smf.ols("Salary~YearsExperience",data = salary).fit()


# In[17]:


model.params


# In[18]:


(model.tvalues, '\n', model.pvalues)


# In[19]:


(model.rsquared,model.rsquared_adj)


# In[20]:


model.predict(salary)


# In[21]:


#crosschecking manually
25792.200+9449.962*2.2 #sorting time=2.2 yrars


# In[ ]:




