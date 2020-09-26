#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def merge(left, right):
    sorted_result = []
    left_index = 0
    right_index = 0
    
    Active = True
    
    while Active:
        if left[left_index] < right[right_index]:
            sorted_result.append(left[left_index])
            left_index = left_index + 1
        else:
            sorted_result.append(right[right_index])
            right_index = right_index + 1
        if left_index == len(left):
            sorted_result.extend(right[right_index:])
            Active = False
        if right_index == len(right):
            sorted_result.extend(left[left_index:])
            Active = False
    return sorted_result

import time
import random
time_results_shuffled = []

def test_merge_sort(function):
    #creating a shuffled data set, its a worst case scenario

    i = 1000

    while i <= 512000:
        print('This is the processing time for average case scenario with a list of range '
                + str(i))
    
        trial_ac = list(range(0, i))
    
        random.shuffle(trial_ac)
    
        start = time.time()
    
        function(trial_ac)
    
        end = time.time()
    
        total_time = end - start
    
        print(total_time)
        # Add result to list
        time_results_shuffled.append(total_time)
        i = i * 2
        
        
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def data_visualization(time_set1):
    
    #Create list for the number of items
    i = 1000
    items = []
    while i <= 512000:
        items.append(i)
        i = i * 2
    
    plt.plot(items, time_set1, marker='.', label ='worst case')
    
    
    
    plt.xlabel ('Items sorted')
    plt.ylabel ('Time in seconds')
    plt.title ('Time Complexity - Merge Sort Algorithm')
    plt.xticks([1000,2000,4000,8000,16000,32000, 64000, 128000, 256000, 512000], 
            ['1k','2k','4k','8k','16k','32k', '64k', '128k', '256k', '512k'])
    plt.legend()
    plt.show()

