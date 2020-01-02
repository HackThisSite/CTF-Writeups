#### Challenge 4 (Crypto)

###### Details
- Difficulty: easy
- Section: crypto
- Creds: [Pyhscript (NETWORKsecurity)](https://github.com/pyhscript)

##### Description

We're given the following challenge description:

`When things are small you have to be carefull!`

and a file with the following contents:

```
message = int('REDACTED', base=35)
N = 31882864753733457706900355195561745936205728163688545344755624355885302677527509480805991969514641856022311950710014654686332759895303124949904557581766107448945073828773339824936328117599459705430379854436444155104737774883908742430619368768337640156577480749932446289330171110268995901030116001751822218657

c = message^3 % N
# c = 272712645051843502864020676686837219546440933810920336253597504130258033336636323130656292878088405243095416128

The message is the flag. No flag format.
```

#### Analysis

Analyzing the contents of the given file, one can easily see that this is a RSA challenge. Why:

##### Real quick intro to RSA, and why does it work

RSA is a cryptosystem which allows for **asymmetric encryption**. Asymmetric cryptosystems are commonly referred to as **Public Key Cryptography** where a `public key` is used to **encrypt** data and only a **secret**, `private key` can be used to decrypt the data.

If public `n`, public `e`, private `d` are all very **large** numbers and a message `m` holds **true** for `0 < m < n`, then we can say: `(m^e)^d ≡ m (mod n)`, where the triple equals sign in this case refers to [modular congruence](https://en.wikipedia.org/wiki/Modular_arithmetic), which is yet another fancy math word for "there **exists** an **integer** `k` such that `(m^e)^d = kn + m`".

RSA is viable because it is incredibly hard to find `d` even with `m`, `n`, and `e`, because factoring large numbers is an arduous process.

#### Approach and solution

There are few approaches you can take when trying to solve these kind of challenges. If you read the description of the challenge carefully, and you went through the RSA [Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) page, you can see that under the `Padding > Attacks against plain RSA` section, there is a descripton of an approach that kinda-sorta matches the description of the challenge, and it goes like:

> When encrypting with low encryption exponents (e.g., `e = 3`) and small values of the `m`, (i.e., `m < n^(1/e)`) the result of `m^e` is strictly **less** than the **modulus** `n`. In this case, ciphertexts can be easily decrypted by taking the **eth root** of the ciphertext over the integers.


What one can take from this is that, we already have `n` (which is the **product** of two large prime numbers `p` and `q`), the exponent `e` and the cipher text `c`.

```
c = 272712645051843502864020676686837219546440933810920336253597504130258033336636323130656292878088405243095416128
n = 31882864753733457706900355195561745936205728163688545344755624355885302677527509480805991969514641856022311950710014654686332759895303124949904557581766107448945073828773339824936328117599459705430379854436444155104737774883908742430619368768337640156577480749932446289330171110268995901030116001751822218657
e = 3
```

We can see that the exponent **is** a small number. So by just following the approach:

```
m = pow(c, (1/e))
```

we should get:


```
6.484877229948686e+36
```

**NOTE**: Be careful how you calculate your roots. I'd recommend using Wolframalpha.

By calculating it correctly, you should come up with a value of:

`value = 6484877229948717415163579969767084212`.

And now, as the challenge says, you would want to convert it to `base 35`. You can do it in multiple ways, but I found it easier just to use `gmpy2` library.

```
result = gmpy2.mpz(value).digits(35)
> juniorissmallkuchenblech
```

And there you have it. Enjoy. :)

#### References

- [ctf101.org - What is RSA](https://ctf101.org/cryptography/what-is-rsa/)
- [Wikipedia - RSA (cryptosystem)](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
