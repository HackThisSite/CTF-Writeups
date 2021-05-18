Challenge: Dragon
<br>
Points: 100
<br>
Category: Misc
<br>
Objective: Find the flag from the provided image
<br><br>
Process to find the flag: So first of all I tried a couple of tools such zsteg, exiftool and stegsolve to find the flag.
<br>
I knew it wasn’t going to be hard because it was just of 100 points.
<br>
I also used strings command in the terminal to check if anything is hidden inside its data.
<br>
My result after using zsteg, exiftool, stegsolve and strings was basically nothing, or at least nothing useful.
<br>
So till now I had checked metadata, normal data, the image in different types of colors but I still hadn’t found the flag.
<br>
I researched a little bit and I found this website which is basically the web version of stegsolve and it is better than it, at least in my opinion it is. 
<br>
Here is the link to the site: https://aperisolve.fr/
<br>
So when I uploaded the image here I quickly spotted the flag.
<br><br>
![image](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/misc/Dragon/image.png)
<br><br>
The flag: dctf{N0w_Y0u_s3e_m3}
