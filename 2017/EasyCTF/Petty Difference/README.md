Petty Difference
======
* **75 points **
* **Category: Forensics**
* **Problem statement:** _I found two files in a secret room. They look like jumbled letters with no patterns. I mean look at it! file1 is identical to file2, right?_
* **Hint:** _No hint_

Since it mentions the files being identical, lets look at the differing bytes!

``` python
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
```

which gives the flag
``` bash
$ python3 solve.py
easyctf{th1s_m4y_b3_th3_d1ff3r3nc3_y0u_w3r3_l00k1ng_4}
lfbz95eobcrtqadt7kdxz0dcisw{x5kik4pueriiebmavwnxdvwex9
```
