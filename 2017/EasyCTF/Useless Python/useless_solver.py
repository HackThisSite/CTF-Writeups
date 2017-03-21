import binascii
a = open('useless.py').read()
b = str(binascii.unhexlify(a), 'utf-8')

for j in range(3):
    for i in range(256):
        b = b.replace('+chr(%s)'%i,chr(i))


print(b)
