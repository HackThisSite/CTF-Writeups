## Poor RSA
* Cryptography
* 200 points

Problem text:
```
This time Fady decided to go for modern cryptography implementations, He is fascinated with choosing his own prime numbers, so he picked up RSA once more. Yet he was unlucky again!
```

Were given two files, flag.b64, and key.pub . As you might expect, the encrypted message is base 64'd in flag.b64, and the RSA public key is in key.pub .

To extract the information from key.pub, I used:
```
$ openssl rsa -pubin -noout -text < key.pub
Public-Key: (399 bit)
Modulus:
    52:a9:9e:24:9e:e7:cf:3c:0c:bf:96:3a:00:96:61:
    77:2b:c9:cd:f6:e1:e3:fb:fc:6e:44:a0:7a:5e:0f:
    89:44:57:a9:f8:1c:3a:e1:32:ac:56:83:d3:5b:28:
    ba:5c:32:42:43
Exponent: 65537 (0x10001)
```
Decoding that modulus, and putting it into factordb gives us our two primes. For my convenience in writing a script to solve the problem, I converted the b64 flag into hex. At this point, you can use the exact same script as CR3. Strangely, you get an odd length string, which thus throws an error and can't be hex decoded. I presume this is because there is a leading 0 that isn't getting stored, but I don't actually know.
Adding a leading 0 to the final hex string, results in a few unprintable bytes in the decoding, and then our flag!

Flag: ALEXCTF{SMALL_PRIMES_ARE_BAD}
