def xor(data, key): 
    return bytearray(a^b for a, b in zip(*map(bytearray, [data, key]))) 

message = " $6<&1#><*\x1a!$2\x22\x1a,\x1a- $7!\x1a<*0\x1a),. !\x1a=*78"

key = "E"*38

print xor(message,key)
