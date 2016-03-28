import re

alpat = re.compile(r'[0-9]+')


with open("looking-for-letters.in", 'r') as fi:
    dump = fi.read()

result = re.sub(alpat, '', dump)

with open("looking-for-letters.out", 'w') as fo:
    fo.write(result)

