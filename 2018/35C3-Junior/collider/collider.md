# Collider

>Solves: 64

>Your task is pretty simple: Upload two PDF files. The first should contain the string "NO FLAG!" and the other one "GIVE FLAG!", but both should have the same MD5 hash!
>http://35.207.132.47:83

## Analysis

In HTML source there is comment ```<!-- My source is at /src.tgz -->```.
After downloading and unpacking the archive we can see following php code
```php

<?php
    include_once "config.php";
    if(isset($_POST['submit']))  {
            $pdf1 = $_FILES['pdf1']['tmp_name'];
            $pdf2 = $_FILES['pdf2']['tmp_name'];

            if(! strstr(shell_exec("pdftotext $pdf1 - | head -n 1 | grep -oP '^NO FLAG!$'"), "NO FLAG!")) {
                die("The first pdf does not contain 'NO FLAG!'");
            }

            if(! strstr(shell_exec("pdftotext $pdf2 - | head -n 1 | grep -oP '^GIVE FLAG!$'"), "GIVE FLAG!")) {
                die("The second pdf does not contain 'GIVE FLAG!'");
            }

            if(md5_file($pdf1) != md5_file($pdf2)) {
                die("The MD5 hashes do not match!");
            }

            echo "$FLAG";

    }
?>
```
This code converts uploaded pdf's to text files, then checks if first line is 'NO FLAG!'
or 'GIVE FLAG!'. It gives flag only if md5 hashes of file match.

Command injection in shell_exec function is not possible because of server side generated temporary filenames.

## Solution

Following solution was not intended way to solve the challenge, therefore it's unelegant and it took a while to generate , but it still works ;)

While analyzing code what immediately caught my attention is following line:

```php 
if(md5_file($pdf1) != md5_file($pdf2)) {
```

Comparison of md5 hashes is [loose](https://www.whitehatsec.com/blog/magic-hashes/)!
So if md5 hash of each file is "0e" followed by 30 digits PHP will recognize them as same, and we will get the flag!

I created 2 pdf files, one containing just "NO FLAG!" and other containing just "GIVE FLAG!".
Then I created python script to append data after pdf %EOF tag (Thank you Leeky for telling me that pdf with random garbage after %EOF will still be valid pdf!)

```python
import hashlib
import string

noflag=open("noflag.pdf","rb").read()

c=0

while 1:
        noflagwin=noflag+str(c)
        c=c+1
        d=hashlib.md5(noflagwin).hexdigest()
        if d[:2]=="0e" and d[2:].isdigit() :
                print "found one"
                f=open("noflagwin.pdf","wb").write(noflagwin)
                break
        print c
```

And I did same for giveflag.pdf, after some time it generated flag winning files!

35C3_N3v3r_TrusT_MD5 

I was later told by one of organizers that loose comparison was unintended, for intended solution see [this writeup](https://ctftime.org/writeup/12836) by fearless.
