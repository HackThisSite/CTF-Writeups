a = open('file1').read()
b = open('file2').read()
c = ""
d = ""
for i in range(len(a)):
    if(a[i]!=b[i]):
        c += a[i]
        d += b[i]

print(c)
print(d)
