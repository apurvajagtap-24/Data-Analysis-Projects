#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np 
import pandas as pd
import os
for dirname, _, filenames in os.walk('"C:/Users/Apurva/Downloads/archive (1)/job_descriptions.csv"'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# In[5]:


df=pd.read_csv('C:/Users/Apurva/Downloads/archive (1)/job_descriptions.csv')


# In[6]:


df.head()


# In[7]:


df.info()


# In[8]:


df.isnull().sum()


# In[9]:


df = df.dropna(subset=['Company Profile'])


# In[10]:


df.describe()


# In[11]:


df.shape


# In[12]:


df.size


# In[13]:


df.value_counts


# In[14]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[19]:


df.columns


# In[20]:


# Plot the top 10 most common job titles
plt.figure(figsize=(12, 6))
df['Job Title'].value_counts().head(10).plot(kind='barh', color='skyblue')
plt.title('Top 10 Most Common Job Titles')
plt.xlabel('Number of Postings')
plt.ylabel('Job Title')
plt.show()


# In[21]:


work_type_distribution = df['Work Type'].value_counts()
work_type_distribution.plot(kind='pie', autopct='%1.1f%%', title='Job Postings by Work Type')


# In[22]:


import pandas as pd

# Load the dataset
# Assuming your dataset is stored in a file named 'job_data.csv'
df = pd.read_csv("C:/Users/Apurva/Downloads/archive (1)/job_descriptions.csv")

# Group data by 'Country'
grouped_by_country = dict(tuple(df.groupby('Country')))

# Save each country's data into separate CSV files
for country, data in grouped_by_country.items():
    # Clean up country names to use as filenames
    file_name = f"{country.replace(' ', '_').replace('/', '_')}.csv"
    data.to_csv(file_name, index=False)
    print(f"Saved data for {country} in {file_name}")


# In[24]:


import os
print(os.getcwd())


# In[25]:


df_usa = pd.read_csv("C:/Users/Apurva/Downloads/archive (1)/Country wise/USA.csv")
df_usa.shape


# In[26]:


import pandas as pd

# Load the dataset
df = pd.read_csv("C:/Users/Apurva/Downloads/archive (1)/Country wise/USA.csv")

# Remove the 'latitude' and 'longitude' columns
df = df.drop(['latitude', 'longitude'], axis=1)

# Verify the columns are removed
print(df.columns)

# Optional: Save the updated DataFrame back to a CSV file
df.to_csv("job_data_cleaned.csv", index=False)
print("Columns removed and data saved to 'job_data_cleaned.csv'")


# In[27]:


plt.figure(figsize=(12, 6))
df_usa['Job Title'].value_counts().head(10).plot(kind='barh', color='skyblue')
plt.title('Top 10 Most Common Job Titles')
plt.xlabel('Number of Postings')
plt.ylabel('Job Title')
plt.show()


# In[28]:


# Remove '$' and 'K' from the Salary Range and handle missing values
df_usa['Salary Range'] = df_usa['Salary Range'].str.replace('$', '', regex=False).str.replace('K', '', regex=False)

# Handle missing or improperly formatted salary ranges
df_usa = df_usa[df_usa['Salary Range'].str.contains('-')]  # Keep rows with a valid range

# Extract minimum and maximum salary from 'Salary Range' column
df_usa['Min Salary'] = df_usa['Salary Range'].str.split('-').str[0].str.strip().astype(float) * 1000
df_usa['Max Salary'] = df_usa['Salary Range'].str.split('-').str[1].str.strip().astype(float) * 1000

# Calculate the average salary
df_usa['Average Salary'] = (df_usa['Min Salary'] + df_usa['Max Salary']) / 2

# Check if salary extraction worked
print(df_usa[['Salary Range', 'Min Salary', 'Max Salary', 'Average Salary']].head())


# In[29]:


job_role_portal = pd.crosstab(df['Job Portal'], df['Role'])
job_role_portal.plot(kind='bar', stacked=True, title='Job Roles by Job Portal')

