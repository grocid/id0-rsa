import hashlib, itertools, affine_cipher


ciphertext = 'JIPBUZZFJRAJKWMQI CIIFUZKWKN .WBUZAOMQI.A.ZSCWDNG,B.M,SAUPCEKRWQE,OSISB.CDTRH.RWKRDYASRBJ.PB.IBPJ JEW.KIEJB.YSN VAXBG,IFAE,RWFDIS.PG .IEPBAJO A.OPUBI.N.CNHOQETYDNB.UIIYKDUPCE FTRBERBICI C.PG .GIOJUZ,WNBJ.GNQEHFI..IP KRDY.IWDBUKRJEQE, DNCEPNVPKMCEPNVPUUFDOL .KD..NEU,ZZXBB.MQKRQ.UEM.QBAJMRGEEBF.I,PGDNUFAEE,N.KNAJAQ.YJRI.P O JRSKGNBECDWFCEEBCEJDTRO CJCEW.HIFJJ WY .WQJ  BAJO A.ZBJYPQCMAJAQ.YJRSKGNBECDWFCEEBCEJDTRO CJCEW.NSM.E,PBDIM.PG .P PRQMJ E.,KDN.DRCG,B.BIIWHIRUDIJ.A,JDDIBBJ.PG .BIPUUZU,QFQ.KNUZISRJKMIC .J,JDKRWQIB,QDIUNZBWKWFDIWDL.J,PGJ  BDIBBWWHI,.RWAJAQ.YJRUZ,WNBFFQ.S  BWCTF .ZQRCM.ZFUFAEELUZZFCJUZ,WNBJ.,KDN.DRCKM'

ciphertext = [ciphertext[i : i + 2] for i in range(0, len(ciphertext), 2)]

folded_priori_dist = {}
folded_look_up = []

for x, y in itertools.product(affine_cipher.priori_dist, repeat=2):
    folded_priori_dist[x+y] = affine_cipher.priori_dist[x] * affine_cipher.priori_dist[y]

for x, y in itertools.product(affine_cipher.look_up, repeat=2):
    folded_look_up.append(x+y)

a, b = affine_cipher.break_affine_cipher(folded_look_up, ciphertext, folded_priori_dist)
message = ''.join(affine_cipher.decrypt(ciphertext, a, b, folded_look_up))

print message
print hashlib.md5(message).hexdigest()