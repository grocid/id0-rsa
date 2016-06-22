import urllib2

def oracle(payload):
    response = urllib2.urlopen('https://id0-rsa.pub/problem/rsa_oracle/' + payload)
    return int(response.read(), 16)

N = 21417796527836084184909381847347996579544574856536138887095572895605838936183797133497945149041143747935697840040038878051837066916098917830507702189036474052559440023560073044871506915412125924451079846179181310933243078160174081203833277764294560781167257508183474040791469949490073063621508350223394644084480243319785802072416191661242887403456436340352491914665462451622845195529700750590231557792010569404312659993869936897967297972271825868537334316050945924043213637990528504616783764719232801862604492419501841834817152625201356251989468366357139655821655574801663780279380761798039447128430604777726363650041

ciphertext = 0x912fcd40a901aa4b7b60ec37ce6231bb87783b0bf36f824e51fe77e9580ce1adb5cf894410ff87684969795525a63e069ee962182f3ff876904193e5eb2f34b20cfa37ec7ae0e9391bec3e5aa657246bd80276c373798885e5a986649d27b9e04f1adf8e6218f3c805c341cb38092ab771677221f40b72b19c75ad312b6b95eafe2b2a30efe49eb0a5b19a75d0b31849535b717c41748a6edd921142cfa7efe692c9a776bb4ece811afbd5a1bbd82251b76e76088d91ed78bf328c6b608bbfd8cf1bdf388d4dfa4d4e034a54677a16e16521f7d0213a3500e91d6ad4ac294c7a01995e1128a5ac68bfc26304e13c60a6622c1bb6b54b57c8dcfa7651b81576fc

# divisible by 2
ciphertext1 = ciphertext / 2
ciphertext2 = 0x2L

message = oracle(hex(ciphertext1)[2:-1]) * oracle(hex(ciphertext2)[2:-1])
print hex(message % N)[2:-1]