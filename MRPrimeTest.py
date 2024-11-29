import random
def isPrime(n):
    #generate witness randomly 
    for i in range(10):
        a = random.randint(1, n - 1)
        if a%n == 0: return True
        q = n - 1
        k = 0 
        while q % 2 == 0:
            q = q //2 
            k +=1
        b = pow(a, q, n)
        for i in range(k):
            if b == n-1: return True
            if b == 1: return True 
            b = b*b % n 
        return False 
    

# You do not have to modify this line
checkList = lambda ls : tuple(map(isPrime,ls))

import random

def millerrabtest(a, n):
    if a%n == 0: return True
    q = n - 1
    k = 0 
    while q % 2 == 0:
        q = q //2 
        k +=1
    b = pow(a, q, n)
    if b == 1: return True 
    for i in range(k):
        if b == n-1: return True
        b = b*b % n 
    return False 

