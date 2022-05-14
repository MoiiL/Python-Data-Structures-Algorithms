#Binary search fucntion to track number of comparisions and presence of element in the list

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
