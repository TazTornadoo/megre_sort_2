#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def split(list_):
    if len(list_) <= 1:
        return list_
        
    middle = len(list_) // 2
    left = split(list_[:middle])
    right = split(list_[middle:])
    
    return merge(left, right)

