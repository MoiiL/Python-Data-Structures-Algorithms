#Problem set 4

def expanding(l):
    ls, temp = [], True
    for i in range(len(l)-1):
        diff = l[i]-l[i+1]
        ls.append(abs(diff))
    for i in range(len(ls)-1):
        if ls[i] >= ls[i+1]:
            temp = False
            break
    return temp
            

L = eval(input())
print(expanding(L))
