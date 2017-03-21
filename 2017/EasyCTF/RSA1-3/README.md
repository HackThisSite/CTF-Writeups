RSA 1 - RSA 3
======
##### RSA 1
* **50 points **
* **Problem statement:** _I found somebody's notes on their private RSA! Help me crack this._
* **Problem hint:** _Go google RSA if you're stuck._

##### RSA 2
* **80 points **
* **Problem statement:** _Some more RSA! This time, there's no P and Q..._
* **Problem hint:** _It's like RSA 1 but harder. Have fun!_

##### RSA 3
* **135 points **
* **Problem statement:** _We came across another message that follows the same cryptographic schema as those other RSA messages. Take a look and see if you can crack it._
* **Problem hint:** _You might want to read up on how RSA works._

These were extremely easy RSA problems! Using the solver I created for the Boston Key Party, I got all the solutions.
(https://github.com/HackThisCode/CTF-Writeups/tree/master/2017/Boston%20Key%20Party/RSA%20Buffets)

RSA 1 gave you p and q, thus it simply tested if you knew how RSA worked.

RSA 2 was a small modulus problem, so I let factordb do the hardwork.

RSA 3 was a twin primes problem, so it was solved in the first iteration of the Fermat Factorization of Factorizer.py

Here is the output of the program:
```
RSA1
bytearray(b'easyctf{wh3n_y0u_h4ve_p&q_RSA_iz_ez_8b1f4c9a}')
RSA2
[*] Checking Factor DB...
[*] Factors are: 513910465601463936991 and 514967492450613671867
Wrote private key to file privkey-2.pem
bytearray(b'flag{l0w_n_bfca}')
RSA3
[*] Checking Factor DB...
[x] Factor DB did not have the modulus
[*] Trying Wiener Attack...
[x] Wiener Attack Failed
[*] Trying Fermat Attack...
[*] Fermat Attack Successful!!
[*] Factors are: 3423616853305296708261404925903697485956036650315221001507285374258954087994492532947084586412780871 and 3423616853305296708261404925903697485956036650315221001507285374258954087994492532947084586412780869
Wrote private key to file privkey-3.pem
bytearray(b'easyctf{tw0_v3ry_merrry_tw1n_pr1m35!!_417c0d}')
```
And thats it! Pretty easy 265 points.
