#!/usr/bin/env python
# coding: utf-8

# In[ ]:


analysis by inaara rajwani


# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df=pd.read_csv('Amazon Sale Report.csv',encoding='unicode_escape')


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.info()


# In[7]:


df.describe


# In[8]:


#remov
#e 19  New                 0 non-null       float64
 #20  PendingS            0 non-null       float64
df.drop(['New','PendingS'], axis=1, inplace=True)


# In[9]:


df.info()


# In[10]:


df.isnull()


# In[11]:


df.isnull().sum()


# In[12]:


#drop null values
df.shape


# In[13]:



df.dropna(inplace=True)


# In[14]:


df.shape


# In[15]:


df.columns


# In[16]:


#change datatype for ship-postal-code float->int
df['ship-postal-code']=df['ship-postal-code'].astype('int')


# In[17]:


#check whether the data type has changed or not
df['ship-postal-code'].dtype


# In[18]:


df['Date']=pd.to_datetime(df['Date'])#date object->datetime64[ns]


# In[19]:


df.columns


# In[20]:


df.info()


# In[21]:


#rename 'Qty' to quantity
df.rename(columns={'Qty':'Quantity'})


# In[22]:


df.describe()


# In[23]:


df.describe(include='object')


# # eda

# In[24]:


df.columns


# # size

# In[25]:


ax=sns.countplot(x='Size',data=df)


# In[26]:


pip install --upgrade matplotlib


# In[27]:


pip install --upgrade seaborn


# In[28]:


ax=sns.countplot(x='Size',data=df)

for bars in ax.containers:
    ax.bar_label(bars)
#from above graph you can see that most of the people buys M-size


# In[29]:


ax = sns.countplot(x='Size', data=df)
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center',
                xytext=(0, 10),
                textcoords='offset points')


# # groupby

# # it is used to grp data based on one or more columns in a dataframe

# In[30]:


s_qty = df.groupby(['Size'],as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)
sns.barplot(x='Size',y='Qty',data=s_qty)


# # as we can mmost quuantity bought size is M

# # courier status

# In[31]:


ax=sns.countplot(data=df,x='Courier Status',hue='Status')


# In[32]:


plt.figure(figsize=(11,10))
ax=sns.countplot(x='Courier Status',data=df,hue='Status')
plt.show()


# # as we can see major orders are  shipped

# # histogram

# In[33]:


df['Size'].hist()


# In[34]:


#category graph
df.info()


# In[35]:


#change datatype of ctegory column object->str
df['Category']=df['Category'].astype('str')
newcategory=df['Category']


# In[36]:


plt.figure(figsize=(10,5))
plt.hist(newcategory,bins=10,edgecolor='black')
plt.xticks(rotation=90)
plt.show()


# # as we can see from graph t shirt is the most bought item

# In[40]:


b2bcheck=df['B2B'].value_counts()
plt.pie(b2bcheck,labels=b2bcheck.index,autopct='%1.1f%%')
plt.show()


# 99.2% retailers,0.8%b2bbuyers

# In[41]:


x=df['Category']
y=df['Size']
plt.scatter(x,y)
plt.title("scatterplot")
plt.xlabel('x')
plt.ylabel('y')


# In[42]:


#plot to count cities by states
#count of buyers
plt.figure(figsize=(12,5))
sns.countplot(data=df,x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title("distribution of state in countplot")
plt.xticks(rotation=90)
plt.show()


# In[44]:


#to get top 10 states
top10=df['ship-state'].value_counts().head(10)
#count of buyers
plt.figure(figsize=(12,5))
sns.countplot(data=df[df['ship-state'].isin(top10.index)],x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title("distribution of state in countplot")
plt.xticks(rotation=90)
plt.show()


# In[ ]:


#most buyers are in buyers state


# conclusion :
#     as da suggest most of the customer base is in state maharastra mainly retailers ,fulfills orders through amazon ,high demand in tshrit (m size mostly preferred).

# https://youtu.be/1TmrFEHTg54?si=dLP9e3uw_R0zuKR4
#     reference concepts: https://www.youtube.com/@datacodewithsharad/playlists

# In[ ]:




