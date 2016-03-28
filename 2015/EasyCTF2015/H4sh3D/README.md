Description:
Solved by 121 teams.

We discovered that Varsos's server uses a fairly insecure hash function to check passwords. The hashed password is c9b5af9864efa933, and the hashing function can be found here.


The hashing script is provided in this folder as `hash1.py`



The plain text string is being hashed into a 32 byte string, and then the script takes the 8 4-byte substrings, and maps each substring into an individual byte.
To break the encryption we can start with a random 31 byte input, and hash it. For every byte of output that is wrong, modify the corresponding 4-byte substring in the plain text, and repeat until the hash is the expected value. This encryption was so bad that it was possible to hand brute-force it within minutes, which is what I did, and came out with the following solution:
`iiii99hh55ddoocchhcc44ll//GG9ab03`
