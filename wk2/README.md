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

#### theta
We use theta notation to express a g(n) which is a set of functions
For some positive constants
f(n) lies in between c1g(n) and c2g(n)

g(n) is asymptotically tight bound for f(n)
For everymemyber f(n) in  Theta(g(n))

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

No matter what input of size n, the runnign time on that input is at least a constant x g(n)

#### The reason for the constants
Different computers run algorithms in different ways. Some may require more steps to complete, so therefore the c is there to account for these situations

The n greater than a certain number is required in examples of cases where computers are required to load in memory. There are these starting cases, so therefore it is better to just consider larger N (?)


## Master Theorem

