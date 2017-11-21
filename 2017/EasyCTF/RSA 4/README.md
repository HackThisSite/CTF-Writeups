RSA 4
======
* **200 points\***
* **Category: Cryptography**
* **Problem statement:** _Something to the extent of "After doing so much RSA, I finally messed up"_
* **Hint:** _Something to the extent of "Think about why this can't decrypt"_

\*Unfortunately due to a flag leak this challenge was taken down. It was a great challenge.

This was a really cool RSA problem, that I've never seen before!
We're given p,q,e and C, but e is equal to 100. e can't be this value! There is no modular inverse of e mod φ(N), since e is not coprime to φ(N).

`GCD(e,φ(N)) != 1`, instead it is 4. (Another way of saying the above)

In other words, it can't invert because there is no number x, such that
`ex mod φ(N) ≡ 1`
since if x is large enough, instead of looping back to the beginning of the modular ring, `ex` becomes 0.

But! If we divide the GCD from e, that number is invertible!
This will always exist, since GCD isn't 0, and because the modular inverse always exists if the number being inverted and the modulus are coprime.

So in our case ```e//GCD(e,φ(N)) = 25```
So now we raise c to the inverse of this!
Lets use the normal notation x^-1 = modInv(x,φ(N))
```
c ≡ m^100 mod N
c^(25^-1) ≡ m^(100*(25^-1))
c^(25^-1) ≡ m^(4*25*(25^-1))
```
Recall that by definition,
```
x*x^-1 ≡ 1 mod φ(N)
```
And recall that we only care about the exponent of m mod φ(N), because of Fermat's Little Theorem

so
```
c^(25^-1) ≡ m^(4*25*(25^-1))
c^(25^-1) ≡ m^(4*1)
c^(25^-1) ≡ m^4 mod N
```
So if we take the 4th root of c, we will get a few of the most significant bits of m! We don't get the whole thing because we don't have the exact value of C, only it modulo N.

```
∜c^(25^-1) ≡ m mod N
```

And that is how we get m! Coding this:

``` python

def invalidPubExponent(self,c,p="p",q="q",e="e"):

        if(p=="p"): p = self.p
        if(p=="q"): q = self.q
        totientN = (p-1)*(q-1)
        n = p*q
        if(e=="e"): e = self.e
        GCD = gcd(e,totientN)
        if(GCD == 1):
            return "[X] This method only applies for invalid Public Exponents."
        d = self.modinv(e//GCD,totientN)
        c = pow(c,d,n)
        import sympy
        plaintext = sympy.root(c,GCD)
return plaintext
```
I have coded this in https://github.com/ValarDragon/CTF-Crypto/blob/master/RSA/RSATool.py , and this is an excerpt from that, hence the self's.
Running this with our input gives:

``` bash
$ python3 RSA4.py
0x656173796374667b6d3064756c34725f66754e217d
bytearray(b'easyctf{m0dul4r_fuN!}')
```
