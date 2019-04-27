'''
An example of the cutting rod DP problem
Found in textbook, a range of cuts with different prices, we want to
maximise the price for a certain amount of cuts

'''

length = [1,2,3,4,5,6,7,8]
price = [1,5,8,9,10,17,17,20]
r = []

def main():
    top_down_rod(price, 30)


def naive_cut_rod(price, n):
    if n == 0:
        return 0
    q = -1
    for i in range(0,n-1):
        q = max(q,price[i] + naive_cut_rod(price, n-i))
    print(q)
    return q


def top_down_rod(price, n):
    for i in range(0,n-1):
        r[i] = -100000
    return top_down_rod(price, n, r)


main()



