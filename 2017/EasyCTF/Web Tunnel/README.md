Web Tunnel
======
* **260 points**
* **Category: Web**
* **Problem statement:** _I was just going to search some random cat videos on a Saturday morning when my friend came up to me and told me to reach the end of this tunnel. Can you do it for me?_
* **Hint:** _You should write a script for this. The tunnel goes on too deep for any normal human._

Your given a link, which has a tunnel of QR Codes.
I found this website https://zxing.org/
which allows you to decode QR codes, and even better you can do it through a URL!

It however can't decode all of them, and so breaks often. For the ones it breaks on, I manually uploaded it to
 https://online-barcode-reader.inliteresearch.com/
which decoded all of them without fail.
I had to do that about 15 times.

``` python
import requests
import re
import time

def decodeQR(extension):
    r = requests.get('https://zxing.org/w/decode?u=http%3A%2F%2Ftunnel.web.easyctf.com%2Fimages%2F'+extension+'.png')
    regex = re.compile("Raw text</td><td><pre>([a-zA-z0-9\{_\}]+)", re.IGNORECASE)
    return regex.findall(r.text)

#There are several breaks, use https://online-barcode-reader.inliteresearch.com/
# to handle those
curLink = 'DaicO7460493nYSuvLPW'

for i in range(1000):
    curLink = decodeQR(curLink)[0]
    print(curLink)
    time.sleep(.3)

```
If you run this, and solve the QR codes it breaks on with https://online-barcode-reader.inliteresearch.com/ ,
you eventually get
```
h3d0mOApnx3XoL9foSD7
easyctf{y0u_sh0uld_b3_t1r3d_tr4v3ll1ng_all_th1s_w4y
```
Add the close paren, and you have your flag!
