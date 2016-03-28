message = "<redacted>"
key = 3
encrypted = ' '.join([str(ord(c)//key) for c in message])
print(encrypted)