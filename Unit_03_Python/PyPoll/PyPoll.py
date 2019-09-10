#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd


# In[10]:


#create a variable for csv file

pypoll = "election_data.csv"

#create a variable for the data frame
poll_df = pd.read_csv(pypoll)
poll_df.head()


# In[11]:


#calculate total number of votes
votes = len(poll_df["Voter ID"].unique())
print(votes)


# In[12]:


#complete list of candidates
candidates = poll_df["Candidate"].unique()
print(candidates)

#type candidate names into output lines


# In[13]:


#total number of votes per candidate
count = poll_df["Candidate"].value_counts()
print(count)


# In[14]:


#% of votes per candidate
percent = (count / votes)*100
print(round(percent))


# In[15]:


#winner based on popular vote
maxVotes = count.max()
maxCand = count.idxmax()
print(str(maxCand) + " won the election with " + str(maxVotes) + " votes.")


# In[16]:



  # style output 
output = (
  f"\nElection Results: \n"
  f"------------------- \n"
  f"Total Votes: {votes} \n"
  f"------------------- \n"
  f"{list(percent.index)[0]}  {str(round(percent[0]))}% ({str(count[0])})\n"
  f"{list(percent.index)[1]}  {str(round(percent[1]))}% ({str(count[1])})\n"
  f"{list(percent.index)[2]}  {str(round(percent[2]))}% ({str(count[2])})\n"
  f"{list(percent.index)[3]}  {str(round(percent[3]))}% ({str(count[3])})\n"
  f"------------------- \n"
  f"Winner : {maxCand} won the election with {maxVotes} votes.\n"
  f"------------------- \n")
# print results
print(output)


# In[18]:


text_file = open("Output.txt", "w")
text_file.write(output)
text_file.close()


# In[ ]:




