#Problem set 5
def sumsquare(ls):
    odd, even = 0,0
    for l in ls:
        if l%2 == 0:
            even += l**2
        else:
            odd += l**2
    return ([odd, even])
        
L = eval(input())
print(sumsquare(L))
