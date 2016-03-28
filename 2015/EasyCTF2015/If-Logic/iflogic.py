with open("if-logic.in", 'r') as fi:
    dump = fi.read()

numbers = map(int, dump.split(','))

result = ''
for item in numbers:
    if item in range(0, 51):
        result += "hi\n"
    elif item in range(51, 101):
        result += "hey\n"
    else:
        result += "hello\n"

with open("if-logic.out", 'w') as fo:
    fo.write(result)
