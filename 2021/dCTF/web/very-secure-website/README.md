# Very secure website

> Tags: web, php
> Points: 200
> Solves: 399

## Challenge Description

> Some students have built their most secure website ever. Can you spot their mistake?
> http://dctf1-chall-very-secure-site.westeurope.azurecontainer.io/

## Analysis

We are given a link to a website (http://dctf1-chall-very-secure-site.westeurope.azurecontainer.io) which takes us to a simple login form that performs a GET call to `/login.php`. On that login form page, there's also this text:

> This is a very secure website, so we will also include the source code. Nobody will ever break it. It is the best.

The "source code" text links to a file (http://dctf1-chall-very-secure-site.westeurope.azurecontainer.io/source.php), which contains the following code:

```php
<?php
    if (isset($_GET['username']) and isset($_GET['password'])) {
        if (hash("tiger128,4", $_GET['username']) != "51c3f5f5d8a8830bc5d8b7ebcb5717df") {
            echo "Invalid username";
        }
        else if (hash("tiger128,4", $_GET['password']) == "0e132798983807237937411964085731") {
            $flag = fopen("flag.txt", "r") or die("Cannot open file");
            echo fread($flag, filesize("flag.txt"));
            fclose($flag);
        }
        else {
            echo "Try harder";
        }
    }
    else {
        echo "Invalid parameters";
    }
?>
```

The first hash is easy enough to guess; it's `admin`. The second one, however, is a bit more difficult. But we don't need to run it through a password cracker like [John the Ripper](https://en.wikipedia.org/wiki/John_the_Ripper). Using a `==` comparitor operator in PHP has a long-known pitfall, known as "magic hashes." Thankfully, WhiteHat Security has [published a table](https://www.whitehatsec.com/blog/magic-hashes/) of magic hashes and a description about this `==` operator pitfall. Notably the only `tiger128,4` entry in this table has a magic hash number of `479763000`, and this works! Enter `admin` as the username and `479763000` as the password, and we get the flag: `dctf{It's_magic._I_ain't_gotta_explain_shit.}`
