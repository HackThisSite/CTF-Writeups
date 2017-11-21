Description: Solved by 678 teams.

A lonely little text file wants to play a game: /problems/owner.

Upon tunneling over to the challenge on the server, and performing an `ls` command, we see a file called `file.txt`

Let's see the content of the file:

```
user00fc9@shell:/problems/owner$ cat file.txt
Help! I was wandering unfamiliar lands when I was suddenly taken hostage!

Please tell me who's my owner, and what his group is!
easyctf{<owner>:<group>}

__
person
```

It appears we need to find out the owner and group of whomever wrote this file on the server. So, there is a pretty simple way to get the user and group, and it's a simple `-l` option with `ls`

```
user00fc9@shell:/problems/owner$ ls -l file.txt
-rwxr-xr-x 1 leonidas sparta 165 Nov  4 01:04 file.txt
```

Okay, the file was wrote by the user `leonidas`, who belongs to group `sparta` so now all that's left is to piece together our flag:

`easyctf{leonidas:sparta}`
