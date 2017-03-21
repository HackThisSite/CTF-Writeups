from Crypto.PublicKey import RSA
import Factorizer
import os

def RSA3():
    fact = Factorizer.Factorizer()
    N = int("0x27335d21ca51432fa000ddf9e81f630314a0ef2e35d81a839584c5a7356b94934630ebfc2ef9c55b111e8c373f2db66ca3be0c0818b1d4eda7d53c1bd0067f66a12897099b5e322d85a8da45b72b828813af23",0)
    e = int("0x10001",0)
    c = int("0x9b9c138e0d473b6e6cf44acfa3becb358b91d0ba9bfb37bf11effcebf9e0fe4a86439e8217819c273ea5c1c5acfd70147533aa550aa70f2e07cc98be1a1b0ea36c0738d1c994c50b1bd633e3873fc0cb377e7",0)

    pubKey = RSA.construct((N,e))

    fact.factorModulus(pubKey,outFileName='privkey-3.pem')
    key = RSA.importKey(open('privkey-3.pem').read())
    message = pow(c,key.d,N)
    plaintext = str(bytearray.fromhex(hex(message)[2:]))
    print(plaintext)

def RSA1():
    p = 33132682577565126969140002129633649554751216806378793848788711477877065876428791
    q = 30499295022924348240291300676281238378975669046700846004703307670180486189350193
    e = 65537
    c = 660474724815540720613531868092397691552741064511546824568120281740415543775213104869225380836741678627218552010355976744867444511891060921755575057758398772339
    d = modinv(e,(p-1)*(q-1))
    message = pow(c,d,p*q)
    plaintext = str(bytearray.fromhex(hex(message)[2:]))
    print(plaintext)


def RSA2():
    fact = Factorizer.Factorizer()
    N = 264647183814913237076256557870096437332197
    e = 65537
    c = 116398201525894981634448031206761899942677

    pubKey = RSA.construct((N,e))

    fact.factorModulus(pubKey,outFileName='privkey-2.pem')
    key = RSA.importKey(open('privkey-2.pem').read())
    message = pow(c,key.d,N)
    plaintext = str(bytearray.fromhex(hex(message)[2:]))
    print(plaintext)


def extended_gcd(aa, bb):
    """Extended Euclidean Algorithm,
    from https://rosettacode.org/wiki/Modular_inverse#Python
    """
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
    """Modular Multiplicative Inverse,
    from https://rosettacode.org/wiki/Modular_inverse#Python
    """
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m
print("RSA1")
RSA1()
print("RSA2")
RSA2()
print("RSA3")
RSA3()
