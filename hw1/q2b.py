


def main():
    hi = set()

    array = [7, 1, 9,3, 5, 3]
    sum = 100

    for i in array:
        if sum - i in hi:

            return True
        else:
            hi.add(i)

    return False

print(main())