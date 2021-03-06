# Insertion Sort Algorithms

## Time Complexity: O(n<sup>2</sup>)

### Series: T(n) = 0 + 1 + ... + (n-1) || T(n) = n(n-1)/2

<div>

#### Inserting element in a sorted list

##### Code:
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


#### Inserting element in a sorted list using recursion

##### Code:
<pre>
<p>
def InsertList(ls, num):
    n = len(ls)
    if n == 0:
       return ([num])
    if num >= ls[-1]:
       return (ls + [num])
    else:
       return (InsertList(ls[:-1], num) + ls[-1:])
 
 def SortList(ls):
     n = len(ls)
     if n < 1:
         return(ls)
     ls = InsertList(SortList(ls[:-1]), ls[-1])
     return ls    
</p>
</pre>

</div>
