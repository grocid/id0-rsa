from sage.all import *
import urllib2

def ph_log(p, g, h):

    Zp = IntegerModRing(p)
    g = Zp(g)
    h = Zp(h)
    G, H, X, c = [],[],[],[]
    
    N = factor(p-1)
    
    for i in range(len(N)):
        G.append(g**((p-1) / (N[i][0]**N[i][1])))
        H.append(h**((p-1) / (N[i][0]**N[i][1])))
        X.append(log(H[i], G[i]))
        c.append((X[i], (N[i][0]**N[i][1])))
	
    while(len(c) > 1):
        a = c.pop()
        b = c.pop()
        r = crt(a[0], b[0], a[1], b[1])
        c.append((r, a[1] * b[1]))
	
    return c[0]

# public parameters
p = 0x0a38522d6c0b9a056801aa0cbe0329ce8457e9724acd1323f19ea310700d6e38e0252e2eb5b2ba4846259c99e0006441199cf10053471486058a4caa04156a504b
g = 0x2
c = int(urllib2.urlopen('http://id0-rsa.pub/problem/dh-oracle/' + str(g)).read(), 16)

result, _ = ph_log(p,g,c)
print result[-50:]