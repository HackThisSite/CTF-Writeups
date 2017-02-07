import binascii
import math

p = 863653476616376575308866344984576466644942572246900013156919
q = 965445304326998194798282228842484732438457170595999523426901

e = 65537
b64 = "362e39887e149d74adb4db9fd0ecbcd3e1b927bb66f2c049b8334deea7d321d10a268c38b2217672949b3ffa885838d28bec"
c = int(b64,16)
n = p*q
totn = (p-1)*(q-1)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

d = modinv(e,totn)
c = pow(c,d,n)
c = "0"+hex(c)[2:]
print(binascii.unhexlify(c))
