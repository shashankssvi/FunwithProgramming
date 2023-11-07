#!/usr/bin/env python
# coding: utf-8

# In[5]:


# we take a module and convert to kannada
import md_se as e
from googletrans import Translator 
t = Translator()
translated_text = t. translate(e.out,dest='kn')
kannada=(translated_text. text)
print(kannada)


# In[ ]:




