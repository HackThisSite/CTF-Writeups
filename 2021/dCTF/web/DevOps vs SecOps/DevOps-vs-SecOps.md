Challenge: DevOps vs SecOps
<br>
Points: 200
<br>
Category: Web
<br>
Objective: Find the flag
<br>
Hint: What does automation and DevOps remind you of? For me thats CI/CD...
<br><br>
Process to find the flag: So first of all this is not a Web challenge, this is a Misc challenge the devs added it in the web category by mistake.
<br>
So if a user completed Leak Spin, they could complete DevOps vs SecOps as well, because when you find Leak Spin challenge on the GitHub you will see two more repositories.
<br><br>
![github_repo](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/web/DevOps%20vs%20SecOps/github_repo.png)
<br>
When you open up DevOps vs SecOps repository you will find two files readme.md which doesn’t contain anything useful and another file challenge.yml which when you open you will find this: 
<br><br>
![not_flag](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/web/DevOps%20vs%20SecOps/not_flag.png)
<br>
But this is not the flag, so to find the flag you need to go to .github repository.
This is what .github repository contains and if you check all the of these files carefully you will find the flag.
<br><br>
![files](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/web/DevOps%20vs%20SecOps/files.png)
<br>
The flag is in the setup.py file
<br><br>
![setup.py](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/web/DevOps%20vs%20SecOps/setup_py.png)
<br>
The flag: dctf{H3ll0_fr0m_1T_guy}
