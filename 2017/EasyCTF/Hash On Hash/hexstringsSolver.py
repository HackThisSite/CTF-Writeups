import hashlib
a = open('hexstrings').read().splitlines()
md5s = {}
for i in range(256):
    md5s[hashlib.md5(chr(i).encode()).hexdigest()] = chr(i)
flag = ""
for line in a:
    flag += md5s[line]
print(flag)
