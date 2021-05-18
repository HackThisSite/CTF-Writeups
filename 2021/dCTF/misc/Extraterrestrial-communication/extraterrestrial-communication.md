# Extraterrestrial Communication


> Tags: misc, mp3  
> Points: 200  

## Challenge Description
> Aliens have recently landed on the moon and are attempting to communicate with us. Can you figure out what they are trying to tell us?


## Analysis
First of all I listened to the audio file, it was nothing but beeps, so I thought it would be morse code, so I tried decoding it with https://morsecode.world/international/decoder/audio-decoder-adaptive.html but it did not work, as it turned out that the audio isn’t morse code.

I had never done any CTF challenge which included an audio file, so I went straight to me good ol’ friend YouTube and searched for “how to analyze mp3 files for CTFs”, but this time YouTube couldn’t be of any help either.

So, now I tried to focus on the hint, the hint is related to how the first image was transmitted from the moon, so I quickly googled that and I found that it was transmitted in SSTV format. Then I did some research on SSTV, and I found this tool to decode audio file. http://rxsstv.cqsstv.com/

I quickly downloaded it and uploaded the audio file on it and found this

![flag](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/misc/Extraterrestrial-communication/image.png)

The flag: dctf{wHat_ev3n_1s_SSTV}
