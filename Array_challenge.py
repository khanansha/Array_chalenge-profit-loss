# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 17:55:59 2021

@author: Anjum Khan
"""


def ArrayChallenge(arr): 
    # arr=[4, 6, 23, 10, 1, 3]
    sort_arr = arr.sort()
    
    largest_num = arr.pop()
   
    total = 0
    
    for i in range(0, len(arr)):
        total += arr[i]
        
        for j in range(0, len(arr)):
            if i != j:
                total += arr[j]
                if (total == largest_num):
                    return 'True'  
        
        for k in range(0, len(arr)):                
            if i != k:
                total -= arr[k]
                if (total == largest_num):
                    return 'True'
        
        total = 0
    return 'False'

output=ArrayChallenge([4, 6, 23, 10, 1, 3])
print(output)