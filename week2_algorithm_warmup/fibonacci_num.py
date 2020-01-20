# python3
import numpy as np
def fibo(n):
    x= np.zeros(n+1)
    if n==0:
        return int(x[0])
    x[1]=1
    for i in range(2,n+1):
        x[i]=x[i-1]+x[i-2]
    return int(x[n])
n = int(input())
fibon = fibo(n)
print(fibon)
