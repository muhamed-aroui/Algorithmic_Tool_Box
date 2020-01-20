# Uses python3
import sys

def optimal_sequence(n):
    sequence = []

    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + 1
        if i % 2 == 0:
            s[i] = min(s[i // 2] + 1, s[i])
        if i % 3 == 0:
            s[i] = min(s[i // 3] + 1, s[i])
    #print('arr',arr)
    while n >= 1:
        sequence.append(n)
        #print('sequence',sequence)
        if s[n] == s[n - 1] + 1:
            n = n - 1
        elif n % 2 == 0 and s[n // 2] == s[n] - 1:
            n = n // 2
        elif n % 3 == 0 and s[n // 3] == s[n] - 1:
            n = n // 3

    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
