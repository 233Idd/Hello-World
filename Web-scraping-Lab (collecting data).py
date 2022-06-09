#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **Hands-on Lab : Web Scraping**
# 

# Estimated time needed: **30 to 45** minutes
# 

# ## Objectives
# 

# In this lab you will perform the following:
# 

# *   Extract information from a given web site
# *   Write the scraped data into a csv file.
# 

# ## Extract information from the given web site
# 
# You will extract the data from the below web site: <br>
# 

# In[1]:


#this url contains the data you need to scrape
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"


# The data you need to scrape is the **name of the programming language** and **average annual salary**.<br> It is a good idea to open the url in your web broswer and study the contents of the web page before you start to scrape.
# 

# Import the required libraries
# 

# In[2]:


from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests # this module helps us to download a web page


# In[3]:


import numpy as np
import pandas as pd


# Download the webpage at the url
# 

# In[4]:


# get the contents of the webpage in text format and store in a variable call
data = requests.get(url).text


# Create a soup object
# 

# In[5]:


soup = BeautifulSoup(data,"html5lib")


# Scrape the `Language name`, `Created By` `annual average salary`and `Learning Difficulty`.
# 

# In[6]:


scraped_table=pd.DataFrame(columns=["language", "createdby", "salary", "difficulty"])


# In[7]:


#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>

#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
   
# Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    if (cols!=[]):
        lang = cols[1].getText() # store the value in column 1 as lang
        creater = cols[2].getText() # store the value in column 2 as creater
        salary = cols[3].getText() # store the value in column 3 as salary
        diff = cols[4].getText() # store the value in column 4 as diff
        print("{}--->{},{},{}".format(lang,creater, salary,diff))
       
        scraped_table=scraped_table.append({"language":lang, "createdby":creater, "salary":salary, "difficulty":diff}, ignore_index=True) 

#important to have the scraped_table append statemented indented under the if or for statement


# Create a *dataframe* for scrapped data
# 

# In[8]:


scraped_table


# Save the scrapped data into a file named *popular-languages.csv*
# 

# In[9]:


import csv


# In[10]:


scraped_table.to_csv('popular-languages.csv', index=False, header = False) #Writing to csv file


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
