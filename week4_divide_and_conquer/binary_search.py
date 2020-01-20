# Uses python3
import sys
import math

def binary_search(a,low,high, key):
    #print('b_low is and b_high is',low,high)
    #left, right = 0, len(a)
    # write your code here
    if high<low:

        #print('low,hight,key',low,high,key)
        return -1
    mid = math.floor(low + (high-low)/2)
    #print('mid ',mid)
    if key == a[mid]:
        return mid
    elif key < a[mid]:
        return binary_search(a,low,mid-1,key)
    elif key>a[mid]:
        return binary_search(a,mid+1,high,key)
    else:
        return -1

def linear_search(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    #low, high = 0, len(a)
    for key in data[n + 2:]:
        low, high = 0, len(a)-1
        #print('\nkey is ',key,high)
        # replace with the call to binary_search when implemented
        print(binary_search(a,low,high, key), end = ' ')
