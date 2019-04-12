'''
A simple fibonacci but using memoization and dynamic programing
An introduction to the basics of dynamic programming
'''

memo = {}

def main():
    print(fib_naive(5))
    print(fib_bottoms_up(4))

def fib_naive(n):
    '''
    We used the recursive method in order to fine
    every combination from f(n) down the tree

    This is EXPONENTIAL and bad..
    '''
    #fib(1) and fib(2) are 1
    if n == 1 or n == 2:
        return 1
    else:
        f = fib_naive(n-1) + fib_naive(n-2)
    return f

def fib_bottoms_up(n):
    '''
    We iteratively start from 1..n
    Store it in memoization
    WE can actually just keep updating as we go up
    O(n) TIME
    '''
    for k in range(1,n + 1):
        if k <= 2:
            f = 1
        else:
            f = memo[k-1] + memo[k-2]
        memo[k] = f
    return memo[n]

main()