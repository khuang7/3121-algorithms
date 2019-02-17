## Divide and Conquer

#### Mergesort Basics
Mergesort is an example of divide and conquer

1. Divide

    Split the list into halves. We continuously do this via recursion till it reaches one element

2. Conquer

    Solve each subproblem recursively. Sort via mergesort

3. Combine

    Merge the sorted lists together into its own sorted list

#### Pseudocode
```
mergesort(Array, p , r)
if p < r
  q - floor(p + r) / 2
  mergesort(A, p , q)
  mergesort(A, q + 1, r)
  merge(A, p, q, r)
```

#### Recursion Tree
A useful way to keep track of the recursion is via a tree
When tracking through it, remember that it goes towards the left first logically down the tree until it reaches 1 element then it goes back up to the right element. At the end it merges.

![Image of mergesort](https://i.imgur.com/H23uuMx.png)

#### T(n)
The time or efficiency to process n elements of mergesort

