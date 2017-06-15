#!/usr/bin/env python3

import re
import os
import sys
from subprocess import Popen, PIPE

ops = {
        "xor" : lambda a, b : a ^ b,
        "add" : lambda a, b : a + b,
        "sub" : lambda a, b : b - a,
        "or"  : lambda a, b : a | b,
        "and" : lambda a, b : a & b
    }

def bash (cmd) :
    ret = Popen(cmd.encode(), stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=True).communicate()
    #if ret[1] : print(ret[1])
    return ret[0].decode()

def rshift(val, n): return val>>n if val >= 0 else (val+0x100000000)>>n

def main (filenames) :
    print(" [+] out : ")
    out = ""
    eaxp = r"=0x[a-f0-9]+"
    clp  = r"=[0-9]+"
    clp2 = r"=\-[0-9]+"
    hexp = r"0x[a-f0-9]+"
    charp= r"\(.\)"
    for fname in filenames :
        #os.system("clear")
        entry0 = bash("r2 {fname} <<< 'pd 30'".format(fname=fname)).split('\n')
        i = [x for x in range(len(entry0)) if 'mov' in entry0[x] and 'eax' in entry0[x] and 'dword' in entry0[x]]
        i = i[0]
        eax = int(re.findall(eaxp, entry0[i])[0][1:], 16)
        ecx = int(re.findall(hexp, entry0[i+1])[1], 16)
        call= re.findall(hexp, entry0[i+2])[1]
        expr= bash("r2 {fname} <<< 's {call}; pd 1'".format(fname=fname, call=call)).split('\n')[-2]
        expr= [k for k in ops.keys() if k in expr][0]
        ans = ops[expr](ecx, eax)
        try : cl  = int(re.findall(clp, entry0[i+5])[0][1:])
        except : cl = int(re.findall(clp2, entry0[i+5])[0][1:])
        char= chr(rshift(int(ans), cl) & 0xff)
        #char= bash("wine {fname} <<< {ans}".format(fname=fname, ans=ans)).split('\n')[1]
        #char= re.findall(charp, char)[0][1:-1]
        out += char
        print(out)
        print(len(out))
    print()
    f = open("out.txt", 'w')
    f.write(out)
    f.close()

if __name__ == "__main__" :
    print(" [+] getting files....")
    filenames = bash("echo $(ls bins/*.exe --color=none)").split(' ')
    print(" [+] cracking....")
    main(filenames)

