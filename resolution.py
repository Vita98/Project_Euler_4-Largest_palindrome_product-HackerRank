#!/bin/python3

import sys

def isDivis(n):
    for i in range(143,1000):
        if n % i == 0 and len(str(n//i)) == 3:
            return True
    return False


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    maxV = 101101
    for i in range(102,999):
        num = int(str(i)+str(i)[::-1])
        if num >= n:
            break
        
        if isDivis(num):
            maxV = num
    print(maxV)
