#Sorting a combination of strings using swapping method

import copy
def firstsort(ls):
    n = len(ls)
    while n>0:
        flag = False
        for i in range(1,len(ls)):
            if ls[i-1][0] > ls[i][0]:
                ls[i-1] , ls[i] = ls[i], ls[i-1]
                flag = True
        if flag == False:
            break
        n -= 1
    return ls
        
def secondsort(lis):
    n = len(lis)
    while n>0:
        flag = False
        for i in range(1,len(lis)):
            if (int(lis[i-1][1:]) < int(lis[i][1:])):
                if lis[i-1][0] == lis[i][0]:
                    lis[i-1] , lis[i] = lis[i], lis[i-1]
                    flag = True
        if flag == False:
            break
        n -= 1
    return lis

def combinationSort(strList):
    temp = copy.copy(strList)
    return (firstsort(temp),secondsort(firstsort(strList)))
    
