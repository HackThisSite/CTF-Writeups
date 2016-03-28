import string

def encrypt_data(plaintext):
    orig = string.ascii_uppercase + string.ascii_lowercase
    cipher = "CWKygzGDOIVBLnQqpmHtfJxYoShvMREeFwdTNuAcilakZUrXsbjP"
    enc_transl = string.maketrans(orig, cipher)

    result = plaintext.translate(enc_transl)
    
    return result
            
def decrypt_data(ciphertext):
    orig = string.ascii_uppercase + string.ascii_lowercase
    cipher = "CWKygzGDOIVBLnQqpmHtfJxYoShvMREeFwdTNuAcilakZUrXsbjP"
    dec_transl = string.maketrans(cipher, orig)

    result = ciphertext.translate(dec_transl)
    return result

dump = ''
with open("knownplaintext3.in", 'r') as fi: 
    dump = fi.read()

strng = dump[2:]

if dump.startswith("e"):
    res = encrypt_data(strng)
else:
    res = decrypt_data(strng)
   
with open("knownplaintext3.out", 'w') as fo: 
    fo.write(res)
