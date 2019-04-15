'''
Balanced Partition
Given N integers, split both and minimise the sum between them
'''




def main():
    print(balanced_partition())

def balanced_partition():
    v = w = arr = [0, 1, 6, 7]
    c = int(sum(arr) / 2)

    partition1 = max_value2(c, v)
    partition2 = [i for i in v if i not in partition1]
    return [partition1, partition2]

def max_value2(c, v):
    #DP = [[0 for i in range(c + 1)] for j in range(len(v))]
    DP = [[0] * (c+1) for i in range(len(v))]
    #came_from = [[for i in range(c+1)] for j in range(len(v))]
    came_from = [[(-1, -1)] * (c+1) for i in range(len(v))]

    used = [[False] * (c+1) for i in range(len(v))]
    w = v

    for i in range(len(v)):
        for j in range(c + 1):
            if i == 0 or j == 0:
                DP[i][j] = 0
            elif j-w[i] >= 0 and DP[i-1][j-w[i]] + v[i] > DP[i-1][j]:
                DP[i][j] = DP[i-1][j-w[i]] + v[i]
                came_from[i][j] = (i-1, j-w[i])
                used[i][j] = True
            else:
                DP[i][j] = DP[i-1][j]
                used[i][j] = False
                came_from[i][j] = (i-1, j)


    return result

main()