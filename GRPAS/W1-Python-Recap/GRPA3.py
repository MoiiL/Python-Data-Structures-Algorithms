def odd_one(ls):
    if len(ls)>=3:
        for i in range(1,len(ls)):
            if type(ls[i-1]) != type(ls[i]):
              return(datatype(ls[i]))
        

def datatype(element):
    if type(element) == int:
        return ('int')
    if type(element) == float:
        return ('float')
    if type(element) == bool:
        return ('bool')
    if type(element) == str:
        return ('str')
    else:
        return None

print(odd_one(eval(input().strip())))
