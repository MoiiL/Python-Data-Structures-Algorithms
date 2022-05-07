#Problem set 6

#function to sort tuples
def tuple_sort(ls):
    ls = sorted(ls, key = lambda l : l[1])
    for j in range(len(ls)):
        for i in range (len(ls)-1):
            if (ls[i][1] == ls[i+1][1]):
                if (ls[i][0] > ls[i+1][0]):
                   temp = ls[i]
                   ls[i] = ls[i+1]
                   ls[i+1] = temp
    return (ls)
 
def histogram(ls):
    dicto, newls = {}, []
    for l in ls:
        if l not in dicto.keys():
            dicto[l] = ls.count(l)
    for keys,values in dicto.items():
        newls.append((keys,values))
    return (tuple_sort(newls))    
    
L=eval(input())
print(histogram(L))
