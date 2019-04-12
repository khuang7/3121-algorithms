'''
An example of the cutting rod DP problem

'''

length = [1,2,3,4,5,6,7,8]
price = [1,5,8,9,10,17,17,20]

def main():
    print(cut_rod(price, 3))

def cut_rod(price, n):
    if n == 0:
        return 0
    q = -1
    for i in range(0,n-1):
        q = max(q,price[i] + cut_rod(price, n-i))
    print(q)
    return q

main()



