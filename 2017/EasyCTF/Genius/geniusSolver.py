import hashlib

def chunks(l, n):
    toReturn = []
    for i in range((len(l)//n)):
        toReturn.append(l[i*n:(i+1)*n])
    return toReturn


md5Sols = chunks("""8a7fca9234d2f19c8abfcd812971a26c8c510dcaefd5061b191ad41d8b57d0ce631f5074f94b32730d0c025f1d7aacd7
be1ab1632e4285edc3733b142935c60b90383bad42309f7f6850d2b4250a713d0b2d7a97350465a02554d29d92bfefaf
d64ddd0de1b187cd670783f5e28d681dd401ed3009d05ce4ef600d364a2c953e4cc801b880dddef59829a5ad08bd8a63
73d559bc117f816333174e918d0587de5cca214701dbe9f7f42da7bccf074b811292b9d4dc398866ef95869b22b3941e
78635bc95eaa7662a2ddf3e3d45cf1084f4233d6c396e8a0e6fbf597d07b88178d03f3f7757bdbdaaed60729d08bb180
b42dad5453b2128a32f6612b13ea5d9fef843bee79633652a6d6ae08e964609f00e883ab809346226dff6887080fb68b""".replace('\n',''),32)

plaintextSols = [1]*len(md5Sols)
startval = 48
endval = 123
a = startval
#made unpythonic with while loops for a big speedup
#with skipping irrelevant ranges
while(a < endval):
    if(a == 58):
        a = 65
    if(a == 91):
        a = 95
    i = startval
    while(i < endval):
        if(i == 58):
            i = 65
        if(i == 91):
            i = 95
        j = startval
        while(j < endval):
            if(j == 58):
                j = 65
            if(j == 91):
                j = 95
            b = "%s%s%s"%(chr(a),chr(i),chr(j))
            k = startval
            while(k < endval):
                if(k == 58):
                    k = 65
                if(k == 91):
                    k = 95
                md5 = hashlib.md5((b+chr(k)).encode()).hexdigest()
                if(md5 in md5Sols):
                    print(md5+"   "+b+chr(k))
                    plaintextSols[md5Sols.index(md5)]=b+chr(k)
                k+=1
            j+=1
        i+=1
    a+=1

print(''.join(plaintextSols))
