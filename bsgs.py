import math 

def bsgs(g,h,p):
    bslist = []
    gslist = []
    gs = findinverse(g,p)
    g2pow = 1
    gpow = 1
    N = math.ceil(math.sqrt(p-1))
    print(f"N is{N}")
    for i in range(N):
        bslist.append(gpow)
        gpow = (g*gpow) % p
        g2pow = (g2pow*gs) % p  #get inverse g to the Nth in the same loop 
    hgpow = h
    for i in range(N):
        gslist.append(hgpow)
        hgpow = (hgpow * g2pow) % p 
    i, j = collision(bslist, gslist)
    return i + j*N

def collision(bslist, gslist):
    lookup = dict()
    for i in range(len(bslist)):
        lookup[bslist[i]] = i
    for j in range(len(gslist)):
        if gslist[j] in lookup:
            i = lookup[gslist[j]]
            return i, j 

def findinverse(m, p):
    w, q, z = gcd(m,p)
    return q


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
