# Uses python3
import sys


def Change(changeList,change,minC):
   for smallc in range(change+1):
      coinCount = smallc
      for j in [c for c in changeList if c <= smallc]:
            if minC[smallc-j] + 1 < coinCount:
               coinCount = minC[smallc-j]+1
      minC[smallc] = coinCount
   return minC[change]



if __name__ == '__main__':
    m = int(sys.stdin.read())
    coinCount = [0]*(m+1)
    changelist = [1,3,4]
    print(Change(changelist,m,coinCount))
