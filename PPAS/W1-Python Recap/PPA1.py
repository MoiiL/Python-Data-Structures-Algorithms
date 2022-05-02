#A function to check primes
def prime(n):
    ls = []
    for i in range(1,n+1):
        if (n%i) == 0:
            ls.append(i)
    return(ls == [1,n])

#A fucntion to check twin primes having a difference of two
def Twin_Primes(n,m):
    ls = []
    for i in range(n,m+1):
        if prime(i) and prime(i+2):
            ls.append((i,i+2))
    return ls
            
n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))
