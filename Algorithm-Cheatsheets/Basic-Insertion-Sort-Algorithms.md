# Insertion Sort Algorithms

## Time Complexity: O(n<sup>2</sup>)

### Series: T(n) = 0 + 1 + ... + (n-1) || T(n) = n(n-1)/2

#### Code: Inserting element in a sorted list
<pre>
<p>
def InsertionSort(ls):
    n = len(ls)
    if n < 1:
       return ls
    for i in range(n):
       j = i
       while (j > 0 and ls[j] < ls[j-1]):
           ls[j], ls[j-1] = ls[j-1], ls[j]
           j -= 1
    return ls
</p>
</pre>


#### Code: Inserting element in a sorted list using recursion
<pre>
<p>
def insert(ls, num):
    n = len(ls)
    if n == 0:
       return ([num])
    if num >= ls[-1]:
       return (ls + [num])
    else:
       return (insert(ls[:-1], num) + ls[-1:])
 
 def sortList(ls):
     n = len(ls)
     if n < 1:
         return(ls)
     ls = insert(sortList(ls[:-1]), ls[-1])
     return ls    
</p>
</pre>

