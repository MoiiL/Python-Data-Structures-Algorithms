### A python function binarySearchIndexAndComparisons(L,K) that accepts a list L sorted in ascending order and an integer k that returns a tuple of true/false and a number of comparisions made while searching for the element k in the list L using binary search. 
#### Code:
<pre>
<p>
def binarySearchIndexAndComparisons(ls,n):
    global count
    count += 1
    if ls == []:
       return (False, count)
    mid = len(ls)//2
    if n == ls[mid]:
       return (True, count-1)
    if n < ls[mid]:
       return (binarySearchIndexAndComparisons(ls[:mid],n))
    else:
       return (binarySearchIndexAndComparisons(ls[mid+1:],n))
    
count = 0
</p>
</pre>
