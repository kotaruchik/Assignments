#!/usr/bin/env python
# coding: utf-8

# In[1]:


def myfilter(anyfunc, sequence):
 result = []
 for item in sequence:
  if anyfunc(item):
   result.append(item)
 return result


# In[3]:


def ispositive(x):
 if (x <= 0): 
  return False 
 else: 
  return True
print ("Filter only positive Integers on list using custom filter function"  + str(myfilter(ispositive, [0,1,-2,3,4,-5])))


# In[ ]:




