# Uses python3
import sys
import numpy as np

def get_change(W):
    #write your code here
    c=0

    while W!=0:
        if W >= 10:
            w1 = 10
        elif W>=5 :
            w1 = 5
        elif W>= 1:
            w1 =1
        a = np.minimum(w1,W)
        W = W- a
        c = c+ 1
    return c

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
