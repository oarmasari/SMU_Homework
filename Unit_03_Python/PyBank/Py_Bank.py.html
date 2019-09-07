#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


path = "/Users/kivcargo/Documents/SMU_Assignments/Unit_03_Python/Instructions/PyBank/Resources/budget_data.csv"


# In[3]:


budget = pd.read_csv(path)


# In[15]:


budget.head(26)


# In[ ]:





# In[5]:


total_rows = budget.Date.count()
total_rows
#print (total_rows +1)


# In[6]:


total_profit = budget["Profit/Losses"].sum()
total_profit


# In[7]:


total_profit/total_rows


# In[8]:


changes = []
for indx, row in budget.iterrows():
    print(indx,row['Date'], row['Profit/Losses'])

    if (indx < 85):
        change = budget['Profit/Losses'][indx+1] - row['Profit/Losses']
        #print(change)
        changes.append(change)


# In[26]:


avg_change = sum(changes)/85


# In[10]:


max_value = max(changes)
min_value = min(changes)


# In[11]:


print (max_value)


# In[12]:


print (min_value)


# In[13]:


changes.index(max_value)


# In[17]:


max_change = changes.index(max_value)


# In[18]:


min_change = changes.index(min_value)


# In[25]:


max_month = budget.iloc[max_change +1].Date
print(max_month)


# In[24]:


min_month = budget.iloc[min_change +1].Date
print (min_month)


# In[33]:


output = (
        f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_rows}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: ${avg_change}\n"
    f"Greatest Increase in Profit: {max_month} (${max_value})\n"
    f"Greatest Decrease in Profit: {min_month} (${min_value})\n")


# In[35]:


text_file = open("output.txt", "w")
text_file.write(output)
text_file.close()

