# Leak Spin


> Tags: misc  
> Points: 100  


## Description
> We have confident insider report that one of the flags was leaked online. Can you find it?


## Analysis

For this challenge the organizers did not give us anything except a hint and the description of the challenge was "We have confident insider report that one of the flags was leaked online. Can you find it?"

At first this seemed ridiculous, and I thought the developer(devs) made a mistake and left the challenge midway, but I noticed there were a few solves at that time so that wasn’t the case the challenge was working perfectly.

Then I noticed the hint, and I was trying really hard to think what can they control, and for some reason I could only think of their website, so I scanned their whole site, did some google dorking trying to find the flag but couldn’t find anything at all.

Then I figured it’s not going to be on their site then I google DCTF and funnily enough I found this:

![dctf_football](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/misc/Leak-spin/DCTF_football.png)

So this made it even harder to find information about DCTF.

But then something clicked in my mind and I instantly thought about GitHub, so I googled “dctf github” but couldn’t find anyone useful so I tried to search them with their full name “dctf dragonsec si” and I found their Twitter page which completely distracted me from the motive of searching for their GitHub page, so I tried to look for flag on their Twitter page and couldn’t find anything, then at last I googled “dctf.dragonsec.si github” and I found their GitHub page. 

On their GitHub page I found 3 repositories and one of them was:

![challenge](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/misc/Leak-spin/dctf_github.png)

This felt like progress to me and when I opened it up, I found two files, a readme.md and a challenge.yml, the readme file had nothing useful, but the challenge file had this:

![image](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/misc/Leak-spin/image.png)

The flag: dctf{I_L1k3_L1evaAn_P0lkk4}
