'''
Finds the longest common subsequence of two sequences
(Given as 2 arrays)
'''

from pandas import DataFrame

x = [0, 3, 9, 8, 3, 9, 7, 9, 7, 0,]
y = [0, 3, 3, 9, 9, 9, 1, 7, 2, 0,6]

def main():
    longest_subsequence(x, y)

def longest_subsequence(a, b):
    DP = [[0] * (len(a)) for i in range(len(b))]
    back_trace = [[(-1,-1)] * (len(a)) for i in range(len(b))]
    went_here = [[False] * (len(a)) for i in range(len(b))]

    for i in range(1, len(b)):
        for j in range(1, len(a)):
            if a[j] == b[i]:
                DP[i][j] = DP[i - 1][j - 1] + 1
                back_trace[i][j] = (i-1, j-1)
                went_here[i][j] = True
            else:
                if DP[i - 1][j] >= DP[i][j-1]:
                    DP[i][j] = DP[i-1][j]
                    back_trace[i][j] = (i-1,j)
                else:
                    DP[i][j] = DP[i][j-1]
                    back_trace[i][j] = (i, j-1)

    results = []
    cur_grid = (len(y)-1, len(x)-1)
    while back_trace[cur_grid[0]][cur_grid[1]] != (-1,-1):
        if went_here[cur_grid[0]][cur_grid[1]]:

            results.append(b[cur_grid[0]])
        cur_grid = back_trace[cur_grid[0]][cur_grid[1]]



    print(DataFrame(DP))
    print(DataFrame(back_trace))
    print(DataFrame(went_here))
    print(results)

main()