#Problem Set 2
def del_char(s,c):
    if len(c) == 1:
        temp = ""
        for l in s:
            if l != c:
                temp += l
        return temp
    return s
    
s = input()
c = input()
print(del_char(s,c))
