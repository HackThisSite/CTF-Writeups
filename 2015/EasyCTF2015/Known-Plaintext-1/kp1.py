import re

def encrypt_data(string):
    string = string.decode("string_escape")
    transl = {
            '70' : '6g',
            '60' : '5g',
            '50' : '4g',
            '40' : '3g',
            '30' : '2g',
            'a'  : ':'
            }

    tmp_lst = map(lambda x: chr(ord(x) + 1).encode("hex"), string)

    tmp_string = ' '.join(tmp_lst)
    
    robj = re.compile('|'.join(transl.keys()))

    tmp_res = robj.sub(lambda m: transl[m.group(0)], tmp_string)

    result = tmp_res.replace(' ', '')

    return result
            
def decrypt_data(string):
    transl = {
            ':'  :  'a',
            '6g' : '70',
            '5g' : '60',
            '4g' : '50',
            '3g' : '40',
            '2g' : '30'
            }
    robj = re.compile('|'.join(transl.keys()))

    string = ' '.join([string[i:i+2] for i in range(0, len(string), 2)])

    tmp_string = robj.sub(lambda m: transl[m.group(0)], string)

    dec_string = map(lambda x: x.decode("hex"), tmp_string.split())

    tmp_res = map(lambda x: chr(ord(x) -1), dec_string)

    result = ''.join(tmp_res)

    return result

dump = ''

with open("knownplaintext1.in", 'r') as fi: 
        dump = fi.read()

string = dump[2:-1]
if dump.startswith("e"):
    res = encrypt_data(string)
else:
   res = decrypt_data(string)

with open("knownplaintext1.out", 'w') as fo: 
    fo.write(res)
