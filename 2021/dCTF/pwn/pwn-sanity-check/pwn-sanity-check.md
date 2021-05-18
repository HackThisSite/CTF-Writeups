Challenge: Strong Password
<br>
Points: 100
<br>
Category: Crypto
<br>
Objective: Retrieve the flag from a password protected zip file
<br>
Hint: Don't use fcrackzip(this hint was added later on)
<br>

Process to find the flag: So first of all I tried all the passwords I could think of and none of them worked.
<br>
As I couldn’t find any password that would work I went to google and started looking for how to brute force a password for zip file and I stumbled across an app to brute force password, I tried it and it did not work at all, so I did some more research and found fcrackzip and I left it running for an hour and wasn’t working either, then the hint was uploaded and it said don’t use fcrackzip.
<br>
So once again I went in search for a tool to crack open zip files and I found out that John The Ripper (https://github.com/openwall/john) can also be used to brute force zip files.
<br>
I already had this tool and had used before so I did not have any problem with it.
<br>
I quickly got the zip file’s hash like this:
 

Then I used john to brute force and get the password, I also used rockyou.txt (https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) wordlist for cracking the password
 
The password: Bo38AkRcE600X8DbK3600
<br>
Then I opened the file inside of the zip file 
 


It had this text
 

So I just pressed Ctrl+F and then searched for “dctf” and found this
 

The flag: dctf{r0cKyoU_f0r_tHe_w1n}
