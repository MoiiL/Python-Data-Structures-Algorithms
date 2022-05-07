#Problem set 3

def shuffle(l1, l2):
    l1_len, l2_len = len(l1), len(l2)
    max_len = max(l1_len, l2_len)
    temp = []
    for i in range(max_len):
        if l1_len > i:
            temp.append(l1[i])
        if l2_len > i:
            temp.append(l2[i])
    return temp
     
L1 = eval(input())
L2 = eval(input())
print(shuffle(L1,L2))
