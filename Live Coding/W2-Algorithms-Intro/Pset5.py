def listcreator(l1,l2):
    for l in l2:
        if l not in l1:
                l1.append(l)
    l1 = sorted(l1)
    return l1
                


def listUnion(l1,l2):
    if len(l1)>len(l2):
        temp = listcreator(l1,l2)
    else:
        temp = listcreator(l2,l1)
    return temp
        

set1 = [int(item) for item in input().split()]
set2 = [int(item) for item in input().split()]
print(*listUnion(set1, set2))
