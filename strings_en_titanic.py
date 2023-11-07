#!/usr/bin/env python
# coding: utf-8

# In[3]:


# we take a module and convert to english
import md_se as e
from googletrans import Translator 
t = Translator()
translated_text = t. translate(e.out)
english=(translated_text. text)
print(english)


# In[ ]:




