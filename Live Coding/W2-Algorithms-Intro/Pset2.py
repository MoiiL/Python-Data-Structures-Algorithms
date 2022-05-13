#Common elements between two lists

def findIntersection(l1, l2):
    temp = []
    if len(l1) < len(l2):
        for l in l1:
                if l in l2:
                    temp.append(l)
    else:
        for l in l2:
            if l in l1:
                temp.append(l)
    return temp                    
                

set1 = [int(item) for item in input().split()]
set2 = [int(item) for item in input().split()]
result = findIntersection(set1, set2)
result.sort()
print(*result)
