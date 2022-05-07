#Problem Set 1

def prime(num):
    for i in range(2,num):
        if num%i == 0:
          return False
    return True

def prime_product(n):
    for i in range(2,n):
        for j in range(i,n):
            if prime(i) and prime(j):
               if i*j == n:
                  return True
                  break
    return False

n = int(input())
print(prime_product(n))
