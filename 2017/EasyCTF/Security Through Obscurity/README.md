Security Through Obscurity
======
* **150 points**
* **Category: Cryptography**
* **Problem statement:** _I've never seen such a cryptosystem before! It looks like a public key cryptosystem, though... Could you help me crack it?_
* **Hint:** _Maybe google would help._

I think this problem achieves the true definition of failed Security Through Obscurity! These files, except for my [solver](sageSolver.py), are all sage files.
Sage is an open source python-based alternative to Mathematica and Matlab.

Lets analyze the code in sage.py

``` python
def calc_root(num, mod, n):
    f = GF(mod)
    temp = f(num)
    return temp.nth_root(n)
```
Looking through the Sage documentation, we can see that
f becomes a finite field of order mod. Mod is actually a prime, being passed from `gen_v_list(primelist, p, secret)`.

temp.nth_root(n) is finding the nth root of temp in this finite field. This means that
``` python
pow(temp.nth_root(n),n) ≡ temp mod num
```

This means that we can quite easily brute force for SECRET, see [sageSecret](sageSecret.py) file.
We don't actually need to solve for SECRET however.

So now this tells us what
``` python
def gen_v_list(primelist, p, secret):
    a = []
    for prime in primelist:
        a.append(calc_root(prime, p, secret))
    return a
```
means. gen_v_list is the nth root of each prime in the finite field of size p.

``` python
primelist = [2,3,5,7,11,13,17,19,23,29,31,37,43,47,53,59]
message = REDACTED
chunks = []
for i in range(0,len(message),2):
    chunks += [message[i:i+2]]
```
This splits the message into 2 byte chunks

``` python
for chunk in chunks:
    binarized = bin(int(chunk.encode('hex'),16)).replace('0b','').zfill(16)[::-1] #lsb first
    enc = 1
    for bit in range(len(binarized)):
        enc *= vlist[bit]**int(binarized[bit])
    enc = enc%p
    print(enc)
```
This converts every chunk to hex, removes any `0b` in the hex, converts it to binary, pads the left with 0's until its 16 bits longs, and then reverses the string. The for loop is multiplying enc by that
index in vlist if binarized[i] is 1. If its 0, then do nothing to enc. Finally take enc modulo p.

Wait!!! Only 16 bits in a chunk?? That means theres only `2**16 = 65536` options, well within the brute force range!
 We can just do a reverse lookup on everything in the ciphertext!


Brute forcing all 16 bits of options, and doing reverse lookups on Ciphertext, gives us the flag:
``` bash
$ python3 sageSolver.py
flag{i_actu4lly_d0nt_know_th3_name_of_th15_crypt0sy5tem}
```

In discussion with Neptunia, the challenge creator, I found out this was actually an unintended solution,
 and this solution reduced the point value from 500 points (iirc),
 to this current 150.

The intended solution involved learning what cryptosystem this is through google, and from there figuring out its decrypt function.

A link for the cryptosystem given post-CTF on this cryptosystem is:
 https://www.di.ens.fr/~stern/data/St63.pdf
