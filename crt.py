def crtList(ls):
    curr = crt(ls[0][0], ls[0][1], ls[1][0], ls[1][1])

    for i in range (2,len(ls)):
     #   print(f"inputing:#{curr[0]}, #{curr[1]}, #{ls[i][0]}, #{ls[i][1]} ")
        curr = crt(curr[0], curr[1], ls[i][0], ls[i][1])
        
    return curr


def crt(a1,m1,a2,m2):
    #solving x congr a1 mod m1 and x congr a2 mod m2 
    #re-write first eq as x = a1 + m1*k and 
    #set x's equal=- so a1 +m1*k = m2, solve for m1 alone
    #find inverse for multiple of y using eea 
    #multiply by inverse to get y alone and plug back into solve for x 
    m1inv = findinverse(m1, m2)
    y = ((a2-a1)*m1inv) % m2
    a = (a1 + y*m1) 
    return (a, m1*m2)


#find the inverse
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
