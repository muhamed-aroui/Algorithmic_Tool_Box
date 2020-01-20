# Uses python3
import sys
import numpy as np

def optimal_weight(W, w):
    # write your code here
    a = len(w) + 1
    b = W + 1
    P = [[0 for x in range(b)] for x in range(a)]
    for i in range(a):
        for j in range(b):
            if i == 0 or j==0 :
                P[i][j]=0
            #P[j][i]=P[j][i-1]
            elif w[i -1] <= j:
                P[i][j]= max(w[i-1]+P[i-1][j-w[i-1]],P[i-1][j])
            else:
                P[i][j]=P[i-1][j]
    return P[a -1][b-1]



if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
