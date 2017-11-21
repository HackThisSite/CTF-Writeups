Sponge
======
![Sponge bob](http://www.kevblog.co.uk/blog/25/spongebob.png)
No not that kind of Sponge, a Cryptographic sponge!
### Crypto: 200 points ###
We are given a custom python hashing / sponge function, and we are told to find a string that collides with *'I love using sponges for crypto'*
**Disclaimer:** I did not solve this during the CTF, the challenge was explained to me by [gsilvis](https://github.com/gsilvis) (a bkp admin) but the solution is genius (Meet in the Middle Attack) and I suspect it will appear in other CTF's.
The code for the given hashing function is in hash.py!

----------
First looking at the hashing function, we see that:

 1. The input string is split into blocks of 10, and the final block is padded depending on its size.
 2. Each of these blocks is 'ingest'ed in order, which means that 6 null bytes are padded to it, and then it is XOR'd with the functions internal state. The state then equals the AES encryption of this XOR. Thus the internal state changes between ingests.
 3. The final ingest does the same, but with its padding.
 4. Then the state is 'squeezed', which means the output is the first 10 chars of the state, plus the first 10 chars of the AES of the state.

How do we solve this?
 -------------

Since we can't break AES, we need the state of our crafted input to be exactly equal to the state before the squeeze. Since our block is XOR'ing the internal state, we can control the first 10 bytes of the internal state before AES'ing in each block. (Except the final block)

Our original idea was to brute force for a valid byte sequence, which when AES'd, the last 6 bytes equal the last 6 bytes of one of the internal states before a round of ingesting. We can't do this in the final ingest, since it has more padding, so there are 3 possibilities for what this AES equals. We would be brute forcing for one of 3, 6 byte strings after AES'ng, we would have  
(256^6 )/3 AES attempts before we expect to get one match. This is approx 2^47 AES attempts, and we don't have the computation power to solve such a brute force. (We tried)

After the CTF, talking to gsilvis, I learned that the solution method is called a ["Meet in the Middle Attack"](https://en.wikipedia.org/wiki/Meet-in-the-middle_attack), and I will try to explain it here.

The general idea of a Meet in the Middle Attack, which works on repeated encryption, is that you search for a first and third block, such that encrypt(block1) = decrypt(block3).

In our case, since we can control the first 10 blocks with the XOR from block2, we only need the last 6 bytes of encrypt(block1) to equal decrypt(block3) to match.

In our case, block 1 would be 10 bytes long. Since the internal state during block 1 is all zeroes, XOR'ng the padded version of block 1 with the internal state gives block1 + '\x00'*6 .
Therefore encrypt block1 = aes.encrypt(block1 + '\x00'*6)

Decrypting block3 is a wee bit more complex.
Here we need to work backwards a bit. We want our solution to be 3 blocks long, so we need to work backwards from the output of the sponge.
Since our solution is 3 blocks long, final_ingest does an ingest of block "'\x80' + '\x00'*8 + '\x01'".
Let TARGET be the state of the Sponge algorithm, right before the squeezing, when its given the given string, "*I love using sponges for crypto*" .

    Then to undo the effects of final_ingest,
    TARGET = aes.decrypt(TARGET)
    To undo the XOR done in TARGET,  
    TARGET = TARGET ^ ('\x80' + '\x00'*8 + '\x01' + '\x00'*6)
The 6 null bytes come from the padding in ingest.
This means that TARGET is now what we want the state of ingest to be when it is ingesting block 3, right before the AES.
Since TARGET is XOR'd with padded block 3 during its ingestion, decrypt(block3) = aes.decrypt(TARGET ^ block3)

Lets relook at what exactly we are trying to achieve.
Were trying to find two blocks such that

    aes.encrypt(block1 ^ Initial State)[10:] = aes.decrypt(TARGET ^ Block 3)[10:]

[10:] in this context means last 6 bytes of.
aes.encrypt(block1 ^ initial state) is the state after ingesting the first byte.
We can manipulate the first 10 bytes to be whatever we want them to be through the XOR'ing of block 2 during its ingestion. So we make block 2 set the first 10 bytes to be whatever aes.decrypt(TARGET ^ Block 3)[10:] is.
Then when it is AES'd as part of block 2 ingestions, the State right before block 3's ingestion is
TARGET ^ Block 3!!!!
This is great, because in block 3 this is XOR'd so that now the state is the TARGET.  The Target is defined so that once we reach the target and carry on with processes (aes encrypting it, and then final ingesting it) we get the same result which the Given string "*I love using sponges for crypto*" gives us.
How much processing will this take?
-------------
Is this solution going to be any faster than the brute force we were using before? Well we are looking for *any* last 6 bytes to be the same between encrypt and decrypt for the different blocks, not just the 3 specific cases we were looking for in the brute force. This means that we have a birthday problem scenario. https://en.wikipedia.org/wiki/Birthday_attack

The mathematics of the Birthday Attack tells us that since we are looking for a collision of two 6 bytes to be the same, (with AES we are assuming any final 6 bytes are generated with uniform probability), that we will expect to get a collision after doing `1.25*(2^24)≈2^24` encryptions / decryptions! This is definitely doable!

I had already seen gsilvis's code for solving Sponge, and since I couldn't do it any better myself, I just marginally tweaked it before putting it in here. (I replaced the block generation with struct, added a few comments and made it less general-case) gsilvis gets all the credit for this! The modified file mod_gsilvis_sponge_solver. You can see gsilvis' original solver at: https://gist.github.com/gsilvis/64bbb435d3f90a6f208cceaddeaf1a95

I hope this helped! The meet in the middle attack is incredibly useful, as it reduced the computational complexity from 2^48 to 2^24 !

If you just curl the URL with the collision strings in hex, the site returns the flag: FLAG{MITM 3: This Time It's Personal!}
