def findPair(l, pairSum):
    for i in l:
        for j in l:
            if i + j == pairSum:
                return True
    return False


L = [int(item) for item in input().split()]
pairsum = int(input())
print(findPair(L, pairsum))
