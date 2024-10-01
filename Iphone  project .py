#!/usr/bin/env python
# coding: utf-8

# # iphone sale analysis

# inaara rajwani

# In[1]:


pip install plotly


# In[2]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# In[3]:


data=pd.read_csv("apple_products.csv")
print(data)


# In[4]:


data


# In[5]:


print(data.isnull().sum())
#there are no missing values


# In[6]:


data.describe()


# In[7]:


print(data.describe())


# # top 10 iphones sold in india(iphones sales analysis in india) on the basis of rating

# In[8]:


highest_rated=data.sort_values(by=["Star Rating"],ascending =False)
highest_rated=highest_rated.head(10)
print(highest_rated['Product Name'])


# # lets c at the no of rating of highest rated iphone on flipcart

# # datavisualization 

# In[9]:


iphones=highest_rated["Product Name"].value_counts()
iphones


# In[10]:


labels=iphones.index
counts=highest_rated["Number Of Ratings"]
fig=px.bar(highest_rated,x=labels,y=counts,title="no.of rating of highest rated iphones ")
fig.show()


# # reviews on iphones,--
# 

# In[11]:


iphones=highest_rated["Product Name"].value_counts()
labels=iphones.index
counts=highest_rated["Number Of Reviews"]
fig=px.bar(highest_rated,x=labels,y=counts,title="reviews of highest rated iphones ")
fig.show()


# 
# # now lets c the sales therefore y=sale price and x=rating

# In[12]:


fig=px.scatter(data_frame=data,x="Number Of Ratings",y="Sale Price",
               size="Discount Percentage",trendline="ols",title="Relationship between sale price and no of ratings")
fig.show()


# In[13]:


fig=px.scatter(data_frame=data,x="Number Of Ratings",y="Discount Percentage",size="Sale Price",trendline="ols",title="Relationship between discount percentage and no of ratings")
fig.show()


# # objective -prices of iphones(iphone sales analysis)
# #whether data is clean or not?(pandas,numpy)
# #data analysis
# #datavisualize(bar,scatter)
# #model 
# #deployment
# 
