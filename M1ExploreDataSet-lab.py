#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **2020 Survey Dataset Exploration Lab**
# 

# Estimated time needed: **30** minutes
# 

# ## Objectives
# 

# After completing this lab you will be able to:
# 

# *   Load the dataset that will used thru the capstone project.
# *   Explore the dataset.
# *   Get familier with the data types.
# 

# ## Load the dataset
# 

# Import the required libraries.
# 

# In[1]:


import pandas as pd


# The dataset is available on the IBM Cloud at the below url.
# 

# In[2]:


dataset_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/Capstone_edX/Module%201/survey_results_public_2020.csv"


# Load the data available at dataset_url into a dataframe.
# 

# In[3]:


df=pd.read_csv(dataset_url)


# ## Explore the data set
# 

# It is a good idea to print the top 5 rows of the dataset to get a feel of how the dataset will look.
# 

# Display the top 5 rows and columns from your dataset.
# 

# In[4]:


df.head()


# In[ ]:


# your code goes here


# ## Find out the number of rows and columns
# 

# Start by exploring the numbers of rows and columns of data in the dataset.
# 

# Print the number of rows in the dataset.
# 

# In[6]:


print (df.index)


# In[7]:


len(df. index)


# Print the number of columns in the dataset.
# 

# In[8]:


print (df.columns)


# In[9]:


len (df.columns)


# ## Identify the data types of each column
# 

# Explore the dataset and identify the data types of each column.
# 

# Print the datatype of all columns.
# 

# In[10]:


df.dtypes


# Print the mean age of the survey participants.
# 

# In[11]:


mean_age= df["Age"].mean()
mean_age


# The dataset is the result of a world wide survey. Print how many unique countries are there in the Country column.
# 

# In[12]:


df["Country"].value_counts() #Returns counts of unique values [countries]
# can use df["Country"].value_counts().to_frame() to have output in a dataframe table


# In[14]:


# get unique values [countries] without counting each occurence
df["Country"].unique()


# In[15]:


#Get number of unique countries
len(df["Country"].unique())


# ## Authors
# 

# Ramesh Sannareddy
# 

# ### Other Contributors
# 

# Rav Ahuja
# 

# ## Change Log
# 

# | Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
# | ----------------- | ------- | ----------------- | ---------------------------------- |
# | 2020-10-17        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |
# 

# Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2022-01-01&cm_mmc=Email_Newsletter-\_-Developer_Ed%2BTech-\_-WW_WW-\_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).
# 
