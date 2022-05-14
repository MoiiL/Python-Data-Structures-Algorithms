# FInding the maximum number in a list

def findLargest(ls):
    start,end = 0, len(ls)
    l, r = ls[0], ls[-1]
    
    while(start<end):
        mid = (start+end)//2
        if(l>ls[mid]):
            end = mid
        else:
            start = mid+1
    return ls[start-1]
  
  
