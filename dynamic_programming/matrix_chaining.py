'''
Multiplying a sequence of matrix such that we
reduce the total amount of multiplications

'''


def main():

    m = [(10,10)]*200
    print(matrix_chaining(m))

def brute(m):

    if len(m) == 1:
        return 0
    if len(m) == 2:
        return m[0][0] * m[1][1] * m[0][1]

    min = 900000000000
    for i in range(1, len(m)):
        l = m[:i]
        r = m[i:]
        n_mult = brute(l) + brute(r) + l[0][0] * r[-1][-1] * r[0][0]
        if n_mult < min:
            min = n_mult
    return min



def matrix_chaining(m):

    dp = [[0] * len(m) for i in range(len(m) + 1)]


    for i in range(0, len(m) - 1):
        dp[i][i+1] = m[i][0] * m[i+1][1] * m[i][1]

    for i in range(3, len(m) + 1):
        for j in range(0, len(m) - i + 1):
            # current window is from j to j + i
            min = 900000000000
            for k in range(0, i-1):
                num_l = dp[j][j+k]
                num_r = dp[j+k+1][j+i-1]

                n_mult = num_l + num_r + m[j][0] * m[j+i-1][1] * m[j+k][1]
                if n_mult < min:
                    min = n_mult

            dp[j][j+i-1] = min
    #print(dp)
    return dp[0][len(m)-1]

main()
