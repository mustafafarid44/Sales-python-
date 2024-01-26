#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


import seaborn as sns


# In[5]:


df = pd.read_csv('C:/Users/Mustafa/Desktop/datasets/Pandas-Data-Science-Tasks-master/Pandas-Data-Science-Tasks-master/SalesAnalysis/Output/all_data.csv')


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


df.head()


# In[9]:


df.isna().value_counts()


# In[10]:


df.columns


# In[11]:


df = df.dropna(axis =0)


# In[13]:


df.isna().sum()


# In[14]:


pd.set_option('display.max_columns', 15)


# In[16]:


pd.set_option('display.max_rows', 50)


# In[17]:


df.head()


# In[18]:


df.sample(50)


# In[19]:


df.dtypes


# In[20]:


d =df.groupby('Product')['Price Each'].mean()


# In[21]:


df.head()


# In[70]:


df['Price Each'].mean()


# In[61]:


d=pd.DataFrame(d)


# In[62]:


d


# In[73]:


df['Price Each']=df['Price Each'].select_dtypes(include=['float'])


# In[22]:


df.dtypes


# In[79]:


df['Price Each'].astypes


# In[23]:


df['Price Each'] = pd.to_numeric(df['Price Each'].astype(str), errors='coerce')


# In[24]:


df.dtypes


# In[25]:


df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'].astype(str), errors='coerce')


# In[26]:


df.dtypes


# In[27]:


df.head(10)


# In[91]:


df['Quantity Ordered'].astype(int)


# In[28]:


df['Quantity Ordered'].isna().sum()


# In[29]:


df['Price Each'].isna().sum()


# In[30]:


df = df.dropna(axis=0)


# In[31]:


df.isna().sum()


# In[97]:


df.dropna(axis=0)


# In[32]:


df


# In[37]:


df['Quantity Ordered']=df['Quantity Ordered'].astype(int)


# In[38]:


df.dtypes


# In[ ]:


###Analysing Data


# In[ ]:


#1-Most Sales Products


# In[39]:


df.groupby('Product')['Quantity Ordered'].sum()


# In[44]:


Most_sales = pd.DataFrame(df.groupby('Product')['Quantity Ordered'].sum()).sort_values(by = 'Quantity Ordered',ascending=False)


# In[46]:


Most_sales


# In[49]:


plt.rcParams["figure.figsize"] = (20, 10)


# In[61]:


plt.figure(figsize=(6, 10))
Most_sales.plot(kind='bar')
plt.title('Most Sold Products',size=35)
plt.xlabel('Product', size=35)
plt.ylabel('Count',size=35)
plt.legend('Quantity Ordered',fontsize=35)
#plt.ticklabel_format(style='plain',axis='y')..... only when scientific notation
plt.xticks(rotation=90, size=15)
plt.yticks( size=15)
plt.show()


# In[62]:


#2-Most revenued products


# In[68]:


Most_rev= df.groupby('Product')['Price Each'].sum().sort_values( ascending=False)


# In[69]:


Most_rev


# In[73]:


plt.figure(figsize=(20, 10))
Most_rev.plot(kind='bar')
plt.title('Most Revenued Products',size=35)
plt.xlabel('Product', size=35)
plt.ylabel('Revenue',size=35)
plt.legend('Quantity Ordered',fontsize=35)
plt.ticklabel_format(style='plain',axis='y')
plt.xticks(rotation=90, size=15)
plt.yticks( size=15)
plt.show()


# In[74]:


#3-Value Vs Piece 


# In[76]:


df.columns


# In[78]:


Value_Piece= df.groupby('Product')['Quantity Ordered','Price Each'].sum()


# In[82]:


p = sns.scatterplot(data=Value_Piece, x="Quantity Ordered", y="Price Each", hue='Product', s=100).set(title='Revenue vs Count of pieces', xlabel='xG per team')
#sns.move_legend(p, "upper right", bbox_to_anchor=(1, 1))


# In[ ]:




