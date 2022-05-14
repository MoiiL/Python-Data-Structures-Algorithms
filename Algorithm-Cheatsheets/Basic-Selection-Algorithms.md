# Selecting Sort Algorithms

#### Series Formula
T(n) = n + (n-1) + (n-2) + ... + 1  ||  T(n) = n(n+1)/2

### Time Complexity : O(n<sup>2</sup>)

#### Code: Selection sort in a list
<pre>
<p>
def selectionSort(ls):
   n = len(ls)
   if n < 1:
      return (ls)
   for i in range(n):
      minposition = i
      for j in range(i+1,n):
          if ls[j] < ls[minposition]:
             minposition = j
      ls[i], ls[minposition] = ls[minposition], ls[i]
    return ls
</p>
</pre>

