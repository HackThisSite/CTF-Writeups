Challenge: Extraterrestrial Communication
<br>
Points: 200
<br>
Category: Misc
<br>
Objective: Find the flag from the provided mp3 file
<br>
Hint: On a completely unrelated note, did you know how they transmitted the first image from the moon?
<br><br>
Process to find the flag: First of all I listened to the audio file, it was nothing but beeps, so I thought it would be morse code, so I tried decoding it with https://morsecode.world/international/decoder/audio-decoder-adaptive.html but it did not work, as it turned out that the audio isn’t morse code.
<br>
I had never done any CTF challenge which included an audio file, so I went straight to me good ol’ friend YouTube and searched for “how to analyze mp3 files for CTFs”, but this time YouTube couldn’t be of any help either.
<br>
So, now I tried to focus on the hint, the hint is related to how the first image was transmitted from the moon, so I quickly googled that and I found that it was transmitted in SSTV format. Then I did some research on SSTV, and I found this tool to decode audio file. http://rxsstv.cqsstv.com/
<br>
I quickly downloaded it and uploaded the audio file on it and found this
<br><br>
![flag](https://github.com/thirty2/CTF-Writeups/blob/master/2021/dCTF/misc/Extraterrestrial-communication/image.png)
<br>
The flag: dctf{wHat_ev3n_1s_SSTV}
