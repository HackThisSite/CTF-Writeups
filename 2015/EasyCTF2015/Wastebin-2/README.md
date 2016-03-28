Description: Solved by 383 teams.

So after the previous fiasco, I decided to generate a random admin password, and hide it in a file that no one will ever find. And don't try Googling it either, cuz Google can't find it either! Hahaha >:) Link

So, the description mentions not Googling it either. This made me assume it was a `robots.txt` deal right off the bat, and I was not further from correct.

Navigating from `http://web.easyctf.com:10207/2/index.php` over to `http://web.easyctf.com:10207/robots.txt` reveals the following:

```
User-agent: *
Disallow: /2/password_Tj9WBkFpORmHYaYBG5GR7VZzgDaEM2e2aWeeCRtJ.txt
```

Now, we should obviously navigate over to given directory: `http://web.easyctf.com:10207/2/password_Tj9WBkFpORmHYaYBG5GR7VZzgDaEM2e2aWeeCRtJ.txt`

This reveals to us the following text:

`11FutLBObDdAnSIyEo9LF6TLiWuG8GpHSLnRBAYD4jUGM0O4Jbt8KPasU5CpAGmZW2dX97HX4xHau8asmrN5CzIiM6Xb51plWa3q`

Looking back at our description, we know there is an account named admin. Let's login as `admin:11FutLBObDdAnSIyEo9LF6TLiWuG8GpHSLnRBAYD4jUGM0O4Jbt8KPasU5CpAGmZW2dX97HX4xHau8asmrN5CzIiM6Xb51plWa3q`

We get greated with a nice message: `Nice. The flag is easyctf{looks_like_my_robot_proof_protection_isn't_very_human_proof}`
