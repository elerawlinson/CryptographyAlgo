import math
def modpow(a,e,m):
    #negative case
    if e < 0: 
        r, u, v = gcd(a,m)
        a = u % m 
        e = abs(e)
    if e == 0:
        return 1 
    else: 
        f = e // 2 
        b = modpow(a,f,m) 
        if e % 2 == 0: 
            return b*b%m
        else: 
            return a*b*b%m
        
#Helper Functions for negative case 
def bezout(a,b):
    g, u, v = gcd(a,b)
    return g,u,v


def gcd(a, b):
    rprev = a
    rcurr = b
    uprev = 1
    vprev = 0
    ucurr = 0
    vcurr = 1
    counter = 0
    while rcurr != 0:
        unext = uprev - (rprev//rcurr)*ucurr
        vnext = vprev - (rprev//rcurr)*vcurr
        uprev = ucurr
        vprev = vcurr
        ucurr = unext 
        vcurr = vnext 
        rnext = rprev % rcurr
        rprev = rcurr 
        rcurr = rnext 
    return rprev, uprev, vprev 
