Premium RSA
======
* **350 points **
* **Category: Cryptography**
* **Problem statement:** _My RSA is the greatest. It's so strong, in fact, that I'll even give you d!_
* **Hint:** _You thought it'd be that simple?_

This was a terrific challenge about RSA Partial Key Recovery! (Something I didn't even know existed before) Thankfully we were given over half of the private key. If we were given a quarter of the key, we would have to implement the Coppersmith attack, in addition to this.
**Due to a lack of Latex, if notation is non-standard mathematics notation, it is Python notation**

We are given N, The last 2048 bits of d, e, and c, and asked to get the message!

Lets call the least significant 2048 bits of d we have `d0`

Solving this involved a lot of derivation and reading up on RSA Attacks, namely the following two documents:
* http://www.ijser.org/researchpaper/Attack_on_RSA_Cryptosystem.pdf
* http://honors.cs.umd.edu/reports/lowexprsa.pdf

The idea is that `ed - k(N-p-q+1) = 1` by definition. `[1]`

Note that `N-p-q+1 = φ(N)`

d must be less than φ(N), since `d = modInv(e,φ(N))`

Therefore `k < e` since `ed > kφ(N)`

Thus k is in `range(1,e)`!

But we don't have φ(N), we have N, so we will switch φ(N) with N in the `[1]`

Lets call this `d'` since its just an approximation.
`ed' - kN = 1`

Rearrange, and solve for `d'` as:

`d' = (kN + 1) // e`

The maximum error in d' is: `3 sqrt(nBitSize)` bits, where nBitSize is how many bits long the modulus is. See the links for a proof this maximum error.

That error is less than dBitSize/2, so we can just replace the least significant bits with `d0`
and get the plaintext!

But we need a way of testing k. One way to do it would be to try encrypting a known message with e and n, and decrypting it with the d were getting from that particular k.
The only issue is that modpows are slow, especially as the exponent d is growing, as is the case with increasing k.

We actually have a way to speed this up greatly!
Using `[1]` again,
```
ed - k(N-p-q+1) = 1
ed ≡ 1 mod k
ed -1 ≡ 0 mod k
```
Nearly all k will fail that criterion, making it perfect!
I'm then going to decrypt test messages, just to be absolutely sure.
Now we have e,d, and N! Just for completion, lets find p and q.
Rearranging `[1]`
`φ(N) = (ed - 1)//k`
```
φ(N) = (p-1)(q-1) = n - p - q + 1
p^2 - p^2 - N + N = 0
p^2 - p^2 - pq + N = 0
p^2 + (-p -q)p + N = 0
p^2 + (φ(N) -n -1) + N = 0
```
Solving this quadratic for variable p:
``` python
b = totientN - n - 1
discriminant = b*b - 4*n
#make sure discriminant is perfect square
root = self.floorSqrt(discriminant)
assert root*root == discriminant
p = (-b + root) // 2
q = n // p
```
Now raise the message to d, and we get our flag!

My code is in premiumRSA.py, the method halfdPartialKeyRecoveryAttack
comes from my RSA Solver, https://github.com/ValarDragon/CTF-Crypto/blob/master/RSA/RSATool.py

``` bash
$ python3 premiumRSA.py
easyctf{wow_i_pR0bABLY_5h0uldntA_l33k3d_d}
```
