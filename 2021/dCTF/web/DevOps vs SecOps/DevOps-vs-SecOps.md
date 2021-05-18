Challenge: DevOps vs SecOps
<br>
Points: 200
<br>
Category: Web
<br>
Objective: Find the flag
<br>
Hint: What does automation and DevOps remind you of? For me thats CI/CD...
<br>
Process to find the flag: So first of all this is not a Web challenge, this is a Misc challenge the devs added it in the web category by mistake.
<br>
So if a user completed Leak Spin, they could complete DevOps vs SecOps as well, because when you find Leak Spin challenge on the GitHub you will see two more repositories.
 
When you open up DevOps vs SecOps repository you will find two files readme.md which doesn’t contain anything useful and another file challenge.yml which when you open you will find this: 

But this is not the flag, so to find the flag you need to go to .github repository.
This is what .github repository contains and if you check all the of these files carefully you will find the flag.
 

The flag is in the setup.py file
 

The flag: dctf{H3ll0_fr0m_1T_guy}
