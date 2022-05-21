#Function to check the operands +, -,*, ** and /
def check_operand(s,n1,n2):
    temp = 0
    if s == '+':
        temp = n2 + n1
    elif s == '-':
        temp = n2 - n1
    elif s == '*':
        temp = n2 * n1
    elif s == '/':
        temp = n2/n1
    elif s == '**':
        temp = n2**n1
    return temp

#Function to evaluate the expression
def EvaluateExpression(ls):
    ls = ls.split()
    num , i = len(ls) , 0
    temp = []
    while num > 0:
        n = ls[i]
        try:
            temp.append(int(n))
        except:
            n1 = temp.pop()
            n2 = temp.pop()
            t = check_operand(ls[i], n1, n2)
            temp.append(t)
        num -= 1
        i += 1
    return str(temp[0])

print(float(EvaluateExpression(input())))
