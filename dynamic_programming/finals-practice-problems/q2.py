'''
The bigger the elephant the higher IQ it has?
'''

weights = [3, 2, 10, 4, 3, 8]
iq = [3, 6, 9, 10, 1, 4]

def longest_sequence():

    dp = []

    for i in range(len(weights)):
        if i == 0:
            dp.insert(i, 1)

        elif weights[i] > weights[i-1] and iq[i] < iq[i-1]:
            dp.insert(i,dp[i-1] + 1)

        else:
            find_max = 1
            for j in range(i,-1,-1):
                if weights[i] > weights[j] and iq[i] < iq[j]:
                    find_max = find_max + 1
            if find_max < dp[i-1]:
                dp.insert(i,dp[i-1])
            else:
                dp.insert(i, find_max)

    print(dp)

longest_sequence()