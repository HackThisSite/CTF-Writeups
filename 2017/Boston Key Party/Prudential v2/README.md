Prudential v2
======
### Cloud: 50 points ###

We are given a website with a username and login form, and by viewing the HTML source, we are given a way a link for its php source. (Saved here as Prudential v2.php*)
<sub>* I couldn't find official source of Prudential v2, but I edited it from Prudential v1 from memory. I am pretty sure it is right though. </sub>

The first thing we thought to do was compare what had changed between now and the original Prudential problem.

Prudential v1
``` php
if (isset($_GET['name']) and isset($_GET['password'])) {
    if ($_GET['name'] == $_GET['password'])
        print 'Your password can not be your name.';
    else if (sha1($_GET['name']) === sha1($_GET['password']))
      die('Flag: '.$flag);
    else
        print '<p class="alert">Invalid password.</p>';
}
```
Prudential v2
``` php
if (isset($_GET['name']) and isset($_GET['password'])) {
    name = (string)$_GET['name']
    password = (string)$_GET['password']
    if (name == password)
        print 'Your password can not be your name.';
    else if (sha1(name) === sha1(password))
      die('Flag: '.$flag);
    else
        print '<p class="alert">Invalid password.</p>';
}
```
 What had changed between the two sources was casting the get parameters to strings, before comparing them in ==.
The old method of solution was to use php type juggling, by making the get parameters in the url `name[]=a&password[]=a` . We spent awhile trying php type juggling to get passed its faulty `==` check, but the casting to string meant that all our attempts ultimately failed.

At this point we turned to the SHAppening(https://shattered.it/), which happened 2 days before the CTF began. Essentially, google found the first SHA Collision. They released the collisions in the form of two pdfs, and so at first we tried to urlencode and pass the PDF's as the name and password parameters. The server kept returning `414 URI Too Long` errors, because the url was well over 800kb long with the URL encoded pdfs.

If you read the research paper google actually published on the subject, https://shattered.io/static/shattered.pdf , you would see that only the prefix matters. (Page 3) As long as both messages have their correct prefixes, and the same suffix, then they will have the same SHA1. Therefore we urlencoded the collision blocks, put them in each parameter and submitted it, and got the flag. I don't have the code for this as rik is the one who actually did it, and the web page is offline for me to test any code which I wrote.

FLAG{AfterThursdayWeHadToReduceThePointValue}
