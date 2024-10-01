#!/usr/bin/env python
# coding: utf-8

# In[ ]:


inaara rajwani


#  It is a project of Data Analysis with Python or you can say, Data Science with Python.
# 
# The commands that we used in this project :
# 
# * head() - It shows the first N rows in the data (by default, N=5).
# * tail () - It shows the last N rows in the data (by default, N=5).
# * shape - It shows the total no. of rows and no. of columns of the dataframe.
# * size - To show No. of total values(elements) in the dataset.
# * columns - To show each Column Name.
# * dtypes - To show the data-type of each column.
# * info() - To show indexes, columns, data-types of each column, memory at once.
# * value_counts - In a column, it shows all the unique values with their count. It can be applied on a single column only.
# * unique() - It shows the all unique values of the series.
# * nunique() - It shows the total no. of unique values in the series.
# * duplicated( ) - To check row wise and detect the Duplicate rows.
# * isnull( ) - To show where Null value is present.
# * dropna( ) - It drops the rows that contains all missing values.
# * isin( ) - To show all records including particular elements.
# * str.contains( ) - To get all records that contains a given string.
# * str.split( ) - It splits a column's string into different columns.
# * to_datetime( ) - Converts the data-type of Date-Time Column into datetime[ns] datatype.
# * dt.year.value_counts( ) - It counts the occurrence of all individual years in Time column.
# * groupby( ) - Groupby is used to split the data into groups based on some criteria.
# * sns.countplot(df['Col_name']) - To show the count of all unique values of any column in the form of bar graph.
# * max( ), min( ) - It shows the maximum/minimum value of the series.
# * mean( ) - It shows the mean value of the series.
# 
# 
# 
# i shall be doing following things ::
# * Creating New Columns & Dataframe
# * Filtering (Single Column & Multiple Columns)
# * Filtering with And and OR
# * Seaborn Library - Bar Graphs
Task. 1) Is there any Duplicate Record in this dataset ? If yes, then remove the duplicate records.
Task. 2) Is there any Null Value present in any column ? Show with Heat-map.
Q. 1) For 'House of Cards', what is the Show Id and Who is the Director of this show ?
Q. 2) In which year the highest number of the TV Shows & Movies were released ? Show with Bar Graph.
Q. 3) How many Movies & TV Shows are in the dataset ? Show with Bar Graph.
Q. 4) Show all the Movies that were released in year 2000.
Q. 5) Show only the Titles of all TV Shows that were released in India only.
Q. 6) Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?
Q. 7) Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom".
Q. 8) In how many movies/shows, Tom Cruise was cast ?
Q. 9) What are the different Ratings defined by Netflix ?
Q. 9.1) How many Movies got the 'TV-14' rating, in Canada ?
Q. 9.2) How many TV Shows got the 'R' rating, after year 2018 ?
Q. 10) What is the maximum duration of a Movie/Show on Netflix ?
Q. 11) Which individual country has the Highest No. of TV Shows ?
Q. 12) How can we sort the dataset by Year ?
Q. 13) Find all the instances where: Category is 'Movie' and Type is 'Dramas' or Category is 'TV Show' & Type is 'Kids' TV'.
# In[1]:


import pandas as pd 
data=pd.read_csv(r'8. Netflix Dataset.csv')
data


# In[2]:


data.head(5)


# In[3]:


data.tail()


# In[4]:


data.describe()


# In[5]:


data.info()


# In[6]:


data.size


# In[7]:


data.columns


# # 1)remove duplicates if present

# In[8]:


data.head(2)


# In[9]:


data[data.duplicated()]


# In[10]:


#removing 


# In[11]:


data.drop_duplicates(inplace=True)


# In[12]:


data.info()


# # is thr any null value in column if yes show with heatmap

# In[13]:


data.head(2)


# In[14]:


data.isnull()


# In[15]:


data.isnull().sum()


# now for heatmap we use seaborn 
# what is seaborn?

# In[16]:


import seaborn as sns


# In[17]:


sns.heatmap(data.isnull())


# # for "13 Reasons Why" what is the show id and who is the director of that show?

# In[18]:


data.head(1)


# In[19]:


# way1
data[data['Title'].isin(['13 Reasons Why'])]


# In[20]:


#way2
data[data['Title'].str.contains('13 Reasons Why')]


# # in which year higherst number of tv shows and movies were released ? show with bar graph

# In[21]:


data.dtypes


# In[22]:


data.head(2)


# # therfore conversion in datetime format is needed
# #to_datetime

# In[23]:


# therfore conversion in datetime format is needed
#to_datetime
data['date_New']=pd.to_datetime(data['Release_Date'])


# In[24]:


data.head(1)


# In[25]:


data.info()


# # find and count occurance of all individual year in date column

# In[26]:


data['date_New'].dt.year.value_counts()


# # bar graph

# In[27]:


data['date_New'].dt.year.value_counts().plot(kind='bar')


# 
# # we can use groupby to grp shows and movies

# In[28]:


data.groupby('Category').Category.count()


# # now plot the graph and we use matplotlib library 

# In[29]:


import matplotlib.pyplot as plt


# # in order to show the count of unique vlaue in the from of bar graph

# In[30]:


sns.countplot(data=data,x='Category')


# # show all movies that where released in 2020

# # creating a new column

# In[31]:


data.head(1)


# In[32]:


data['year']=data['date_New'].dt.year


# In[33]:


data.head(1)


# In[34]:


data.info()


# # here we want for year 2020 therefore we filter it

# In[35]:


#filtering 
data[(data['Category']=='Movie') & (data['year']==2020)]
#we get movies from 2020


# In[36]:


df1=data[(data['Category']=='Movie') & (data['year']==2020)]


# In[37]:


df1.shape


# # show all the title of all tv shows that were released in india only

# In[38]:


data.head(2)


# In[39]:


data[(data['Category']=='TV Show') & (data['Country']=='India')]['Title']


# In[40]:


data[(data['Category']=='Movie') & (data['Country']=='India')]['Title']


# # show top 10 director who gave the highest numbers of tv shows and novies to netflix

# In[41]:


#value_count
data['Director'].value_counts().head(10)


# In[42]:



data['Director'].value_counts().head(1)


# # show all records where category is movie and types  is comedies or country is india...

# In[43]:


data.head(2)


# In[44]:


data[(data['Category']=='Movie') & (data['Type']=='Comedies') | (data['Country']=='India')]


# In[45]:


data[(data['Category']=='Movie') & (data['Type']=='Comedies')]


# In[46]:


data[(data['Category']=='Movie') & (data['Type']=='Comedies') | (data['Country']=='United Kingdom')]


# In[47]:


data[(data['Category']=='Movie') & (data['Type']=='Comedies') & (data['Country']=='India')]


# # in how many movies vicky kaushal was casted?

# In[48]:


data.head(1)


# In[49]:


data[data['Cast']== 'Hrithik Roshan']


# In[50]:


data[data['Cast'].str.contains('Hrithik Roshan')]
#there are null values in cast column so remove it first


# # there are null values in cast column so remove it first

# In[51]:


datan=data.dropna()


# In[52]:


datan.head(3)


# In[53]:


datan[datan['Cast'].str.contains('Hrithik Roshan')]


# # what are the different rating defined by netflix

# In[54]:


data.head(2)


# In[55]:


data.Rating.nunique()


# In[56]:


data.Rating.unique()


# # how many movies got the "TV-14" rating in canada?

# In[57]:


data.head(2)


# In[58]:


data[(data['Category']=='Movie') & (data['Rating']=='TV-14')].shape


# In[59]:


data[(data['Category']=='Movie') & (data['Rating']=='TV-14') & (data['Country']=='Canada')].shape


# In[60]:


data[(data['Category']=='Movie') & (data['Rating']=='TV-14') & (data['Country']=='India')].shape


# In[61]:


data[(data['Category']=='Movie') & (data['Rating']=='TV-14') & (data['Country']=='Brazil')].shape


# # how many tv shows got the "R" rating  after year 2020?

# In[62]:


data[(data['Category']=='TV Show') & (data['Rating']=='TV-14') & (data['year']==2020)]


# # what is the max duration of a movie /show on netflix??

# In[63]:


data['Duration'].unique()


# In[64]:


data.Duration.dtypes


# In[65]:


#spliting 
data[['Minutes','Unit']]=data['Duration'].str.split(' ',expand=True)


# In[66]:


data.head(2)


# In[67]:


data.Minutes.max()


# In[68]:


data.Minutes.min()


# # which indivdual country has highest no of tv shows?

# In[69]:


tv=data[data['Category']=='TV Show']


# In[70]:


tv.head(2)


# In[71]:


tv.max()


# In[72]:


tv.Country.value_counts()


# # sort data set by year

# In[73]:


data.head(1)


# In[74]:


data.sort_values(by='year').head(5)


# In[75]:


data.sort_values(by='year',ascending =False).head(5)


# # find all the instances where:
#     

# # category is 'movie ' and type 'dramas'

# In[76]:


data[ (data['Category']=='Movie') & (data['Type']=='Dramas')].head(2)


# In[77]:


data[(data['Category']=='TV Show')  & (data['Country']=='South Korea')].head(2)


# # category is "tv show " and type is "kids Tv"

# In[78]:


data[ (data['Category']=='TV Show') & (data['Type']=="Kids' TV")].head(2)


# # visualization

# In[79]:


data.Type.value_counts()


# In[80]:


import seaborn as sns


# In[83]:


sns.countplot(x='Category',data= data)
plt.title("count vs type of shows")
plt.show()


# In[84]:


data['Country'].value_counts().head(10)


# In[85]:


plt.figure(figsize=(12,6))
sns.countplot(y='Country',order=data['Country'].value_counts().index[0:10],data=data)


# # check type of content based on country

# In[90]:


movcou=data[data['Category']=='Movie']
tvcou=data[data['Category']=='TV Show']


# In[91]:


plt.figure(figsize=(12,6))
sns.countplot(y='Country',order=data['Country'].value_counts().index[0:10],data = movcou)

plt.title("top 10 countries producing movies in netflix")

plt.figure(figsize=(12,6))
sns.countplot(y='Country',order=data['Country'].value_counts().index[0:10],data = tvcou)


# #the above analysis was done in refernce with   
# 
# https://www.youtube.com/watch?v=LzDSlZb41u8&list=PLsEUopXkU3Cux-OVMNOpgBux2ZHNeno3l&index=5
# 
# 
# https://www.youtube.com/watch?v=b7Kd0fLwgO4&list=PLsEUopXkU3Cux-OVMNOpgBux2ZHNeno3l
