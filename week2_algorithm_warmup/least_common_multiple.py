# python3
def lcm(a,b):
    if a>b:
        l=a
        n=a
    else:
        l=b
        n=b
    for i in range(0,a*b):
        i+=1
        #print('i= ',i,'l= ',l)
        if l%a==0 and l%b==0:
            return int(l)
        l=n*i
inputs= [int(x) for x in input().split()]
a=inputs[0]
b=inputs[1]
lcm=lcm(a,b)
print(lcm)
