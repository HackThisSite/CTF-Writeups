with open("can-you-even.in", 'r') as fi:
    dump = fi.read()

numbers = map(int, dump.split(','))

even = [item for item in numbers if item % 2 == 0]

with open("can-you-even.out", 'w') as fo:
    fo.write(str(len(even)) + "\n")

