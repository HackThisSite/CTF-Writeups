x = raw_input()
def piglatinfy(string):
    vowels = "aeiou"
    consonant = "bcdfghjklmnpqrstvwxyz"
    
    if string[0].lower() in vowels:
        return string + "yay"
    else:
        return string[1:] + string[0] + "ay"

output = []
for item in x.split():
    output.append(piglatinfy(item))

print ' '.join(output)
