# This one is really basic


> Tags: crypto  
> Points: 300


## Challenge Description

> The answer to life, the universe, and everything.  


## Analysis
This challenge was really easy, it just required a smart brain.

I tried a few things before I got the flag, I tried to search for the keyword ‘dctf’ in the text but couldn’t find it. 

I also tried to decrypt all of the text and then I tried to search for ‘dctf’ and still I didn’t get anything useful.

I read the description of the challenge and I saw “The answer to life, the universe, and everything”. 

With a quick google search I got to know that the answer of life is 42.

So after a lot of thinking and a couple of challenges after I came back to it and I thought of trying to decrypt it 42 times with the same decryption method, and thankfully the first method that I tried worked, and the method was Base64.

I decrypted it by writing a python script:
```python
from base64 import b64decode

fp = open(r' C:\Users\hp\Desktop\ctf\cipher.txt')

res = fp.read()
for _ in range(42):
    res = b64decode(res)

print(res)
```
The flag: dctf{Th1s_l00ks_4_lot_sm4ll3r_th4n_1t_d1d}
