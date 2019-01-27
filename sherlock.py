#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the isValid function below.
def isValid(s):
    freq = {}
    freq_list = []
    is_valid = False
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    for k, v in freq.items():
        freq_list.append(v)
    
   
    for i in range(len(freq_list)):
        if all(x == freq_list[0] for x in freq_list):
            return "YES"

        freq_list[i] = freq_list[i] - 1
        removed_list = freq_list[:]
        if freq_list[i] == 0:
            removed_list.remove(freq_list[i])
        
        is_valid = all(x == removed_list[0] for x in removed_list)

        if is_valid == True:
            return "YES"

        freq_list[i] = freq_list[i] + 1
    
    return "NO"
        
    
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
