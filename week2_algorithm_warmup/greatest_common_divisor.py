# python3
def EuclideanAlgorithm(a,b):
    if b==0:
        return a
    aa = a%b
    return EuclideanAlgorithm(b,aa)
inputs= [int(x) for x in input().split()]
a=inputs[0]
b=inputs[1]
gcd=EuclideanAlgorithm(a,b)
print(int(gcd))
