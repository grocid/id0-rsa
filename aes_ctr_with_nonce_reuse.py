import string

c1 = '369f9e696bffa098d2bb383fb148bd90'
c2 = '23d7847f28e4b6cc86be386cb64ca281'

look_up = {}
alphabet = string.ascii_lowercase+' '

    
for char in alphabet:
    for schar in alphabet:
        xored = ord(char) ^ ord(schar)
        if xored in look_up: look_up[xored].append((char, schar))
        else: look_up[xored] = [(char, schar)]


for line in [look_up[int(c1[i:i+2], 16) ^ int(c2[i:i+2], 16)] for i in range(0, len(c1), 2)]:
    print line



