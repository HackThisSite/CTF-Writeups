with open("addition.in", 'r') as fi:
      dump = fi.read()
        lst = [int(item) for item in dump.split(',')]

with open("addition.out", 'w') as fo:
    fo.write(str(sum(lst)) + "\n")
