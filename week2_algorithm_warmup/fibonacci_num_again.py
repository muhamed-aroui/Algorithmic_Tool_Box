# python3
#In this problem, your goal is to compute 𝐹𝑛(fibonacciNum) modulo 𝑚, where 𝑛 may be really huge: up to 101
import numpy as np
def fibo(n, m):
    x= np.empty(m*10)
    #print(len(k))
    x[0]=0
    x[1]=1
    for i in range(2,m*10):
        x[i]= (x[i-1]+x[i-2])%m #prints out the mdulo digit
        #print('k[-1i]=',x[i-1],'x[i]=',x[i],i)
        if x[i-1]==0 and x[i]==1:
            lg= i-1
            #print(lg,i)
            r= n%lg
            #print('the length is ',lg,'the mudul is',r)
            return int(x[r])
inputs= [int(x) for x in input().split()]
a=inputs[0]
b=inputs[1]
fibon = fibo(a, b)
print(fibon)
