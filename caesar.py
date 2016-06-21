import string, affine_cipher

look_up = string.ascii_uppercase

ciphertext = 'ZNKIGKYGXIOVNKXOYGXKGRREURJIOVNKXCNOINOYXKGRRECKGQOSTUZYAXKNUCURJHKIGAYKOSZUURGFEZURUUQGZZNKCOQOVGMKGZZNKSUSKTZHAZOLOMAXKOZYMUZZUHKGZRKGYZROQKLOLZEEKGXYURJUXCNGZKBKXBGPJADLIVBAYKZNUYKRGYZZKTINGXGIZKXYGYZNKYURAZOUT'

a, b = affine_cipher.break_affine_cipher(affine_cipher.look_up, ciphertext, affine_cipher.priori_dist)
assert( a == 1 ) # caesar is a subset of affine cipher with a = 1

message = ''.join(affine_cipher.decrypt(ciphertext, a, b, look_up))
print message