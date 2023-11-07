#!/usr/bin/env python
# coding: utf-8

# In[6]:


# we take a module and convert to hindi
import md_se as e
from googletrans import Translator 
t = Translator()
translated_text = t. translate(e.out,dest='hi')
hindi=(translated_text. text)
print(hindi)


# In[ ]:




