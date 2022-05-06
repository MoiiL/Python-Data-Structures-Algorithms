## Write a function Find_Min_Difference(L,P) that accepts a list L of integers and P (positive numbers) where the size of L is greater than P. Pick P different elements from list L where the difference between the maximum and mininum values in selected elements is minimum compared to other differences in possible subset of p elements. The fucntion returns the minimum differencd value.

## Code

<pre>
<p>
def find_Min_Difference(L,P):
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i]>L[j]:
               L[i],L[j]=L[j],L[i]
    start = 0
    min_diff = max(L)
    while len(L)-start >= P:
        temp_ls = L[start:start + P]
        diff = temp_ls[-1] - temp_ls[0]
        if start == 0:
            min_diff = diff
        if diff < min_diff:
            min_diff = diff
        start += 1
    return min_diff
        
L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))
</p>
<pre>
