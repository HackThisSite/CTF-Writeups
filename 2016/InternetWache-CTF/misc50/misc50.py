import sys

a = sys.stdin.read().replace('\n', '').split()
for i in a:
    if len(i) == 3: # don't try to convert offsets:
        character = chr(int(i, 8)) # make the 3 digit octal string a decimal integer
        sys.stdout.write(character)
sys.stdout.write('\n')
