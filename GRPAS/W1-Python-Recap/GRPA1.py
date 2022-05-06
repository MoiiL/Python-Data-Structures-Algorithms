#Finding the Minimum Difference in a List
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
