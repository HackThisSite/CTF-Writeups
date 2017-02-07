Description: Solved by 992 teams.
Oh look, it's a perfectly innocent picture of an [apple](https://www.easyctf.com/static/problems/apple/apple.jpg. Nothing to see here!)

![Apple](https://github.com/Ninjex/Wargame-Writeups/raw/master/CaptureTheFlag/2015/EasyCTF2015/An-apple-a-day-keeps-the-dinosaur-away%3F/apple.jpg?raw=true"Apple")

Solving this challenge is pretty easy. We just had to click the link, download the image and issue following commands under Linux

`strings apple.jpg | grep easyctf`

which revealed the flag to be `easyctf{w0w_much_appl3s}`
