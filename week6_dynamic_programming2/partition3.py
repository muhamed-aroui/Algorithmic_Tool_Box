# Uses python3
import sys
import itertools

def partition3(arr,n):

    sum=0
    for i in range(n):
        sum += arr[i]
        #print('sum',sum)
    if sum%3 != 0:
        return 0
    a = sum//3+1
    b = n+1
    P=[[0 for x in range(b)] for x in range(a)]
    for i in range(b):
        P[0][i]=1
    for i in range(1,a):
        P[i][0]=0
    for i in range(b):
        for j in range(a):
            print('{:4d}'.format(P[i][j]))
        print('\n')
    #print(P)
    for i in range(a):
        for j in range(b):
            P[i][j] = P[i][j-1]
            if i>= arr[i-1]:
                P[i][j] = P[i][j] or P[i-arr[j-1]]
    return P[a-1][b-1]

'''def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0'''

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A,n))
