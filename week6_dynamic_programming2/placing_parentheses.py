# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False
def MinAndMax(M, m, i, j, op):
    min_val = 1000000000000000
    max_val = -100000000000000
    for k in range(i, j):
        a = evalt(M[i][k], M[k + 1][j], op[k])
        b = evalt(M[i][k], m[k + 1][j], op[k])
        c = evalt(m[i][k], M[k + 1][j], op[k])
        d = evalt(m[i][k], m[k + 1][j], op[k])
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    return min_val, max_val
def get_maximum_value(d,op):
    #write your code here
    n = len(d)
    m = [[None for x in range(n)] for x in range(n)]
    M = [[None for x in range(n)] for x in range(n)]

    for i in range(n):
        m[i][i] = d[i]
        M[i][i] = d[i]

    for s in range(0, n):
        for i in range(0, n - s):
            j = i + s
            if i != j:
                m[i][j], M[i][j] = MinAndMax(M, m, i, j, op)

    return M[0][n - 1]



if __name__ == "__main__":
    dataset = input()
    op = []
    d = []

    for opsign in dataset:
        if opsign in ['+', '-', '*']:
            op.append(opsign)
        else:
            d.append(int(opsign))

    print(get_maximum_value(d, op))
