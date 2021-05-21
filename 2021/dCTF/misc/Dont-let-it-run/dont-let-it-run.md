# Don't Let It Run


> Tags: Misc  
> Points: 100  

## Challenge Description
> PDF documents can contain unusual objects within.


## Analysis
Process to find the flag: I had never done a challenge where we had to find the flag in a PDF so this was new to me.

Whenever I get stuck with something I always go to YouTube to check how other people do this kind of stuff, so I quickly searched for “how to analyze PDFs for CTFs”, and then I found this video: https://www.youtube.com/watch?v=0IY8ir5dGGw&t.

The person in this video was using this tool https://github.com/gdelugre/origami so I quickly cloned it onto my machine.

I read a little bit about this tool and then figure that I needed to use the pdfextract tool.

So I typed the command and got this result.   


![command](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/misc/Dont-let-it-run/commands.png)

I got a folder with all the extracted data.

The folder had a few more folders.

![content](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/misc/Dont-let-it-run/content.png)

All of them were empty except scripts and the streams folder, I check the scripts folder first and it had a js file.

![js_file](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/misc/Dont-let-it-run/js%20file.png)

I opened up the file to  see what was inside of it, and I found the flag.

![js_coding](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/misc/Dont-let-it-run/js%20coding.png)

The flag: dctf{pdf_1nj3ct3d}
