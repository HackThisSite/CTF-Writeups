# tracer

## Details

- Difficulty: easy
- Section: for

## Description

Tracing the Kuchenblech-Mafia is hard!

## Analysis

We are given a large [strace](https://linux.die.net/man/1/strace) [file](./run.log). It documents every single system call during a single bash session. 

By searching for `execve` one can easily find all the processes tha have been executed during that session.

```
$ grep execve run.log
264   execve("/bin/bash", ["/bin/bash"], 0x7ffdebc8fb30 /* 8 vars */) = 0
266   execve("/usr/bin/groups", ["groups"], 0x5592eb5c2ed0 /* 8 vars */) = 0
268   execve("/usr/bin/dircolors", ["dircolors", "-b"], 0x5592eb5c2ed0 /* 8 vars */) = 0
269   execve("/usr/bin/apt", ["apt", "install", "vim"], 0x5592eb5cdef0 /* 8 vars */) = 0
...
...
...
541   execve("/usr/bin/vim", ["vim", "Flag"], 0x5592eb5cdef0 /* 8 vars */) = 0
```

Most of the calls are responsible for installing `vim` on the system but the last occurence of `execve` in the log uses the installed editor to edit a file called `Flag`.

Filtering all `read` calls on the file descriptor `0` (`stdin`) which happen after `vim` is launched yields the keystrokes input into the editor.

```
$ grep read(0 run.log
...
541   read(0, "i", 4096)                = 1
541   read(0, "j", 4096)                = 1
541   read(0, "\r", 4096)               = 1
541   read(0, "\r", 4096)               = 1
541   read(0, "\r", 4096)               = 1
541   read(0, "u", 4096)                = 1
541   read(0, "n", 4096)                = 1
541   read(0, "\r", 4096)               = 1
541   read(0, "\r", 4096)               = 1
541   read(0, "i", 4096)                = 1
541   read(0, "o", 4096)                = 1
541   read(0, "\r", 4096)               = 1
541   read(0, "r", 4096)                = 1
541   read(0, "-", 4096)                = 1
541   read(0, "\r", 4096)               = 1
541   read(0, "n", 4096)                = 1
541   read(0, "a", 4096)                = 1
541   read(0, "\33", 4096)              = 1
541   read(0, "y", 4096)                = 1
541   read(0, "y", 4096)                = 1
541   read(0, "p", 4096)                = 1
541   read(0, "A", 4096)                = 1
541   read(0, "\177", 4096)             = 1
541   read(0, "o", 4096)                = 1
541   read(0, "\r", 4096)               = 1
541   read(0, "\r", 4096)               = 1
541   read(0, "i", 4096)                = 1
541   read(0, "\r", 4096)               = 1
541   read(0, "s", 4096)                = 1
541   read(0, "\r", 4096)               = 1
541   read(0, "\r", 4096)               = 1
541   read(0, "w", 4096)                = 1
541   read(0, "a", 4096)                = 1
541   read(0, "\r", 4096)               = 1
541   read(0, "y", 4096)                = 1
541   read(0, "\r", 4096)               = 1
541   read(0, "b", 4096)                = 1
541   read(0, "e", 4096)                = 1
541   read(0, "\r", 4096)               = 1
541   read(0, "t", 4096)                = 1
541   read(0, "t", 4096)                = 1
541   read(0, "e", 4096)                = 1
541   read(0, "\r", 4096)               = 1
541   read(0, "\r", 4096)               = 1
541   read(0, "r", 4096)                = 1
541   read(0, "!", 4096)                = 1
541   read(0, "\33", 4096)              = 1
541   read(0, "g", 4096)                = 1
541   read(0, "g", 4096)                = 1
541   read(0, "J", 4096)                = 1
541   read(0, "J", 4096)                = 1
541   read(0, "J", 4096)                = 1
541   read(0, "J", 4096)                = 1
541   read(0, "J", 4096)                = 1
541   read(0, "J", 4096)                = 1
541   read(0, "J", 4096)                = 1
541   read(0, "J", 4096)                = 1
541   read(0, "J", 4096)                = 1
541   read(0, "J", 4096)                = 1
541   read(0, "J", 4096)                = 1
541   read(0, "J", 4096)                = 1
541   read(0, "J", 4096)                = 1
541   read(0, "J", 4096)                = 1
541   read(0, "J", 4096)                = 1
541   read(0, "J", 4096)                = 1
541   read(0, "J", 4096)                = 1
541   read(0, "J", 4096)                = 1
541   read(0, "b", 4096)                = 1
541   read(0, "b", 4096)                = 1
541   read(0, "~", 4096)                = 1
541   read(0, "~", 4096)                = 1
541   read(0, "~", 4096)                = 1
541   read(0, "~", 4096)                = 1
541   read(0, "~", 4096)                = 1
541   read(0, "~", 4096)                = 1
541   read(0, "~", 4096)                = 1
541   read(0, "~", 4096)                = 1
541   read(0, "\33", 4096)              = 1
541   read(0, ":", 4096)                = 1
541   read(0, "s", 4096)                = 1
541   read(0, "/", 4096)                = 1
541   read(0, " ", 4096)                = 1
541   read(0, "/", 4096)                = 1
541   read(0, "/", 4096)                = 1
541   read(0, "g", 4096)                = 1
541   read(0, "\r", 4096)               = 1
541   read(0, "\33", 4096)              = 1
541   read(0, ":", 4096)                = 1
541   read(0, "w", 4096)                = 1
541   read(0, "q", 4096)                = 1
541   read(0, "\r", 4096)               = 1
...
```

`\r` and `\33` are generated when pressing the return and escape key. `\177` is the delete key.

## Solution

Opening `vim` and replaying all the keystrokes manually is enough to produce the flag:

```
junior-nanoiswayBETTER!
```
