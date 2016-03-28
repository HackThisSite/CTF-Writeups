import sys

with open("math-class.in", 'r') as fi:
    dump = fi.read()

splt = inp.split()

if splt[0] == "add":
      result = int(splt[1]) + int(splt[2])
else:
      result = int(splt[1]) - int(splt[2])

with open("math-class.out", 'w') as fo:
    fo.write(str(result) + "\n")

