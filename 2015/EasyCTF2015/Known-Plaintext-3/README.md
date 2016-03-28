Description: Solved by 75 teams.
Solve the problem using the programming interface. The input file is `knownplaintext3.in`.

The input is formatted `[d/e] <string>`. The first character specifies whether the assignment is to encrypt or to decrypt, and the string is either the plaintext or the ciphertext, depending on the first letter.

Although it was a cryptography challenge, this had to be solved using [programming interface](https://www.easyctf.com/programming).

From various failed instances of the program run (later on used as [test cases](./testcases.txt)), we were able to find cipher used to encrypt and decrypt the text.

For encryption each letter in plaintext was translated using following mechanism:
```
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
C W K y g z G D O I V B L n Q q p m H t f J x Y o S h v M R E e F w d T N u A c i l a k Z U r X s b j P
```

For decryption each letter in ciphertext was translated using following mechanism: 
```
C W K y g z G D O I V B L n Q q p m H t f J x Y o S h v M R E e F w d T N u A c i l a k Z U r X s b j P
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z
```

A Python script called [kp3.py](./kp3.py) was written to solve the challenge.
Upon successful run, it gaves us the flag which was:
`easyctf{at_least_im_better_than_caesar}`
