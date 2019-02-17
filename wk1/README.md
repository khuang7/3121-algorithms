## Divide and Conquer

#### Mergesort
Mergesort is an example of divide and conquer

*1. Divide*

    Split the list into halves. We continuously do this via recursion till it reaches one element

*2. Conquer*

    Solve each subproblem recursively. Sort via mergesort

*3. Combine*

    Merge the sorted lists together into its own sorted list

This recursion is *bottoms up* 

```
mergesort(Array, p , r)
if p < r
  q - floor(p + r) / 2
  mergesort(A, p , q)
  mergesort(A, q + 1, r)
  merge(A, p, q, r)
```
