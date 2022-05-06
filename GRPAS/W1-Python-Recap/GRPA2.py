#function to check prime number
def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

#function to find Goldback numbers
def Goldbach(num):
    ls = []
    for j in range(2,num):
        for z in range(j,num):
            if prime(j) and prime(z):
                if (j+z == num):
                   ls.append((j,z))
    return ls
            
n=int(input())
print(sorted(Goldbach(n)))
