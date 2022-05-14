# Basic Search Algorithms

### Time Complexity: O(n) (Worst Case)
#### Code: Native Search - simplistic search for element in a list
<pre>
<p>
def nativesearch(n,ls):
     for l in ls:
        if n == l:
           return True
     return False   
</p>
</pre>

### Time Complexity: O(log n)
#### Code: Binary Search in a Sorted List using Recursion 
<pre>
<p>
def binarysearch(n,ls):
    if ls ==   []:
       return False
    mid = len(ls)//2
    if n == ls[mid]:
       return True
    if n < ls[mid]:
       return (binarysearch(n, ls[:mid]))
    else:
       return (binarysearch(n, ls[mid+1:]))
</p>
</pre>

