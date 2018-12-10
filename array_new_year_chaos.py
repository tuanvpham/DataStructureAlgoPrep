#!/bin/python3

import math
import os
import random
import re
import sys

# My approach
def minimumBribes(q):
    bribes = 0
    n = len(q)
    for i in range(n):
        for j in range(n-i-1):
            if q[j] - (j+1) >= 3:
                return "Too chaotic"
            
            if q[j] > q[j+1]:
                q[j], q[j+1] = q[j+1], q[j]
                bribes += 1

    return bribes

# Solution
def minimumBribesSolution(q):
    bribes = 0
    for i in range(len(q)-1,-1,-1):
        if q[i] - (i+1) > 2:
            print('Too chaotic')
            return
        
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes+=1
    print(bribes)

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        result = minimumBribes(q)
        print(result)
