def main():
    A = [2., 4., 6., 1., 2., 3., 4., 5.]
    new_array = mergesort(A)
    print(new_array)

def mergesort(A):

    if len(A) <= 1:
      return A
    n = len(A)
    L = mergesort(A[0:n // 2])
    R = mergesort(A[n // 2:n])
    return merge1(L, R)

def merge1(L, R):

    result = []
    i = 0
    j = 0
    while (len(L) > i and len(R) > j):
        if L[i] <= R[j]:
            result.append(L[i])
            i = i + 1
        else:
            result.append(R[j])
            j = j + 1

    if i == len(L):
        for j in range(j, len(R)):
            result.append(R[j])
    else:
        for i in range(i, len(L)):
            result.append(L[i])

    return result

main()