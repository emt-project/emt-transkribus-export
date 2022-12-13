#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd


# In[14]:


df = pd.read_csv('../metadata.csv')


# In[15]:


wer_an_wen = set(df['weranwen'].values)


# In[16]:


data = []
persons = set()
split_token = ' an '
for x in wer_an_wen:
    sender = ""
    receiver = ""
    try:
        if split_token in x:
            sender, receiver = x.split(split_token)
    except TypeError:
        continue
    if sender.endswith(','):
        sender = sender[:-1]
    persons.add(sender.strip())
    persons.add(receiver.strip())

# In[17]:


data = []
for i, x in enumerate(sorted(persons)):
    item = {
        "name": x,
        "gnd": "",
        "emt_id": f"emt_person_{i+1}"
    }
    data.append(item)


# In[18]:


person_df = pd.DataFrame(data)


# In[20]:


person_df.to_csv('../persons.csv', index=False)


# In[26]:


orte = [x for x in set(df['Ort'].values) if isinstance(x, str)]


# In[30]:


data = []
for i, x in enumerate(sorted(orte)):
    item = {
        "name": x,
        "geonames": "",
        "emt_id": f"emt_place_{i+1}"
    }
    data.append(item)


# In[31]:


places = pd.DataFrame(data)


# In[34]:


places.to_csv('../places.csv', index=False)


# In[ ]:





# In[ ]:




