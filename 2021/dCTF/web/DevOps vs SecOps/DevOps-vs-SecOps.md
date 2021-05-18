# DevOps vs SecOps


> Tags: misc
> Points: 200

## Challenge Description
>Automatization is amazing when it works, but it all comes at a cost... You have to be careful...

## Analysis

So first of all this is not a Web challenge, this is a Misc challenge the devs added it in the web category by mistake.

So if a user completed Leak Spin, they could complete DevOps vs SecOps as well, because when you find Leak Spin challenge on the GitHub you will see two more repositories.

![github_repo](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/web/DevOps%20vs%20SecOps/github_repo.png)

When you open up DevOps vs SecOps repository you will find two files readme.md which doesn’t contain anything useful and another file challenge.yml which when you open you will find this: 

![not_flag](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/web/DevOps%20vs%20SecOps/not_flag.png)

But this is not the flag, so to find the flag you need to go to .github repository.
This is what .github repository contains and if you check all the of these files carefully you will find the flag.

![files](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/web/DevOps%20vs%20SecOps/files.png)

The flag is in the setup.py file

![setup.py](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/web/DevOps%20vs%20SecOps/setup_py.png)

The flag: dctf{H3ll0_fr0m_1T_guy}
