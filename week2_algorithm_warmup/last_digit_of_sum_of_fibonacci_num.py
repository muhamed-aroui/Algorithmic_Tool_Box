# python3
import numpy as np
def fibo(m, n):
    x= np.zeros(61)
    x[1]=1
    for i in range(2,61):
        x[i]= (x[i-1]+x[i-2])%10 #prints out the last digit
    #print(x[n:])
    reminder1=m%60
    reminder2= (n-m)%60+reminder1+1
    My_last_digit= np.sum(x[reminder1:reminder2])
    return int(My_last_digit%10)
inputs= [int(x) for x in input().split()]
a=inputs[0]
b=inputs[1]
fibon = fibo(a, b)
print(fibon)
