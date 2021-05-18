Challenge: Don’t let it run
<br>
Points: 100
<br>
Category: Misc
<br>
Objective: Find the flag from provided PDF
<br><br>
Process to find the flag: I had never done a challenge where we had to find the flag in a PDF so this was new to me.
<br>
Whenever I get stuck with something I always go to YouTube to check how other people do this kind of stuff, so I quickly searched for “how to analyze PDFs for CTFs”, and then I found this video: https://www.youtube.com/watch?v=0IY8ir5dGGw&t.
<br>
The person in this video was using this tool https://github.com/gdelugre/origami so I quickly cloned it onto my machine.
<br>
I read a little bit about this tool and then figure that I needed to use the pdfextract tool.
<br>
So I typed the command and got this result.   
<br><br>

<br>
I got a folder with all the extracted data.
<br>
The folder had a few more folders.
<br><br>

<br>
All of them were empty except scripts and the streams folder, I check the scripts folder first and it had a js file.
<br><br>

<br>
I opened up the file to  see what was inside of it, and I found the flag.
<br><br>

<br> 
The flag: dctf{pdf_1nj3ct3d}
