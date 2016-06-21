import string, libnum.modular, numpy, hashlib
import matplotlib.pyplot as plt

look_up = string.ascii_uppercase+' ,.'

ciphertext = 'ZNKIGKYGXIOVNKXOYGXKGRREURJIOVNKXCNOINOYXKGRRECKGQOSTUZYAXKNUCURJHKIGAYKOSZUURGFEZURUUQGZZNKCOQOVGMKGZZNKSUSKTZHAZOLOMAXKOZYMUZZUHKGZRKGYZROQKLOLZEEKGXYURJUXCNGZKBKXBGPJADLIVBAYKZNUYKRGYZZKTINGXGIZKXYGYZNKYURAZOUT'
priori_dist = {' ': 0.05985783763561542, ',': 0.0037411148522259637, '.': 0.0028058361391694723, 'A': 0.0764122708567153, 'C': 0.02600074822297044, 'B': 0.012065095398428732, 'E': 0.11878039655817432, 'D': 0.03974934530490086, 'G': 0.018892630003741116, 'F': 0.020856715301159744, 'I': 0.0651889263000374, 'H': 0.05695847362514029, 'K': 0.00720164609053498, 'J': 0.0014029180695847362, 'M': 0.02254021698466143, 'L': 0.03769173213617658, 'O': 0.07023943135054246, 'N': 0.06313131313131314, 'Q': 0.0009352787130564909, 'P': 0.01805087916199027, 'S': 0.05920314253647587, 'R': 0.0560231949120838, 'U': 0.025813692480359144, 'T': 0.08473625140291807, 'W': 0.022072577628133184, 'V': 0.00916573138795361, 'Y': 0.01842499064721287, 'X': 0.0014029180695847362, 'Z': 0.0006546950991395436}
dist = {}

def decrypt(ciphertext, a, b, look_up):
    ainv = libnum.modular.invmod(a, len(look_up))
    return [look_up[(look_up.index(cipherbit) - b) * ainv % len(look_up)] for cipherbit in ciphertext]

def break_affine_cipher(look_up, ciphertext, priori_dist):
    N = len(look_up)
    n = len(ciphertext)

    # compute distribution
    for ciphersymbol in ciphertext:
        if ciphersymbol in dist:
            dist[ciphersymbol] += 1.0 / n
        else:
            dist[ciphersymbol] = 1.0 / n

    X, Y = numpy.zeros((N, N)), numpy.zeros((N, N))

    # compute first matrix
    for i in range(1, N):
        for element in priori_dist:
            X[i, (look_up.index(element) * i) % N] = priori_dist[element]

    # compute second matrix
    for i in range(N):
        for element in dist:
            Y[(look_up.index(element) - i) % N, i] = dist[element]

    Z = numpy.dot(X, Y)
    a, b = numpy.unravel_index(Z.argmax(), Z.shape)
    return a, b

if __name__ == "__main__":
    a, b = break_affine_cipher(look_up, ciphertext, priori_dist)
    print a,b
    message = ''.join(decrypt(ciphertext, a, b, look_up))
    print message
    print hashlib.md5(message).hexdigest()