'''
Given an N proposals, find the MAX num of dams
where for each proposal there is x metres from head of stream
and for each proposal there is r metres (dam must have not have another dam within r metres)

'''

x = [3, 7, 11, 15]
r = [1, 1, 3, 1]

def main():
    max_dam()


def max_dam():
    DP = []
    for i in range(0, len(x)):
        if i == 0:
            DP.insert(i,1)

        elif x[i-1] + r[i-1] <= x[i] and x[i] - r[i] >= x[i-1]:
            DP.insert(i,DP[i-1] + 1)

        else:
            DP.insert(i, 1)
            for j in range(i-2, -1, -1):
                if x[j] + r[j] <= x[i] and x[i] - r[i] >= x[j]:
                    if DP[i] <= DP[j]:
                        DP[i] = DP[j] + 1

            if DP[i] == 1:
                DP[i] = DP[i-1]
    print(DP[len(x)-1])
main()




