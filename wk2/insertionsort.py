# we are interested in looking specifically on how to calculate the time

def main():
    A = [5, 4, 3, 2, 1]
    print(insertionsort(A))


def insertionsort(A):
    for j in range(1, len(A)):
        key = A[j]
        # insert A[j] into the sorted sequence A[1..j-1]
        i = j

        while i > 0 and A[i - 1] > key:
            A[i] = A[i - 1]
            i = i - 1
        A[i] = key
    return A

main()