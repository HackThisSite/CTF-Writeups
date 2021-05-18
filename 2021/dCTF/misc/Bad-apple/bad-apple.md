Challenge: Bad Apple
<br>
Points: 200
<br>
Category: Misc
<br>
Objective: Find the flag from the given video
<br>
Hint: Did you even listen to the song?
<br><br>
Process to find the flag: So this time I decided to follow the hint and before doing anything else I listened to the song, I noticed something in the middle of the song, for a short period of time there were some really weird sounds in it.
<br>
I quickly started Sonic Visualizer to look at the video as I found John Hammond do the same in this video https://www.youtube.com/watch?v=rAGkm4pv44s&t, but when I went to upload the video on it, I found out that I can only view audio files on Sonic Visualizer and not videos, so I found a mp4 to mp3 converter and converted the video quickly.
<br>
Then I uploaded the audio file and looked at it and found absolutely nothing, then I watched a few more videos on how to analyze audio files and in one of the videos the person was using spectrogram to analyze the audio more deeply, so I did the same thing I applied spectrogram using Shift+G, one can also use this method to apply spectrogram:
<br><br>
![apply_spectrogram](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/misc/Bad-apple/apply_spectrogram.png)
<br>
After applying spectrogram, I spotted this
<br><br> 
![qr_code](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/misc/Bad-apple/qr_code.png)
<br>
I tried to scan the QR code like this but it did not work, so I changed its color from the panel on the right:
<br><br>
![default_color](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/misc/Bad-apple/default_color.png)
<br>
![color_changed](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/misc/Bad-apple/color_change.png)
<br>
I changed the color from green to White on Black, and then scanned the QR Code.
<br>
Then I finally got the flag.
<br>
The flag: dctf{sp3ctr0gr4msAreCo0l}
