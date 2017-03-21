Hash On Hash
======
* **100 points**
* **Category: Cryptography**
* **Problem statement:** _There's a lot of hex strings here. Maybe they're hiding a message? hexstrings_
* **Hint:** _Thankfully you can solve this without even using a website_

The file hexstrings is a file with many lines of 32 chars of hex.
I ignored the hint, and put the first few into the online hash cracker [CrackStation](https://crackstation.net/)

From that you could see that they were all MD5 hashes of 1 letter!
Then it was easy,
I just wrote a script to make all the 256 1 character MD5's.
Then iterate line by line and replace the lines with character that md5's to it. Concatenate the characters, and print the corresponding characters.

```
$ python3 hexstringsSolver.py
Im far too lazy to put anything meaningful here. Instead, here's some information about what you just solved.
The MD5 algorithm is a widely used hash function producing a 128-bit hash value. Although MD5 was initially designed to be used as a cryptographic hash function, it has been found to suffer from extensive vulnerabilities. It can still be used as a checksum to verify data integrity, but only against unintentional corruption.
Like most hash functions, MD5 is neither encryption nor encoding. It can be cracked by brute-force attack and suffers from extensive vulnerabilities as detailed in the security section below.
MD5 was designed by Ronald Rivest in 1991 to replace an earlier hash function MD4.[3] The source code in RFC 1321 contains a "by attribution" RSA license. The abbreviation "MD" stands for "Message Digest."
The security of the MD5 has been severely compromised, with its weaknesses having been exploited in the field, most infamously by the Flame malware in 2012. The CMU Software Engineering Institute considers MD5 essentially "cryptographically broken and unsuitable for further use".[4]
easyctf{1_h0p3_y0u_d1dn7_d0_7h47_by_h4nd}
```

We learn a few facts about MD5 and get our flag!
