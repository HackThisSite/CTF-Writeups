p = 196732205348849427366498732223276547339
secret = 4919
# Solved through brute force that secret = 4919, see sageSecret

def calc_root(num, mod, n):
    #Create a modular ring with mod as the modulus
    f = GF(mod)
    # temp = num mod Modulus
    temp = f(num)
    #Calculate the nth root temp on this modular field
    # AKA (returnValue)^n % mod = temp
    return temp.nth_root(n)

def gen_v_list(primelist, p, secret):
    a = []
    for prime in primelist:
        a.append(calc_root(prime, p, secret))
    # A is an array of the secreth root of each prime, mod p
    return a

def decodeInt(i, primelist):
    pl = sorted(primelist)[::-1]
    out = ''
    for j in pl:
        if i%j == 0:
            out += '1'
        else:
            out += '0'
    return out

def bin2asc(b):
    return hex(int(b,2)).replace('0x','').decode('hex')

primelist = [2,3,5,7,11,13,17,19,23,29,31,37,43,47,53,59]

#Split message into 2 char chunks
message = REDACTED
chunks = []
for i in range(0,len(message),2):
    chunks += [message[i:i+2]]

vlist = gen_v_list(primelist,p,secret)
print(vlist)
for chunk in chunks:
    # Encode the 2char chunk into hex
    # replace all 0b with null
    # make the thing 16 bits longs
    # reverse it
    binarized = bin(int(chunk.encode('hex'),16)).replace('0b','').zfill(16)[::-1] #lsb first
    enc = 1
    for bit in range(len(binarized)):
        enc *= vlist[bit]**int(binarized[bit])
    enc = enc%p
    print(enc)
