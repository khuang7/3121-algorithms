'''
Turtle Stack Question - Dynamic Programming
A total of n turtles each with strength and weight
Find the tallest possible tower possible with a combination of these turtles.
'''

# sorted by weight and sum
weights =  [1, 3, 9, 3, 10, 12]
strength = [1, 3, 1, 10, 10, 11]



def highest_stack():

    dp = [[0] * len(weights) for i in range(len(weights))]

    for i in range(1, len(weights)):
        for j in range(1, len(weights)):
            dp[i][j] = min(dp[i][j], dp[i-1][j])

            if strength[i] > dp[i-1][j-1]:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + weights[i])






