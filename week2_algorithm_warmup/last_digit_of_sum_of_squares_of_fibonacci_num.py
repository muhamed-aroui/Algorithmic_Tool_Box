# python3
import numpy as np

def fibo(n):
    x= np.zeros(61)
    if n==0:
        return int(x[0])
    x[1]=1
    for i in range(2,61):
        x[i]= (x[i-1]+x[i-2])%10 #prints out the last digit
    #Last_piaso_digit= np.sum(x)
    #print(Last_piaso_digit)
    reminder=n%60
    print(np.sum(x[34:46]))
    #print(reminder)
    #multiple=(n-reminder)/60
    #print(multiple)
    #print(np.sum(x[:reminder+1]))
    My_last_digit =  np.sum(x[:reminder+1])
    return int(My_last_digit%10)

inputs= [int(x) for x in input().split()]
a=inputs[0]
fibon = fibo(a)
print(int(fibon))
