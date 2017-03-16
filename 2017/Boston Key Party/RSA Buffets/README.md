RSA Buffet and RSA Extended Buffet
======
##### RSA Buffet
* **150 points **
* **Problem statement:** _Crack 3 of the given RSA keys, and get the secret_

##### RSA Extended Buffet
* **200 points **
* **Problem statement:** _Crack 5 of the given RSA keys, and get the secret_

Since the fileset for both of these challenges is the same, I'm putting them in the same writeup!

We're given 10 RSA Public Keys, 5 Ciphertexts, and the method use to generate the ciphertexts from the plaintext.

### Cracking the RSA Keys
_The log for Factorizer.py trying to crack the keys can be found in Factorization Log.txt . To run this process, do `python3 solver.py`. solver.py loads the Public keys and passes them to Factorizer._

The first step to this challenge is to crack these RSA public keys, but thats _much_ easier said then done. I made a script _Factorizer.py_ which is what I used to factor the 5 modulii. I drew inspiration from https://github.com/sourcekris/RsaCtfTool and even used @sourcekris 's code for the Wiener Attack.

First step: Check [factorDB](http://factordb.com/) on every modulus! FactorDB factors public key-2 for us.

Then before trying to crack anything, I decided to look if any of these modulii shared a factor, since there were 10 given, and we only needed to solve 5. Indeed key-0 and key-6 shared a common factor! key-6's private key however did not decrypt any ciphertext, so its just an extra key. Still we have 2 keys solved!

Now its time to actually look in detail at the keys and modulii involved. One file stands out from the others, key-3 is almost double the size of all the other public keys!

Using ` openssl rsa -inform PEM -pubin -in key-3.pem -text` we can see that the length of key-3's public exponent is almost as long as the modulus! In base 10, they are both 1233 digits long! The rest of the keys public exponents are 5 decimal digits long, with similarly large modulii. This means that key-3's private exponent must be small, therefore it is susceptible to Wieners attack!

To solve the remaining two keys, you have to try different attacks. One attack needed for this ctf was the Fermat Attack, which runs extremely quickly and essentially breaks keys when the factors are really close to each other / near the square root of the modulus. This cracked Key-1.

The final attack was Pollards P-1 Smooth attack. Essentially this attack breaks modulii where its factors - 1 (The p-1) are products of many small primes. This attack takes the longest of the mentioned attacks, and is used to crack key-5

The code used for all of these RSA attacks is in Factorizer.py, and wienerAttack.py. The explanation I used for all of these algorithms is linked in the code, except for the Wiener Attack. We can reuse this script in future CTF's!

This was by far the hardest part of the challenge, and the most time-consuming. To summarize the methods used:
* key-0.pem - GCD with key-6
* key-1.pem - Fermat Factorization Attack
* key-2.pem - factorDB
* key-3.pem - Wiener Attack
* key-5.pem - Pollard P-1 Smooth Factorization Attack



### Decoding the Ciphertexts

The hardwork is done, now we just have to decode the ciphertexts with the private keys. The Boston Key Party team gave us an easy way of decoding the ciphertexts themselves, we just have to use their method.

Unfortunately they're script runs off of python2, not python3, so I made a second script _decoder.py_ to solve this part, instead of _solver.py_

Here is the plaintext of ciphertext-3.bin:

>Congratulations, you decrypted a ciphertext!  One down, two to go :)
>3-17e568ddc3ed3e6fe330ca47a2b27a2707edd0e0839df59fe9114fe6c08c6fc1ac1c3c8d9ab3cf7860dac103dff464d4c215e197b54f0cb46993912c3d0220a3eb1b80adf33ee2cc59b0372c
>3-b69efb4f9c5205175a4c9afb9d3c7bef728d9fb6c9cc1241411b31d4bd18744660391a330cefa8a86af8d2b80c881cfa
>3-572e70c5acfbe8b4c2cbd47217477d217da88c256ff2586af6a18391972c258bbea6143e7cd2ff6d39393efeb64d51d9318a2c337e50e2d764a42173bc3a1d5c7c8f24b64043daf5d2a8e9f4
>3-e9e6850880eb0a44d36fe9f2e5a458c6da3977b7fcd285afa27e9bfc116b1408570991504116b81864b03a7060bfd5d3fb6e007bb346f276d749befd545d1489c4

Each of these lines is a secret sharing secret, so the secret sharing secrets from each ciphertext needs to be combined to get the flag. BKP gives us the [github repo link](https://github.com/blockstack/secret-sharing) and pip command to install secretsharing: `pip install secretsharing`
Combining these shares to get the flag is easy, its on the front page's readme that we have to do:

````
from secretsharing import PlaintextToHexSecretSharer
PlaintextToHexSecretSharer.recover_secret(shares[0:2])
````

So now if we just brute force every combination of 3 shares and 5 shares using secretsharing, we get the flag! Running the script we get our flags as:
* Three's the magic number!  FLAG{ndQzjRpnSP60NgWET6jX}
* FIVE OUT OF FIVE.  Nice work!  FLAG{KGZSMbd2c9oEtHZ7aXK4}

This was a great challenge for building an RSA cracking tool! Now we can use/improve this factorization tool in many CTF's to come! I highly encourage you to read how these factoring algorithms work, they're quite clever and interesting!
