#!/usr/bin/env python
# coding: utf-8

# ### The Most Frequent Element 

# In[6]:


numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]


# In[7]:


numbers_list = list(numbers)


# In[8]:


print(type(numbers_list))


# In[9]:


print(numbers_list)


# In[13]:


numbers_list.count(3)


# In[17]:


a = max(numbers_list, key = numbers.count)
 
b = numbers_list.count(a)
 

print("the most frequent number is {} and it was {} times repeated".format(a,b))

