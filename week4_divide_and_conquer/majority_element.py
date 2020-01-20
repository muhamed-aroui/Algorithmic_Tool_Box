# Uses python3
import sys
import math
def get_freq(a,maj):
    count = 0
    for i in range(len(a)):
        if maj == a[i]:
            count =count +1
    return count
def get_majority_element(a, left, right):
    k= math.floor((right+1)/2)
    if left == right:
        return a[left]
    if left + 1 == right:
        if a[left]==a[right]:
            return a[left]
        else:
            return -1
    #write your code here
    m = math.floor((left+right)/2)
    #print('m1=',m,left)
    l=get_majority_element(a,left,m)
    #rint('l',l)
    #print("ITIRATION",right)
    r=get_majority_element(a,m+1,right)
    #print('m2=',m)
    #print('l,r',l,r)
    if l==r :
        return l
    #else:
        #print('he reached')
    lcount= get_freq(a,l)
    rcount = get_freq(a,r)
    if lcount > k or rcount> k:
        #print('comparation used')
        return 1
    else:
        #print('comparation 2 used')
        return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)
