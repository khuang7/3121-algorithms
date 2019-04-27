'''
Coin denomination dynamic programming style
'''
import pandas as pd

S = [1,2,3, 5, 10]
m = len(S)
n = 10

def recursive_coin(S, m, n):
    if (n == 0):
        return 1
    if (n < 0):
        return 0;
    if (m <= 0 and n >= 1):
        return 0
    return recursive_coin(S, m - 1, n) + recursive_coin(S, m, n - S[m - 1]);


def bottoms_up_sol():
    dp = [[0 for x in range(len(S))] for x in range(n+1)]

    # zero coins case
    for i in range(m):
        dp[0][i] = 1


    for i in range(1, n+1):
        for j in range(m):


            '''
            
            '''
            if i - S[j] >= 0:
                x = dp[i-S[j]][j]
            else:
                x = 0

            if j >= 1:
                y = dp[i][j-1]
            else:
                y = 0

            dp[i][j] = x + y


    print(pd.DataFrame(dp))

    print(dp[n][len(S)-1])






bottoms_up_sol()