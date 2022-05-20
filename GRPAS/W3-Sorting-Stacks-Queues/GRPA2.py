def DishPrepareOrder(ls):
    temp = set(ls)
    templs = []
    for t in temp:
        templs.append((t,ls.count(t)))
    return(display(templs))
        
def display(ls):
    ls = sorted(ls,key = lambda x : x[1], reverse = True)
    temp = []
    for l in ls:
        temp.append(l[0])
    return temp
    
nums = eval(input())
print(DishPrepareOrder(nums))
