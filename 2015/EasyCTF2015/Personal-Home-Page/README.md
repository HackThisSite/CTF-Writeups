Description:
Solved by 519 teams.

I hate PHP.

So, this challenge has a pretty crappy description, and I love PHP. Anyway, let's talk about the challenge...

Upon viewing the website, we see a hyperlink at the bottom named flags. I immediately opened the code up in firebug:

`<p>This is probably super secure, so I have no problem hiding passwords or <i><a href="supersecretflag.txt">flags</a></i> here.</p>`

The next logical step is to navigate over to: `http://web.easyctf.com:10200/supersecretflag.txt`, upon doing so we are greated with a 403 Denied:

`You don't have permission to access /supersecretflag.txt on this server.`

Digging back into the source, we see that the home and about pages are being fetched from `index.php` by supplied GET variables and then displayed `http://web.easyctf.com:10200/?page=pages/about.html`

This means if there is poor filtering/whitelisting/blacklisting it should be possible to have the `index.php` script fetch the `supersecretflag.txt` file.

So I navigated straight over to `http://web.easyctf.com:10200/?page=supersecretflag.txt`, which displayed the flag: `easyctf{file_get_contents_is_9_safe}`
