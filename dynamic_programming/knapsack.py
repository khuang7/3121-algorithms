

v = [0, 2, 3, 5, 7]
w = [0, 3, 4, 6, 10]

def main():
    print(max_value2(15))

def max_value1(c):

    DP = [0] * (c + 1)

    for i in range(min(w), c+1):
        #res = 0
        #for j in range(len(v)):
        #    if i-w[j] >= 0:
        #        res = max([DP[i - w[j]] + v[j], res])
        #DP[i] = res
        DP[i] = max([DP[i - w[j]] + v[j] for j in range(len(v)) if i - w[j] >= 0])

    print(DP)
    return DP[c]

def max_value2(c):
    DP = [[0 for i in range(c + 1)] for j in range(len(v))]

    print(DP)

    for i in range(len(v)):
        for j in range(c + 1):
            if i == 0 or j == 0:
                DP[i][j] = 0
            elif j-w[i] >= 0 and DP[i-1][j-w[i]] + v[i] > DP[i-1][j]:
                DP[i][j] = DP[i-1][j-w[i]] + v[i]
            else:
                DP[i][j] = DP[i-1][j]
    print(DP)
    return DP[len(w) - 1][c]

main()