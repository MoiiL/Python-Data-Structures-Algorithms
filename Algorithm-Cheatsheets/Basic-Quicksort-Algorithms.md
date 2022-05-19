## QuickSort Algorithms


### Divide and Conquer Method I

<ul>
    <li>Choose Pivot element(first/last/random element)</li>
     <li>Store elements less that pivot in left subarray</li>
     <li>Store elements greater than pivot in right subarray</li>
     <li>Call quicksort recursively on left subarray</li>
     <li>Call quicksort recursively on right sub array</li>
</ul>

##### Series: T(n) = 2T(n/2)-n
##### Time Complexity: Best/Average Case - O(nlogn)  | Worst Case - O(n<sup>2</sup>)
<pre>
<p>
# Quicksort (C.A.R Hoare) method / Pivot method
# L -> List, l -> start index, r -> end index

def quicksort(L,l,r): 
    if (r - l <= 1):
       return (L)
    pivot, lower, upper = L[l], l+1, l+1
    for i in range(l+1, r):
        if L[i] > pivot:
            upper += 1
        else:
            L[i], L[lower] = L[lower], L[i]
            lower, upper = lower + 1, upper + 1
    L[l], L[lower-1] = L[lower-1], L[l]
    lower -= 1
    quicksort(L,l,lower)
    quicksort(L,lower+1,upper)
    return (L)       
</p>
</pre>


### Quicksort method II

<pre>
<p>

def quicksort(arr,left,right):
   if left < right:
       partition_position = partition(arr, left, right)
       quicksort(arr,left,partition_position-1)
       quicksort(arr,partition_position+1,right)
       
def partition(arr,left,right):
    i = left
    j = right - 1
    pivot = arr[right]
    while i < j:
         while i < right and arr[i] < pivot:
             i += 1
         while j > left and arr[j] >= pivot:
             j += 1
         if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
         arr[i], arr[right] = arr[right], arr[i]
    return i
            
</p>
</pre>

