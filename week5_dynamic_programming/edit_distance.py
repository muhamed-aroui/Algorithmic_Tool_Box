# Uses python3
def edit_distance(s, t):
    a = len(s) + 1
    b = len(t) + 1

    P = [[0 for x in range(b)] for x in range(a)]
    #print('1',P)

    '''for i, j in zip(range(a), range(b)):
        P[i][0] = i
        P[0][j] = j'''
    #print(P)

    for i in range(a):
        for j in range(b):

            insertion = P[i][j - 1] + 1
            deletion = P[i - 1][j] + 1
            mismatch = P[i - 1][j - 1] + 1
            match = P[i - 1][j - 1]
            if i ==0:
                P[i][j]= j
            elif j==0:
                P[i][j]=i
            elif (s[i - 1] == t[j - 1]):
                P[i][j] = min(insertion, deletion, match)
            else:
                P[i][j] = min(insertion, deletion, mismatch)

    return P[a - 1][b - 1]
    # A Dynamic Programming based Python program for edit
# distance problem
'''def edit_distance(str1, str2):
    m=len(str1)
    n=len(str2)
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n+1)] for x in range(m+1)]

    # Fill d[][] in bottom up manner
    for i in range(m+1):
        for j in range(n+1):

            # If first string is empty, only option is to
            # isnert all characters of second string
            if i == 0:
                dp[i][j] = j    # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i    # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])    # Replace

    return dp[m][n]'''


if __name__ == "__main__":

       print(edit_distance(input(), input()))
