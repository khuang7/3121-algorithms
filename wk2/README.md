## Complexity

The running time of an algorithm in particular is the
number of steps.

- We try to make it as machine independent as possible
- A constant time for each line of code in the pseudo code
(but in real life it is always differnet obviously)
- We assume that each execution of the ith line takes time c, where c is a constant

With insertion sort we present the time cost of each statement and the number of times
each statement is executed.

![Imgur](https://i.imgur.com/IiVWtMU.png)

In the best case scenario if we add all these up we are
able to express it in terms of an + b which makes it LINEAR

If the list is initially reversed we get the worst case scenario. Because we have to
compare each element in the entire sorted array. If we add it up in this case
we get a quadratic function. Which makes it an^2 

( not really sure how in detailed we have to be? should i know how to reach each case?)


## Rate of growth
This is what interests us more. In the rate of growth we only consider the leading term
of the formula ignoring the lower order terms and coefficients.

#### Asymptotic Notation
A way to describe running times of an algorithm by identifying its behaviour as it grows. Typically it is like the following
![Imgur](https://i.imgur.com/3PvRATx.png)

Growth rate = asymptotic bheaviour.

#### theta
We use theta notation to express a g(n) which is a set of functions
For some positive constants
f(n) lies in between c1g(n) and c2g(n)

g(n) is asymptotically tight bound for f(n)
For every memsber f(n) in  Theta(g(n))

Bounded from above and below which is the same as o-notation + omega notation 
f(n) = Theta(g(n))

#### o notation
Upper bound we use O-notation. aka worst case
 
O(g(n)) = {f(n) with positive constnts c and n
0 <= f(n) <= cg(n)

think of g(n) as a growth rate and f(n) as a growth rate as a function of n
and that after a certain point, f(n) will never be higher than g(n)

Some constant multiple of g(n) is an upper bound on f(n)

#### omega
Lower bound we use omega

Basically the same equation as above but the inequality is swapped

No matter what input of size n, the running time on that input is at least a constant x g(n)

## Mergesort Complexity aka recurrence
T(n) <= 2T(n/2) + cn

also the *DEPTH OF THE TREE?

If we consider each level of the recursion

- Level 1 - single problem of size n
- Level 2 - 2 problems of size n/2
- Level 3 - 4 problems of size n/4

Every level takes cn time at most to process

At each level the sub-problems increase by 2 ^ j but each problem has shrunk by n/2^j

Each layer takes at most 2^j(cn/2^j) to solve where j is the level which becomes just cn

If we sum all levels of the recursion. the same upper bound is always applied. The number of times the input must be halved in order to reduce the size from n to 2 is log(n)


**Summing cn work over log n levels of recursion we get
O(nlogn) running time. (this part doesnt make sense to me..)**


## Master Method
A way to provide bounds on recurrences

T(n) = aT)n/b + f(n)
a >= 1, b > 1, f(n) is a given function.

characterizes a divide and conquery algorithm that
- Creates a sub-problems
- which is divided into 1/b the size of the original problem.
- the divide and combine steps take f(n) time

Another case we didn't really consider is when theres an odd number of elements.
The splitting is different, however we neglect this fact. We tend to omit floors, ceilings and boundary conditions.

![Imgur](https://i.imgur.com/CvGhdbB.png)
Splitting into 2 (a) subproblems. and each time we split the list in 1/2 (1/b)

need to explore this in more detail!!

