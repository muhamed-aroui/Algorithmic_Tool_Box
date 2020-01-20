# Uses python3
import sys
import random


def RandomizedQuickSort(b):
    c=len(b)
    if c < 2:
        return b
    less = [x for x in b[1:] if x < b[0]]
    same = [x for x in b if x == b[0]]
    great = [x for x in b[1:] if x > b[0]]
    return RandomizedQuickSort(less) + same + RandomizedQuickSort(great)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    a = RandomizedQuickSort(a)
    for x in a:
        print(x, end=' ')
