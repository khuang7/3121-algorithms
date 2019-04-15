'''
Skiers go fastest with skis whose length is about their height. Your team consists of n
members, with heights h1, h2, . . . , hn. Your team gets a delivery of m ≥ n pairs of skis, with
lengths l1, l2, . . . , lm. Your goal is to write an algorithm to assign to each skier one pair of
skis to minimize the sum of the absolute differences between the height hi of the skier and
the length of the corresponding ski he got
'''

import pandas as pd
import math


ski = [0, 2, 5, 6, 7, 3, 2, 5]
ppl = [0, 1, 4, 100]

def minimise():
    dp = [[0] * (len(ski)) for i in range(len(ppl))]

    for i in range(1, len(ppl)):
        dp[i][0] = 100000

    for i in range(1, len(ppl)):
        for j in range(1, len(ski)):
            if i>j:
                dp[i][j] = 100000
            else:
                dp[i][j] = min(dp[i-1][j-1] + abs(ski[j] - ppl[i]) , dp[i][j-1])

    print(pd.DataFrame(dp))
    print(dp[len(ppl) - 1][len(ski)- 1])
minimise()

