Description: Solved by 414 teams.
Our intelligence tells us that [this](https://www.easyctf.com/static/problems/hardwood/hardwood.py) function was used to encrypt a message. They also managed to capture a spy while in the field. Unfortunately, our interrogators only managed to find the [ciphertext](https://www.easyctf.com/static/problems/hardwood/floors.txt) of a message on his phone. Can you help us recover the secret message?

The function which was used to encrypt a message was:
```python
message = "<redacted>"
key = 3
encrypted = ' '.join([str(ord(c)//key) for c in message])
print(encrypted)
```

Ciphertext:
```27 39 33 34 10 36 32 33 35 10 37 34 10 38 35 34 37 38 15 15 15 10 33 32 38 40 33 38 34 41 34 36 16 16 38 31 33 16 39 35 38 35 16 36 41```

In the source code above, we can see that floor division was used during encryption of the message. Floor division means the value after '.' or decimal is truncated. For example, both 5.9999 and 5.0001 when floor divided by 3 result to 1.
From this, we can conclude that for each character there are three possible values.

A simple python script called [findvalues.py](./findvalues.py) to decipher the ciphertext and find out the possible values was written. The output with our guess on the right hand side:
`Output        Our guess`
```
Q | R | S       S 
u | v | w       u
c | d | e       c
f | g | h       h
 |  |  
l | m | n       l 
` | a | b       a 
c | d | e       c 
i | j | k       k 
 |  |  
o | p | q       o 
f | g | h       f 
 |  |  
r | s | t       r 
i | j | k       i
f | g | h       g
o | p | q       o
r | s | t       r
- | . | /       .
- | . | /       .
- | . | /       .
 |  |  
c | d | e       e
` | a | b       a
r | s | t       s
x | y | z       y
c | d | e       c
r | s | t       t
f | g | h       f
{ | | | }       {
f | g | h       f
l | m | n       l
0 | 1 | 2       0
0 | 1 | 2       0
r | s | t       r
] | ^ | _       _
c | d | e       d
0 | 1 | 2       1
u | v | w       v
i | j | k       i
r | s | t       s
i | j | k       i
0 | 1 | 2       0
l | m | n       n
{ | | | }       }
```
So, based on our guess, we got the message "Such lack of rigor... easyctf{fl00r_d1visi0n}"
From the message, we found the flag to be `easyctf{fl00r_d1visi0n}`
