Decode me
======
* **100 points **
* **Category: Cryptography**
* **Problem statement:** _Someone I met today told me that they had a perfect encryption method. To prove that there is no such thing, I want you to decrypt this encrypted flag he gave me._
* **Hint:** _Simple decoding :)_

The input file ends in the iconic `=` sign, hinting at base64.
And it b64 decodes, into another base64 string. So I wrote a short python3 script to perform repeated base64 decryption

``` python
import base64

a = open('begin').read()
a = a.replace('\n','').replace('\\n','')
b64 = str(base64.standard_b64decode(a),'utf-8')

while 'easyctf' not in b64:
    b64 = str(base64.standard_b64decode(b64),'utf-8')
print(b64)
```

which gives the flag
``` bash
$ python3 solve.py
easyctf{what_1s_l0v3_bby_don7_hurt_m3}
```
