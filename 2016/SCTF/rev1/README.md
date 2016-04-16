#Rev1

Let's start out with an easy, typical reversing problem.

The answer will not be in the typical sctf{flag} format, so when you do get it, you must put it into the format by doing sctf{flag_you_found}


## Solution overview

There are different ways to solve this, one easy mode one and one where we use gdb in order to see whats going on! Or you could just do a string dump of the binary and see if you could find the flag hardcoded in there.

We will use the **gdb** approach in this writeup, so you might learn something.

First lets check what kind of binary we got

`file ./rev1`

gives us the following info:

`rev1: ELF 64-bit LSB executable, x86-64, version 1`

Ok its a 64 bit executable x86. We could run this on our system, but we'd like to check what it does first using the gnu debugger **gdb**.

##Debugging with gdb

 To fire up gdb issue the following command.

`gdb ./rev1`

This opens the debugger and we are left on the gdb command prompt **(gdb)** , its waiting for our command.

First we will set a breakpoint to the main() function, which we assume is present. We make this breakpoint cause we wanna step over the code that loads the binary and get straight into the main where the business is happening.
(in the following dont type in (gdb), only the text after it ).

`(gdb) break main`

We get a confirmation that the breakpoint has been set, and at what offset.

Now in order to see the assembly listing, we issue the command:
`(gdb) disas main`

This will give us the assembly listing of the main function, to the left in each line of the listing is the address of the instruction, in the <> is the offset counting from the start of the main function, we will use this number to refer to where we are in the listing, once we get to the walkthrough.

Finally after this we get the instruction OR data starting at the address given.

The listing of the disassembly

```
0x0000000000400656 <+0>:     push   %rbp
0x0000000000400657 <+1>:     mov    %rsp,%rbp
0x000000000040065a <+4>:     sub    $0x10,%rsp
0x000000000040065e <+8>:     movl   $0x0,-0x4(%rbp)
0x0000000000400665 <+15>:    movabs $0x2121217230783468,%rax
0x000000000040066f <+25>:    mov    %rax,-0x10(%rbp)
0x0000000000400673 <+29>:    movb   $0x0,-0x8(%rbp)
0x0000000000400677 <+33>:    mov    $0x400744,%edi
0x000000000040067c <+38>:    callq  0x400530 <puts@plt>
0x0000000000400681 <+43>:    lea    -0x4(%rbp),%rax
0x0000000000400685 <+47>:    mov    %rax,%rsi
0x0000000000400688 <+50>:    mov    $0x400760,%edi
0x000000000040068d <+55>:    mov    $0x0,%eax
0x0000000000400692 <+60>:    callq  0x400550 <scanf@plt>
0x0000000000400697 <+65>:    mov    -0x4(%rbp),%eax
0x000000000040069a <+68>:    cmp    $0x5b74,%eax
0x000000000040069f <+73>:    jne    0x4006b7 <main+97>
0x00000000004006a1 <+75>:    lea    -0x10(%rbp),%rax
0x00000000004006a5 <+79>:    mov    %rax,%rsi
0x00000000004006a8 <+82>:    mov    $0x400763,%edi
0x00000000004006ad <+87>:    mov    $0x0,%eax
0x00000000004006b2 <+92>:    callq  0x400510 <printf@plt>
0x00000000004006b7 <+97>:    mov    $0x0,%eax
0x00000000004006bc <+102>:   leaveq
0x00000000004006bd <+103>:   retq

```

The first 3 instructions

```
push   %rbp
mov    %rsp,%rbp
sub    $0x10,%rsp
```

Is the prologue, here the basepointer is saved to the stack, so we have it for later use when we return to the caller. We also copy the stack pointer to the basepointer and finaly reserve 16 bytes for local variables to  our main function.

Every time we see : -0x4(%rbp) or -0x8(%rbp) it means that we access the local variable in reference to the base pointer, the stack grows from high address down, so -0x4(%rbp) is the first local variable, -0x8(%rbp) is the second variable etc.

Usual the next thing that is happening is initialization of local variables as explained above we got 16 bytes set aside for these.

At main+8

```
movl   0x0,-0x4(%rbp)
```

We initialize the first local variable to 0, its a 32 bit value as we can see from **movl** which means move long, which translates to a 32 bit value.


At main+15 and main+25

```
mov    $0x2121217230783468,%rax
mov    %rax,-0x10(%rbp)
```

We first copy a litteral 64 bit value to the rax register and then save this to the second local variable. As this variable is 64 bit, it takes up 8 bytes, ending the value at -0x08(%rbp) (not including this).

At main+29

```
movb   $0x0,-0x8(%rbp)
```

We can see we effectively append a 0 byte to the end of our first variable, telling us that the variable starting at -0x10(%rbp) will likely be interpreted as a string. Your machine is little endian which means the string in %rax will be stored at the address -0x10(%rbp) with the least significant byte first and so on.

Our string will thus be: **68 34 78 30 72 21 21 21** translated to ascii this will be **h4x0r!!!**

We could stop here and call it a day and try to submit the flag as **sctf{h4x0r!!!}** but that won't make you or I better at assembler.

Lets move on and look at main+33 and main+38, here we call the c function puts, which takes an address of 0x400744, which is placed in %edi, common c calling convensions state that the first parameter to a function should be available in edi/rdi for 32/64 bit values.

Lets examine what string is located at that address, we know puts need an address to a 0 terminated string, which it in turn will print out. (a char*). To examine a string at a known address issue the following command:

`(gdb) print (char*) 0x400744`
