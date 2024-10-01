#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


iris=pd.read_excel(r'iris.xlsx')


# In[3]:


print(iris.head())


# In[4]:


print(iris.tail())


# In[5]:


#heavy coding --> moderate coding --> no coding
#Scatter Plot using Matplotlib
fig,ax=plt.subplots()
#scatter the sepal length against sepal width
ax.scatter(iris['Petal_length'], iris['Sepal_width'])
#set a title and labels
ax.set_title("Iris Datasets")
ax.set_xlabel('Sepal_length')
ax.set_ylabel('Sepal_width')


# In[6]:


#Line chart using Matplotlib
columns=iris.columns.drop(['Species_name'])
#create x data
x_data=range(0, iris.shape[0])
#create figure and axis
fig,ax=plt.subplots()
#plot each column
for column in columns:
    ax.plot(x_data, iris[column], label=column)
#set title and legend
ax.set_title('Iris Dataset')
ax.legend()


# In[7]:


#Scatter plot using seaborn
import seaborn as sns
sns.scatterplot(x='Sepal_length', y='Sepal_width', data=iris)


# In[8]:


#Scatter plot using seaborn
sns.scatterplot(x='Sepal_length',y='Sepal_width',hue='Species_name',data=iris)


# In[9]:


#Line chart using seaborn
sns.lineplot(data=iris.drop(['Species_name'], axis=1))


# In[10]:


#Histogram using seaborn6
sns.distplot(wine_reviews['points'],bins=10, kde=True)


# In[ ]:


corr = iris.corr()
fig, ax = plt.subplots()
# create heatmap
im = ax.imshow(corr.values)

# set labels
ax.set_xticks(np.arange(len(corr.columns)))
ax.set_yticks(np.arange(len(corr.columns)))
ax.set_xticklabels(corr.columns)
ax.set_yticklabels(corr.columns)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        text = ax.text(j, i, np.around(corr.iloc[i, j], decimals=2),
                       ha="center", va="center", color="black")


# In[ ]:


#heatmap
sns.heatmap(iris.corr(),annot=True)


# In[ ]:


#face grid using seaborn 
g=sns.FacetGrid(iris,col='Species_name')#generate o/p according to species name
g=g.map(sns.kdeplot,'Sepal_length')


# In[ ]:


#pairplot 
sns.pairplot(iris)


# In[ ]:


#employ data
#bar for gender,corelation,avearge


# In[ ]:





# In[ ]:




