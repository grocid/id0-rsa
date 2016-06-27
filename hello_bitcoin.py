import hashlib, base58, libnum, ecdsa

privkey = 94176137926187438630526725483965175646602324181311814940191841477114099191175

sign_key = ecdsa.SigningKey.from_string(libnum.n2s(privkey), curve=ecdsa.SECP256k1)
pubkey = ('\04' + sign_key.verifying_key.to_string())

s = hashlib.sha256(pubkey).digest()
r = '\x00'+hashlib.new('ripemd160', s).digest()
c = hashlib.sha256(hashlib.sha256(r).digest()).digest()[:4]

print base58.b58encode(r+c)