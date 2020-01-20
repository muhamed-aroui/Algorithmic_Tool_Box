# Python3
def MaxPairWise():
    lo=int(input())
    A=[int(x) for x in input().split()]
    n=lo-1
    #n=len(A)-1
    #print(n)
    index=0
    #print(A[n])
    for i in range(1,n):
        #print(i)
        if A[i]>A[index]:
            index=i
    A[index], A[n]= A[n], A[index]
    index=0
    for i in range(1,n):
        if A[i]>A[index]:
            index=i
    A[index],A[n-1]=A[n-1],A[index]
    return A[n]*A[n-1]
print(MaxPairWise())
