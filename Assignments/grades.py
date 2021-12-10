#!/usr/bin/env python
# coding: utf-8

# In[1]:

import math
import statistics

def total(list_object):
    return float(sum(list_object))

def average(values):
    if len(values) > 0:
        return float((sum(values)/len(values)))
    else:
        return math.nan
    
def median(list_object):
    if len(list_object) > 0:
        return statistics.median(list_object)
    else:
        raise ValueError
    
    

# In[ ]:




