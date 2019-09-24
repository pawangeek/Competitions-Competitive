from sys import stdin,stdout
t = int(input())

while t:
    k,n = map(int,stdin.readline().split())
    
    if k==1 and n==1:
        print(1)
        
    elif k==1 and n==0:
        print(0)
        
    elif k==2 and n==1:
        print(1)
    
    elif n<k-1 or n>(k*(k+1))/2:
        print (-1)
        
    elif n>=k-1 and n<=k+1:
        print (2)
        
    elif n>k+1 and n<=2*k:
        print(3)
        
    elif n>2*k:
        if k%2==0:
            l = n-(2*k)
            p = (l-1)//(k/2)
            print (int(4+p))
            
        else:
            l = n-(2*k)
            p = (l-1)%k
            m = (l-1)//k
            
            if p<int(k/2):
                print (int(4+(2*m)))
            else:
                print (int(5+(2*m)))
            
        
    t-=1