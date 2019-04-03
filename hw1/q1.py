import math


A = [ 1, 3, 3,3,3,3,3, 4, 5, 7, 9 ]


def main():
    left = 4
    right = 8

    index_left = binary_search_l(A, 3)
    print(index_left)


def binary_search_l(array, find):

    lower_bound = 0
    upper_bound = len(array) - 1

    while (upper_bound >= lower_bound):

        mid = math.floor((upper_bound + lower_bound ) / 2)

        if A[mid] < find:
            lower_bound = mid + 1

        elif A[mid] >= find:
            upper_bound = mid - 1

    return lower_bound



def binary_search_r(array, find):
    lower_bound = 0
    upper_bound = len(array) - 1

    while (upper_bound >= lower_bound):

        mid = math.floor((upper_bound + lower_bound ) / 2)
        if A[mid] < find:
            lower_bound = mid + 1

        if A[mid] > find:
            upper_bound = mid - 1

    return lower_bound

main()