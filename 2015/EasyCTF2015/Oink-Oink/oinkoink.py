uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x = raw_input()
def oink(string):

    if string.endswith("yay"):
        result = string[:len(string)-3]
    else:
        splt = string[:len(string)-2]

        if splt[0] in uppercase:
            result = splt[-1].upper() + splt[0].lower() + splt[1:-1]
        else:
            result = splt[-1] + splt[0].lower() + splt[1:-1]
    return result

output = []
for item in x.split():
    output.append(oink(item))

print ' '.join(output)
