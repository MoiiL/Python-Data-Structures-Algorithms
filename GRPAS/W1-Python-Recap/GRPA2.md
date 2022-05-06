## Write a Goldbach function (n) where n is a positive even number (n>2) that returns a list of tuples. Each tuple (a,b) where a<=b, a and b should be prime numbers and the sum of a and b should be n.
## Goldbach's Conjecture - every even number greater than 2 is the sum of two prime numbers.

## Code

<pre>
<p>
def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

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
</p>
<pre>
