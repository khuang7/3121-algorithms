'''
Find the maximum contiguous subsequence
of a sequence of array

'''

array = [2, 3, -2, -1, 4, 7, 9]

def maximise_subsequence():
    dp = []

    for i in range(len(array)):
        if i == 0:
            sum_so_far = array[i]
            start = i
            end = i
            potential_new_start = 0
            dp.insert(i, sum_so_far)

        elif array[i] > 0:
            sum_so_far = sum_so_far + array[i]

            if sum_so_far > dp[potential_new_start]:
                start = potential_new_start + 1
                end = i
                dp.insert(i, sum_so_far)
            else:
                end = end + 1
                dp.insert(i, dp[potential_new_start])
        elif array[i] < 0:
            sum_so_far = 0
            potential_new_start = i
            dp.insert(i, dp[i-1])

    print(array)
    print(dp)
    print(start)
    print(end)
    print(array[start:end+1])


maximise_subsequence()



