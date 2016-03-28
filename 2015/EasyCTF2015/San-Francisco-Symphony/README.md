Description:
```
Who knew musicians could program? They put a flag inside /problems/sfs/sfs! But when I run the program, it's not printing out the flag. Find the flag!
```
Hint:
```
Darn. That c file isn't going to help much either. How can we find the flag using only the binary?
```
The flag is hardcoded into the binary file. We can extract it with ```strings```. To find the flag among other strings present in the binary we can use ```grep```:
```
string sfs | grep easyctf
```
The flag is: ```easyctf{w0aw_stor1ng_fl4gs_in_pla1nt3xt_i5_s0oper_s3cure}```
