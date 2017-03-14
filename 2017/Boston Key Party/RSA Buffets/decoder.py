from Crypto.PublicKey import RSA
import given.encrypt as encrypt
from secretsharing import PlaintextToHexSecretSharer

plaintexts = []
for i in range(5):
    if(i==4):
        i=5
    for j in range(1,6):
        plaintext = encrypt.decrypt(RSA.importKey(open('privkeys/privkey-%s.pem' % i).read()), open('given/ciphertext-%s.bin' % j).read())
        if(plaintext != None):
            plaintexts.append(plaintext)
            print(plaintext)

shares = []
for secretCollection in plaintexts:
    secrets = secretCollection.splitlines()[1:]
    for secret in secrets:
        shares.append(secret)

for i in shares:
    for j in shares:
        if(j==i):
            continue
        for k in shares:
            if(k==i or k==j):
                continue
            try:
                flag = PlaintextToHexSecretSharer.recover_secret([i,j,k])
                if('flag' in flag.lower()):
                    print(flag)
            except:
                pass
            for l in shares:
                if(l==i or l==j or l == k):
                    continue
                for m in shares:
                    if(m==i or m==j or m == k or m==l):
                        continue
                try:
                    flag = PlaintextToHexSecretSharer.recover_secret([i,j,k,l,m])
                    if('flag' in flag.lower()):
                        if('ndQzjRpnSP60NgWET6jX' not in flag):
                            print(flag)
                except:
                    pass
