Description: Although it was a cryptography challenge, this had to be solved using [programming interface](https://www.easyctf.com/programming).

From various failed instances of the program run (later on used as [test cases](./testcases.txt), we were able to find algorithms used to encrypt and decrypt the text.

Encryption part of this challenge was little tricky. The input read from `knownplaintext1.in'contained various special characters like `\n`, `\r`, `\\`, etc. which were escaped by Python when read and passed to encryption method producing incorrect result.

To solve this we had to produce a string that is equivalent to strings in Python source code, which can be done as:
`string.decode("string_escape")`.

Once we solved that, we began our analysis and discovered the encryption and decryption algorithms.

## Encryption algorithm
1. Given plaintext, find out character codes for each character of the plaintext.
2. Increment each character code by one.
3. Convert each incremented character code back to character and encode it to hex.
4. Create blocks of two bytes separated by spaces.
5. Replace '70', '60', '50', '40', '30' and 'a' with '6g', '5g', '4g', '3g', '2g' and ':' respectively.
6. Remove spaces and return the final string as ciphertext.

## Decryption algorithm
1. Given ciphertext, create blocks of two bytes separated by spaces.
2. Replace '6g', '5g', '4g', '3g', '2g' and ':' with '70', '60', '50', '40', '30' and  'a' respectively.
3. Except for spaces, decode each hexadecimal block to their equivalent characters.
4. Find out character codes for each character of the decoded string.
5. Decrement each character code by one.
6. Convert each decremented character code back to character.
7. Remove spaces and return the final string as plaintext.

A Python script called [kp1.py](./kp1.py) was written based on the derived algorithms to solve the challenge.
Upon successful run, it gave us the flag which was:
`easyctf{w0w_d4t_h3x_th0}`
