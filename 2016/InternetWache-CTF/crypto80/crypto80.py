import sys

a = sys.stdin.read().strip().split()
for i in a:
    character = chr(int(i, 8))
    sys.stdout.write(character)

sys.stdout.write('\n')
