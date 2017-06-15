#!/usr/bin/env python

import sys

# zo : zero ones
# d  : dictonary

def morse_decode (code) :
    # reversed morse alphabet
    rma = {
            ".-"      : "A",
            "-..."    : "B",
            "-.-."    : "C",
            "-.."     : "D",
            "."       : "E",
            "..-."    : "F",
            "--."     : "G",
            "...."    : "H",
            ".."      : "I",
            ".---"    : "J",
            "-.-"     : "K",
            ".-.."    : "L",
            "--"      : "M",
            "-."      : "N",
            "---"     : "O",
            ".--."    : "P",
            "--.-"    : "Q",
            ".-."     : "R",
            "..."     : "S",
            "-"       : "T",
            "..-"     : "U",
            "...-"    : "V",
            ".--"     : "W",
            "-..-"    : "X",
            "-.--"    : "Y",
            "--.."    : "Z",
            "/"       : " ",
            "-----"   : "0",
            ".----"   : "1",
            "..---"   : "2",
            "...--"   : "3",
            "....-"   : "4",
            "....."   : "5",
            "-...."   : "6",
            "--..."   : "7",
            "---.."   : "8",
            "----."   : "9"
    }
    return "".join([rma[x] for x in code.split(' ')])

d = { "ZERO" : "0", "ONE" : "1" }
flag = ""
zo = open(sys.argv[1], "r").read().replace("\n", "").split(" ")
flag = "".join([chr(int("".join([d[x] for x in zo[i:i+8]]),2)) for i in xrange(0,len(zo),8)])
flag = flag.decode("base64")
flag = morse_decode(flag)
flag = "AlexCTF{"+flag.replace('O', '_').replace("ALEXCTF", "")+"}"
print flag

