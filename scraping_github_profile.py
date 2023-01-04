#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/rushgala27"
req = requests.get(github_profile)
scraper = bs(req.content,"html.parser")
profile_pic = scraper.find("img",{"alt":"Avatar"})["src"]
print(profile_pic)


# In[ ]:




