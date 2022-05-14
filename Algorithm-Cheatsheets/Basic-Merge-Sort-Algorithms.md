# Merge Sort Algorithms

### Series: T(n) = 2<sup>k</sup>T(n/2<sup>k</sup>) + kn

### Time Complexity: O(nlogn)

#### Using merge sort algorithms to sort a list

##### Code:
<pre>
<p>
def merge(A,B):
    m, n = len(A), len(B)
    C, i, j ,k = [], 0, 0, 0
    while k < (m+n):
         if i == m:
             C.extend(B[j:])
             k = k + (n-j)
         elif j == n:
             C.extend(A[i:])
             k = k + (n-1)
         elif A[i] < B[j]:
             C.append(A[i])
             i, k = i+1 , k+1
         else:
             C.append(B[j])
             j, k = j+1, k+1
      return C
       
</p>
</pre>


#### Using merge sort algorithms recursively to sort a list

##### Code:
<pre>
<p>
def MergeSort(A):
    n = len(A)
    if n <= 1:
        return A
    l = MergeSort(A[:n//2])
    r = MergeSort(A[n//2:])
    B = merge(l,r)
    return B         
</p>
</pre>
