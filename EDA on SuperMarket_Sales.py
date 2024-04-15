#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Importing all the useful libraries


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[51]:


#Importing dataset
data = pd.read_csv("supermarket_sales - Sheet1.csv")


# In[4]:


data


# In[6]:


#Checking First 5 rows of the dataset
data.head()


# In[5]:


#Checking last 5 rows of the datasets
data.tail()


# In[7]:


#Checking random rows of the datasets
data.sample(5)


# In[8]:


#checking shape of the dataset. As in number of rows and number of columns
data.shape 


# In[9]:


print("Number of Columns",data.shape[0])
print("Number of Rows",data.shape[1])


# In[10]:


#Checking null values in the datasets
data.isnull().sum()


# In[11]:


#checking the detailed info of our datasets 
data.info()


# In[12]:


#Checking the statistics of our dataset
data.describe()


# # Univariate Analysis 

# In[13]:


cat = []
num = []
for column in data.columns:
    if data [column].nunique() >10:
         num.append(column)
    else:
         cat.append(column)


# In[14]:


cat


# In[15]:


num


# In[16]:


sns.countplot(x=data['Branch'], data=data)


# In[17]:


data["Branch"].value_counts().plot(kind="pie", autopct="%1.0f%%")


# In[18]:


data["Branch"].value_counts().plot(kind="bar")


# In[19]:


data["Payment"].value_counts().plot(kind="bar")


# In[20]:


num


# In[21]:


sns.displot(data["Rating"])


# In[22]:


data["Rating"].skew()


# In[66]:


sns.distplot(data["cogs"])


# In[67]:


data["cogs"].skew()


# In[23]:


sns.boxplot(x="cogs", data=data)
plt.show()


# In[25]:


sns.scatterplot(data["cogs"])


# In[26]:


sns.scatterplot(data["gross income"], data["Rating"])


# In[27]:


sns.scatterplot(data=data,x ="gross income", y="Rating")


# In[28]:


sns.barplot(x="Branch", y="gross income", data=data)


# In[29]:


sns.barplot(x="Branch", y="gross income", data=data, hue=data["City"])


# In[30]:


sns.boxplot(x="Gender", y="gross income", data=data)


# In[31]:


sns.boxplot(x="Gender", y="gross income", data=data, hue=data["Customer type"])


# In[32]:


data.columns


# In[33]:


sns.barplot(data=data, x="Product line", y="gross income")
plt.xticks(rotation=60)
plt.show()


# In[96]:


sns.barplot(data=data, x="Product line", y="Unit price")
plt.xticks(rotation=60)
plt.show()


# In[34]:


pd.crosstab(data["City"], data["Payment"])


# In[35]:


sns.heatmap(pd.crosstab(data["City"], data["Payment"]))


# In[47]:


(data.groupby("Product line").sum()["Quantity"]).plot(kind="bar")
plt.show()


# In[52]:


(data.groupby("Product line").sum()["Quantity"]).plot(kind="bar")
plt.ylabel('Total Quantity')
plt.title('Total Quantity Sold by Product Line')
plt.show()


# In[46]:


data


# In[53]:


data["Date"]=pd.to_datetime(data["Date"])


# In[54]:


data["Date"].dt.dayofweek


# In[58]:


dw_mapping = {0:"Monday",
             1:"Tuesday",
             2:"Wednesday",
             3:"Thursday",
             4:"Friday",
             5:"Saturday",
             6:"Sunday"}


# In[59]:


data["Date"].dt.dayofweek.map(dw_mapping)


# In[60]:


data["Day_of_week"]=data["Date"].dt.dayofweek.map(dw_mapping)


# In[61]:


data.head(1)


# In[62]:


data["Day_of_week"].value_counts().plot(kind="bar")


# In[67]:


data["Month"]=data["Date"].dt.month.map(month_mapping)


# In[66]:


month_mapping = {1:"January",
             2:"Febuary",
             3:"March",
             4:"April",
             5:"May",
             6:"June",
             7:"July",
             8:"August",
             9:"September",
             10:"October",
             11:"November",
             12:"December"}


# In[68]:


data.head(1)


# In[69]:


data["Month"].value_counts().plot(kind="bar")


# In[ ]:




