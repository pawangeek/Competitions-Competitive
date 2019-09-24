from sys import stdin,stdout
import operator as op
from functools import reduce
import sys 
t = int(input())

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

while t:
    k,n = map(int,stdin.readline().split())
    arr = input().split()
    arr = sorted(list(map(int, arr)))
    
    c,d=n-1,n-1
    
    for j in range(n-1,len(arr)-1):
        if arr[j+1]==arr[j]:
            c+=1
        else:
            break
     
    new_arr = arr[::-1]
    
    for j in range(k-n,len(arr)-1):
        if new_arr[j+1]==new_arr[j]:
            d-=1
        else:
            break

    if d==0:
        print(int(ncr(c+1,n)))
    else:
        print(int(ncr((c+1)-d,n-d)))
    t-=1