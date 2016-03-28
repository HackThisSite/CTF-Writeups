# The hidden message
>Description: My friend really can't remember passwords. So he uses some kind of obfuscation. Can you restore the plaintext?

>Attachment: misc50.zip


## Solution
The single file provided by the challenge is 'README.txt':
```
0000000 126 062 126 163 142 103 102 153 142 062 065 154 111 121 157 113
0000020 122 155 170 150 132 172 157 147 123 126 144 067 124 152 102 146
0000040 115 107 065 154 130 062 116 150 142 154 071 172 144 104 102 167
0000060 130 063 153 167 144 130 060 113 012
0000071
```
This is an octal dump of a text file. So we rebuild it with:
```python
import sys

a = sys.stdin.read().replace('\n', '').split()
for i in a:
    if len(i) == 3: # don't try to convert offsets!
        character = chr(int(i, 8)) # make the 3 digit octal string a decimal integer
        sys.stdout.write(character)
sys.stdout.write('\n')
```

Reconstructing the file yields:
`V2VsbCBkb25lIQoKRmxhZzogSVd7TjBfMG5lX2Nhbl9zdDBwX3kwdX0K`

Which is valid base64 and decodes to the flag: `IW{N0_0ne_can_st0p_y0u}`
