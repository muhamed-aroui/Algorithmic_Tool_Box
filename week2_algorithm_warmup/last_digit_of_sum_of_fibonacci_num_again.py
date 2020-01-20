# python3
import numpy as np
def fibo(m):
    x= np.zeros(61)
    x[1]=1
    for i in range(2,61):
        x[i]= (x[i-1]+x[i-2])%10 #prints out the last digit

    c1= m%60
    c2= (c1+1)%60
    t= x[c1]*x[c2]
    return int(t%10)

a= int(input())
fibon = fibo(a)
print(int(fibon))
