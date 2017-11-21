import base64

a = open('begin').read()
a = a.replace('\n','').replace('\\n','')
b64 = str(base64.standard_b64decode(a),'utf-8')

for i in range(19):
    a = b64
    b64 = str(base64.standard_b64decode(a),'utf-8')
print(b64)
