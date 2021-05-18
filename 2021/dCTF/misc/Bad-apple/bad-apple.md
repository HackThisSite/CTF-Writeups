# Bad Apple


> Tags: misc, mp4, video  
> Points: 200

## Challenge Description
> Someone stumbled upon this file in a secure server. What could it mean?


## Analysis
So this time I decided to follow the hint and before doing anything else I listened to the song, I noticed something in the middle of the song, for a short period of time there were some really weird sounds in it.

I quickly started Sonic Visualizer to look at the video as I found John Hammond do the same in this video https://www.youtube.com/watch?v=rAGkm4pv44s&t, but when I went to upload the video on it, I found out that I can only view audio files on Sonic Visualizer and not videos, so I found a mp4 to mp3 converter and converted the video quickly.

Then I uploaded the audio file and looked at it and found absolutely nothing, then I watched a few more videos on how to analyze audio files and in one of the videos the person was using spectrogram to analyze the audio more deeply, so I did the same thing I applied spectrogram using Shift+G, one can also use this method to apply spectrogram:

![apply_spectrogram](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/misc/Bad-apple/apply_spectrogram.png)

After applying spectrogram, I spotted this
 
![qr_code](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/misc/Bad-apple/qr_code.png)

I tried to scan the QR code like this but it did not work, so I changed its color from the panel on the right:

![default_color](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/misc/Bad-apple/default_color.png)

![color_changed](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/misc/Bad-apple/color_change.png)

I changed the color from green to White on Black, and then scanned the QR Code.

Then I finally got the flag.

The flag: dctf{sp3ctr0gr4msAreCo0l}
