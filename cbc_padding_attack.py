import thread, time, string, urllib2, copy

threads = 30
alphabet = ''.join([chr(i) for i in range(16)]) + string.printable
alphabet_blocks = [alphabet[i : i + threads] for i in range(0, len(alphabet), threads)]
ciphertext = 'c6574d8a54c952a7f298673ee7063c16ecf5f6d6405e2ad74254ff211635e390'


def oracle(payload):
    global responses
    try: response = urllib2.urlopen('http://id0-rsa.pub/problem/cbc_padding_oracle/' + payload)
    except urllib2.HTTPError, error: 
        responses[payload] = False
        return
    responses[payload] = True
    
def flip_cipher(ciphertext, known, i):
    modified_ciphertext = copy.copy(ciphertext)
    for j in range(1, i): modified_ciphertext[16-j] = ciphertext[16-j] ^ ord(known[-j]) ^ i
    return modified_ciphertext
    
ciphertext = [int(ciphertext[i:i+2], 16) for i in range(0, len(ciphertext), 2)]
count, known = 1, ''
while True:
    print [known]
    for block in alphabet_blocks:
        responses, payloads = {}, {}
        modified_ciphertext = flip_cipher(ciphertext, known, count)
        print modified_ciphertext
        for char in block:
            modified_ciphertext[16-count] = ciphertext[16-count] ^ ord(char) ^ count
            payloads[''.join([hex(symbol)[2:].zfill(2) for symbol in modified_ciphertext])] = char
        for payload in payloads.keys(): thread.start_new_thread(oracle, (payload,))
        while len(responses.keys()) != len(payloads): time.sleep(0.1)
        if True in responses.values(): 
            known = payloads[responses.keys()[responses.values().index(True)]] + known
            alphabet_blocks.remove(block)
            alphabet_blocks.insert(0, block)
            count = count + 1
            break