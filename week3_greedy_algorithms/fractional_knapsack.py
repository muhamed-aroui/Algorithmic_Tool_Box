# Uses python3
import sys
import numpy as np

def get_optimal_value(n,capacity, weights, values):
    value = 0.
    # write your code here
    ziplist = list(zip(values,weights))
    nevalues= sorted(ziplist, key=lambda elem: elem[0] / elem[1], reverse=True)
    for i in range(0,n+1):
        if capacity == 0 or i >= n:
            return value
        vi= nevalues[i][0]
        wi= nevalues[i][1]
        a = np.minimum(wi,capacity)
        value = value + (a*vi/wi)
        capacity = capacity - a
        wi = wi - a


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(n,capacity, weights, values)
    print("{:.10f}".format(opt_value))
