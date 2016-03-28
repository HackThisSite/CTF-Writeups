Description: Solved by 172 teams.
How good are you at reading Python? Put your Python skills to the test by finding the password that passes this check: [obfuscated.py](https://www.easyctf.com/static/problems/obfuscated/obfuscated.py)

Note: `easyctf{}` formatting is not required for this problem.

This challenge may look scary but with patience and knowledge of Python, it can be solved.
The way we derived flag is mentioned in a Python file called [obfuscated-sol.py](./obfuscated-sol.py).

This challenge can have multiple flags as long as it satifies the Python script [obfuscated.py](./obfuscated.py)

One of the flag we tested was:
`Wh4teaeReTH0O0O0O0OS3XFXF`

Here's how we derived it (keep [obfuscated-sol.py](./obfuscated-sol.py) and this side-by-side for easy understanding :)):

We supposed that s = "abcdefghijklmnopqrstuvwxy"

Let `sp` be a string that is derived by popping items from `s`. `sp` can have
variable length.

How `sp` changes
```
   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
1. a b c d e f g h i j k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  len(s) = 25
2. a b d e f g h i j k m  o  q  s  t  v  w  x  y                    len(s) = 19
3. a b d f g h j k m o q  s  t  v  w  x  y                          len(s) = 17
4. a b d f g h j k m o q  s  t                                      len(s) = 13
5. a b d f g h j k m o q  s                                         len(s) = 12
```

1. After popping itemsj from locations `[20, 17, 15, 13, 11, 2]` from original string `s`
2. After popping items from locations `[3, 7]` of `sp`
3. After popping four items from new `sp`
4. After popping an item from new `sp`
5. Resulting `sp`

Retrieving flag `s` based on what we know
```
   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
1. a b 4 d e f g h i j k  0  m  0  o  0  q  0  s  t  3  v  w  x  y  
2. a h 4 d e f g h e j k  0  m  0  o  0  q  0  s  t  3  v  w  x  y
3. a h 4 d e f g h e j k  0  m  0  o  0  q  0  s  t  3  X  F  X  F
4. a h 4 d e f g h e j k  0  m  0  o  0  q  0  s  S  3  X  F  X  F
5. W h 4 t e a e R e T H  0  O  0  O  0  O  0  O  S  3  X  F  X  F 
```

1. Substituting the characters `400003` into their respective character positions as derived from our analysis of second `if` statement 
2. Since 4th and 8th characters are same in the `sp`, we replace `i` (8th character of `sp`) with `e`. We also know that `h` lies in the 2nd place in the original string. Now making changes to s using `sp` we get the result on 2.
3. We know that `u` and `v` contain the item popped from `sp` (when `len(sp)` = 19).  We also know that
   `u = [sp[len(sp) - 1], sp[len(s) - 3]]` and
   `v = [sp[len(sp) - 2], sp[len(s) - 4]]`
   We have supposed that `u` and `v` both contain same characters in them too.  Since `u[0] ^ v[0] == 30`, we chose 'X' for `u` and 'F' for `v` So, we have
   `u = ['X', 'X']`, `v = ['Y', 'Y']`

   We now make changes to the original string `s` using `sp`
4. We know that last item for sp when `len(sp)` = 13 has character 'S', so we make changes to the original string `s`.
5. We have to fit 'WRTHOOOO' and 'hate' within `sp` for `len(sp)` = 12. For latter string, 'e' at 5th place will already be popped off, so we have to be careful while making changes. Also the order should be 'htae' so that when statement `i[1:3] = i[2:0:-1]` runs, we have "hate" stored in `i`.
   By making appropriate changes, we get the flag.

Flag: `Wh4teaeReTH0O0O0O0OS3XFXF`
