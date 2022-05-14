### A python function combinationSort(strlist) that takes a list of unique strings strlist as argument and each string is a combination of a letter from a to z and a number from 0 to 99. This function sorts the list and returns two lists : l1 and l2
### l1 : First list returns all the strings arranged in ascending order using the first character of the strings
### l2: Second list returns all the strings arranged in descending order using the list obtained from l1 and using the numbers in the remaining characters in the string.

####Code:

<pre>
<p>
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
    print (firstsort(temp),secondsort(firstsort(strList)))
    
</p>
</pre>

