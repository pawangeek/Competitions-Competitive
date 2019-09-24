t=int(input())
import math

def hi(n):
    p = int(math.log(n, 2))
    return int(pow(2, p))
    
def f_last(n):
    a, b = 0, 1
    for i in range(n % 60):
        a, b = b, (a + b) % 10
    return a    

while t:
    o=hi(int(input()))
    d=f_last(o-1)
    print(d)
    t-=1