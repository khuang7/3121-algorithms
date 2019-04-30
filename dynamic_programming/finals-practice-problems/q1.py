'''

Consider a 2-D map with a horizontal river passing through its center. There are n
cities on the southern bank with x-coordinates a1 . . . an and n cities on the northern
bank with x-coordinates b1 . . . bn. You want to connect as many north-south pairs
of cities as possible, with bridges such that no two bridges cross. When connecting
cities, you are only allowed to connect the the i
th city on the northern bank to the
ith city on the southern bank.
'''


a = [0, 1, 3, 4, 5, 100]
b = [0, 100, 3, 4, 5, 1]

def river():

    dp = []

    for i in range(len(a)):
            if i == 0:
                dp.insert(i,0)
            elif a[i] >= a[i - 1] and b[i] >= b[i - 1]:
                dp.insert(i, dp[i - 1] + 1)
            else:
                dp.insert(i, dp[i - 1])
           # else:
               # m = 1
                #for j in range(1, i):
                 #   if a[i] >= a[j] and b[i] >= b[j]:
                  #      res = dp[j] + 1
                   # else:
                    #    res = 1
                    #m = max(res, m)

    print(dp)


river()
