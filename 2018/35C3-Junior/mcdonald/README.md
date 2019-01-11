## McDonald

>Solves: 214

>Our web admin name's "Mc Donald" and he likes apples and always forgets to throw away his apple cores..

>http://35.207.132.47:85

## Analysis

This challenge does not give us source code , description mentions apple cores so we can assume we need to find some kind of apple core file.
Since ctf's usually are not about directory/file bruteforcing I decided to checkout robots.txt, since it sometimes discovers important info.

```
User-agent: *
Disallow: /backup/.DS_Store
```

Wikipedia says "In the Apple macOS operating system, .DS_Store is a file that stores custom attributes of its containing folder"
After researching it a bit I came across following tool https://github.com/gehaxelt/Python-dsstore , looks like it's from same guy that made the challenge!

## Solution

I ran the tool on .DS_Store file and discovered a, b and c directories.
Directory listing was disabled on every one of them so I decided to check if any of them contain .DS_Store file too. And /b/ directory did! At this point it just becomes game of finding right path. /b/.DS_Store file tells us that there are a, b and c subdirectories, /b/a/.DS_Store does the same, and /b/a/c/.DS_Store tells us there is flag.txt.

35c3_Appl3s_H1dden_F1l3s


