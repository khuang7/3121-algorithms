
'''
Initialized global variables
https://stackoverflow.com/questions/2631726/how-to-determine-the-longest-increasing-subsequence-using-dynamic-programming
'''
arr = [3, 10, 15, 2, 4, 6, 20, 19, 51]
DP = []
prev = []
DP.append(1)
prev.append(1)
maxLength = 1
bestEnd = 0

def main():
    my_attempt(arr)

def longest_subsequence_naive(arr, n):
    '''
    Returns the length of the longest subsequence of array
    n is the length of the array
    '''

    global maxLength, bestEnd, prev

    for i in range(0, n-1):
        DP.insert(i, 1)
        prev.insert(i, -1)

        # backwards starting from i-1
        for j in range(i-1, -1, -1):
            if DP[j] + 1 > DP[i] and arr[j] < arr[i]:
                DP[i] = DP[j] + 1
                prev[i] = j
        if DP[i] > maxLength:
            bestEnd = i
            maxLength = DP[i]

    print(prev)
    return maxLength



def recursive_solution(arr, bigger_than=None):
    """Finds the longest increasing subsequence of arr that is
    bigger than bigger_than and returns it.  This solution is O(2^n)."""

    # Base case: nothing is remaining.
    if len(arr) == 0:
        return arr

    # Recursive case 1: exclude the current element and process the remaining.
    best_sequence = recursive_solution(arr[1:], bigger_than)

    # Recursive case 2: include the current element if it's big enough.
    first = arr[0]

    if (bigger_than is None) or (first > bigger_than):
        sequence_with = [first] + recursive_solution(arr[1:], first)

        # Choose whichever of case 1 and case 2 were longer.
        if len(sequence_with) >= len(best_sequence):
            best_sequence = sequence_with
    return best_sequence




max_sub_length = 0
mem = []
sub = []
def my_attempt(arr):
    global max_sub_length
    global mem

    for i in range(0,len(arr)):
        if i == 0:
            max_sub_length = 1
            mem.insert(i, 1)
            sub.insert(i, arr[i])

        elif arr[i] > arr[i-1]:
            mem.insert(i, mem[i-1] + 1)
            max_sub_length = max_sub_length + 1




        elif arr[i] < arr[i-1]:
            mem.insert(i, mem[i-1])
    print(sub)

main()
