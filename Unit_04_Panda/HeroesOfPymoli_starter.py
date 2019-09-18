#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
items = "purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(items)
purchase_data.head()


# In[2]:


purchase_data.columns


# In[3]:


## Player Count


# * Display the total number of players
# 

# In[4]:


players = purchase_data ["SN"].nunique()
print (players)


# In[5]:



u_items = purchase_data ["Item ID"].nunique()
print(u_items)


# In[6]:



tot_pur = purchase_data["Purchase ID"].count()
print (tot_pur)


# In[7]:


#calculated sum of total revenue
tot_rev = purchase_data["Price"].sum()
print(tot_rev)


# In[8]:


#calculated average price
av_price = tot_rev / tot_pur
print(av_price)


# In[9]:


summary_df = pd.DataFrame({"Number of Unique Numbers": [u_items],
                          "Average Purchase Price": [av_price],
                          "Total Number of Purchases": [tot_pur],
                          "Total Revenue": [tot_rev]})
summary_df
                          


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# ## Gender Demographics

# In[10]:


find = purchase_data.drop_duplicates("SN")
find['Gender'].value_counts()


# In[11]:


gendercount =  find['Gender'].value_counts().values
genders =  find['Gender'].value_counts().index


# In[12]:


total =gendercount.sum()
total


# In[13]:


genderpercent = gendercount / total *100
genderpercent = [str(round(x,2)) + "%" for x in genderpercent]
genderpercent


# In[14]:


summary_df = pd.DataFrame({"Genders": genders,
                          "Total Count": gendercount,
                          "Percentage of Players": genderpercent})
summary_df


# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[15]:


#create dataframe of unique users
pur_Unq = purchase_data.drop_duplicates("SN")
genders =  pur_Unq['Gender'].value_counts().index

print (genders)


# In[16]:


gender_counts = purchase_data["Gender"].value_counts()
genCounts2 = gender_counts.values
genCounts2


# In[17]:


gender_group = purchase_data.groupby(["Gender"])
gender_comparison = gender_group.mean()
genderPrice2 = gender_comparison.Price.values
genderPrice2


# In[18]:


gender_purchase = gender_group.sum()
genderTotalPrice = gender_purchase.Price.values
genderTotalPrice


# In[19]:


genderCount2 = summary_df.sort_values("Genders")["Total Count"].values
genderCount2


# In[20]:


avgGenderPerson = genderTotalPrice / genderCount2
avgGenderPerson


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[21]:


bins = [0,9,14,19,24,29,34,39,100]

unique_df= purchase_data.groupby('SN').mean()

age=unique_df.groupby(pd.cut(unique_df['Age'],bins=bins)).size()

age_df=pd.DataFrame({ "Total Count":age})
age_df['Percentage of Players']=round(age_df['Total Count']/players *100,2)
age_df


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[22]:


bins = [0,9,14,19,24,29,34,39,100]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]


# In[23]:


purchase_data["Age Demographics"] = pd.cut(purchase_data["Age"], bins, labels=group_names)
purchase_data.head()


# In[24]:


agerange = purchase_data['Age Demographics'].value_counts().index.values
agerange


# In[25]:


age_count = purchase_data["Age Demographics"].value_counts()
age_count2 = age_count.values
age_count2


# In[26]:


age_group = purchase_data.groupby(["Age Demographics"])
age_comparison = age_group.mean()
ageprice2 = age_comparison.Price.values
ageprice2


# In[27]:


age_purchase = age_group.sum()
ageTotalPrice = age_purchase.Price.values
ageTotalPrice


# In[28]:


ageCount2 = age_df.sort_values("Age")["Total Count"].values
ageCount2


# In[29]:


avgAgePerson = ageTotalPrice / ageCount2
avgAgePerson


# In[30]:


summary_df4 = pd.DataFrame({"Age": agerange,
                          "Purchase Count": age_count2})
sortedDf4 = summary_df4.sort_values("Age").reset_index(drop=True)
sortedDf4["Average Purchase Price"] = ageprice2
sortedDf4["Average Purchase Price"] = sortedDf4["Average Purchase Price"].astype(float).map("${:,.2f}".format)
sortedDf4["Total Purchase Value"] = ageTotalPrice
sortedDf4["Total Purchase Value"] = sortedDf4["Total Purchase Value"].astype(float).map("${:,.2f}".format)
sortedDf4["Avg Total Purchase per Person"] = avgAgePerson
sortedDf4["Avg Total Purchase per Person"] = sortedDf4["Avg Total Purchase per Person"].astype(float).map("${:,.2f}".format)
sortedDf4


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[31]:


spenders = purchase_data["SN"].value_counts()
spenders.head()


# In[32]:


spenders=pd.DataFrame(data=spenders)
spenders.columns = ["Purchase Count"]
spenders.head()


# In[36]:


spenders["Average Purchase Price"] = round(purchase_data["Price"].groupby(purchase_data["SN"]).mean(),2)
spenders["Total Purchase Value"] = purchase_data["Price"].groupby(purchase_data["SN"]).sum()


spenders = spenders.sort_values(by="Total Purchase Value", ascending=False)


spenders["Average Purchase Price"] = spenders["Average Purchase Price"].map("${:,.2f}".format)
spenders["Total Purchase Value"] = spenders["Total Purchase Value"].map("${:,.2f}".format)
spenders.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[99]:


popular_items = purchase_data["Item ID"].value_counts()
popular_items.head()


# In[100]:


popular_items=pd.DataFrame(data=popular_items)
popular_items.columns = ["Purchase Count"]
popular_items.head()


# In[101]:


athing = purchase_data.groupby(["Item ID", "Item Name"]).size().reset_index()
anotherthing = athing[["Item ID", "Item Name"]].set_index("Item ID")["Item Name"]
anotherthing


# In[102]:


popular_items["Item Name"] = anotherthing
popular_items["Average Purchase Price"] = round(purchase_data["Price"].groupby(purchase_data["Item ID"]).mean(),2)
popular_items["Total Purchase Value"] = purchase_data["Price"].groupby(purchase_data["Item ID"]).sum()


popular_items = popular_items.sort_values(by="Total Purchase Value", ascending=False)


popular_items["Average Purchase Price"] = popular_items["Average Purchase Price"].map("${:,.2f}".format)
popular_items["Total Purchase Value"] = popular_items["Total Purchase Value"].map("${:,.2f}".format)
popular_items.head(10)


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[103]:


popular_items.head(10)


# In[ ]:




