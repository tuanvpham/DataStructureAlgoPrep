#!/bin/python3

import math
import os
import random
import re
import sys

# My approach
def findIndex(arr, val):
    limit = val -1
    for i in range(limit, len(arr)):
        if arr[i] == val:
            return i  
    return -1

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    min_swaps = 0
    for i in range(len(arr)):
        if i+1 == arr[i]:
            continue
        else:
            index = findIndex(arr, i+1)
            arr[i], arr[index] = arr[index], arr[i]
            min_swaps += 1
    return min_swaps

# Solution
def minimumSwapsSolution(arr):
    swap=0
    i=0
    while i<len(arr):
        if arr[i]==(i+1):
            i+=1
            continue
        arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
        swap+=1
    return swap



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

