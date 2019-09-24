from sys import stdin,stdout
import collections
import bisect

k,n = map(int,stdin.readline().split())
arr = input().split()
arr = sorted(arr)
seti = list(sorted(set(arr)))

#print(seti)

def countx(lst, x): 
    return lst.count(x) 

q=[]
for i in seti:
    l = countx(arr,i)
    q.append(l)

#print(q)
  
def final(arr,k,counts):
    
    n=len(arr)
    s=1
    
    if k>n:
        c=n
    else:
        c=k
    
    dp = [[0 for i in range(n)]  
             for i in range(c)]
    
    f=0
    for i in range(n): 
        dp[0][i] = f+counts[i]
        f = dp[0][i]
        
    for l in range(1,c):
        for i in range(l,n):
            dp[l][i]=dp[l][i-1]+(dp[l-1][i-1]*counts[i])
  
    for i in range(c):   
        s += dp[i][n-1]
    
    #print(dp)
    
    return s%1000000007
    
j = final(seti,n,q)
print(j)