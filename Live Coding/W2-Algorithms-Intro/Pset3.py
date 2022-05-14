def subordinates(ls):
    max_len = len(ls)
    count = 0
    temp = []
    for l in ls:
        if ls.count(l) > 1 and l not in temp:
            count += 1
            temp.append(l)
    diff = max_len - count
    ls = sorted(ls)
    return ((ls,diff))
    
print(subordinates(eval(input())))
