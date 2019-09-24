from sys import stdin,stdout

t = int(input())

while t:
    count=0
    
    m,n,o = map(int,stdin.readline().split())
    for i in range(2,m+1):
        for j in range(2,o+1):
            for k in range(1,n+1):
                #print(i,k,j)
                if (i-1)*(j-1)<=k*k:
                    break
                else:
                    count+=1
                    
    print((count)%(1000000007))
    t-=1