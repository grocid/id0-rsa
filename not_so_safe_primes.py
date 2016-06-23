def pohligHellmanPGH(p,g,h):
    F = IntegerModRing(p)
    g = F(g)
    h = F(h)
    G,H,X,c = [],[],[],[]
    N = factor(p-1)
    
    for i in range(0,len(N)):
        G.append(g**((p-1)/(N[i][0]**N[i][1])))
        H.append(h**((p-1)/(N[i][0]**N[i][1])))
        X.append(log(H[i],G[i]))
        c.append((X[i],(N[i][0]**N[i][1])))

	c.reverse()
	
    for i in range(len(c)):
        if len(c) < 2:
            break
        t1=c.pop()
        t2=c.pop()
        r=crt(t1[0],t2[0],t1[1],t2[1])
        m=t1[1]*t2[1]
        c.append((r,m))
	
	print "(x,p-1) =",c[0]


p = 0x0a38522d6c0b9a056801aa0cbe0329ce8457e9724acd1323f19ea310700d6e38e0252e2eb5b2ba4846259c99e0006441199cf10053471486058a4caa04156a504b
g = 0x2
c = int('2068bf07530bf3a6d656d6907e1926505061a209dbac90b3bff8f8cfadf67a4f8e7bb0102144069569cd2fda30ce42f156e563359c6b58c043d141c5668c135ce', 16) # g^secret -- we get this by sending 2 to the oracle

print pohligHellmanPGH(p,g,c)



print str(105441826375770618487901115818858345303623192029412552310756690653339227518434872617163437500938488280393929884789976048752445863186811184117469652522802215)[-50:]