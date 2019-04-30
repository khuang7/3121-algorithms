'''
Your shipping company has just received N shipping requests (jobs). For each request
i, you know it will require ti trucks to complete, paying you di dollars. You have T
trucks in total. Devise an algorithm to select jobs which will bring you the largest
possible amount of money.
'''

import pandas as pd

trucks = [0, 5,3,2, 1]
value = [0,20,50,90, 100]
truck_cap = 8

def maximise_value():
    dp = [[0] * truck_cap for i in range(len(trucks))]

    for i in range(len(trucks)):
        for j in range(truck_cap):
            if i == 0:
                if trucks[i] <= j:
                    dp[i][j] = value[i]
            if j ==0:
                dp[i][j] == 0

            # the new truck we are trying to add is impossible to add
            elif trucks[i] > j:
                dp[i][j] = dp[i-1][j]

            elif dp[i-1][j-trucks[i]] + value[i] > dp[i-1][j]:
                dp[i][j] = dp[i - 1][j - trucks[i]] + value[i]

            else:
                dp[i][j] = dp[i-1][j]


    print(pd.DataFrame(dp))


maximise_value()