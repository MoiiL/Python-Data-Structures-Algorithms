# Comparing Time Complexity

### Time Complexity : O(n<sup>2</sup>)

#### Code: Finding duplicate elements in a list
<pre>
<p>
def duplicates(ls):
   for i in range(len(ls)):
      for j in range(i,len(ls)):
         if ls[i] == ls[j]:
             return False
    return True   
</p>
</pre>

### Time Complexity: O(n)

#### Code: Finding maximum element in a list
<pre>
<p>
def maxElement(ls):
    maxvalue = ls[0]
    for ele in ls:
        if ele > maxvalue:
           maxvalue = ele
    return maxvalue
</p>
</pre>

### Time Complexity: O(n<sup>3</sup>)
#### Code: Matrix mulitplication - Two Matrices
<pre>
<p>
def matrixmulti(matA, matB):
    m, n, p = len(matA), len(matB), len(matB[0])
    c = [[ 0 for i in range (p)]
             for j in range (m)]
    for i in range(m):
        for j in range(n):
            for k in range(p):
               c[i][j] = c[i][j] + matA[i][k] * matB[k][j]
    return c
</p>
</pre>


### Time Complexity: O(log n)
#### Code: Counting number of bits 
<pre>   
<p>
def count_bits(n):
    count = 1
    while n>1:
      count = count + 1
      n = n // 2
    return count
</p>
</pre>
