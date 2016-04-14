#Rain or Shine

I've been working so hard on problems that I didn't even notice it was raining outside. I decided to take a short break and record some ambient sound for a game I've been working on, and just for fun I stuck a flag somewhere in there too! Can you find it for me?

**Hint:** *If you're stuck, start [here](https://en.wikipedia.org/wiki/Steganography).*

## Solution overview

We get a file **rain.wav** which contain what appears to be a recording of some thunderstorm. You can also hear some hiss in the end. But from the challenge text, we can immediately deduce that we have to carve our something else from the file.

### Preliminary search

A quick way to see if you have any text based headers or other ascii information in a file, is to run it through the **string** command in linux. It won't always come up with any usable information, as many file headers are funny "magic" numbers, but its a quick way to start.

`strings rain.wav | less`

We pipe the result of the strings command through less, so we can scroll through the output. A bit down, we can see it plastered with text hinting to Adobe: "Adobe Photoshop CC (Windows)", and some xml header where we find another interesting part:

**<stEvt:parameters>from image/png to image/tiff</stEvt:parameters>**

This tells us that this file is a tiff file, so "strings" business  saves us some time, so we don't have to run through our list of different magic numbers for different file types.

### Carving it out

We use this [list of file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures), in order to determine the magic header bytes for tiff files. We assume the data is stored in little endian format, so the bytes we are looking for are: **49 49 2A 00**.

####Are you the bytes we are looking for?
We fire up our favorite hex editor **bless** and do a search for the bytes **49 49 2A 00**, and sure enough they are present. And sure enough we find it at offset **0058fd00**!

We copy the data from and including this offset, untill the end of the file and paste it into a new file called **embedded.tiff**

### Opening the tiff (hardest part)
Being an avid linux user, I immediately opened the file in gimp! It looked to be a QR-Code that had been splitted into 4 quadrants and shuffled around to form an invalid QR-Code.

I tried here to move the parts around, but no matter what it wouldn't fit, even rotating didn't help. Asked a mate to try to open it in photoshop as this was the program it was made with in the beginning. He could open it and he said there was layers in it, so apparently photoshop had something called layered tiffs.

I searched the trusty google, and found a lot of programs that could open layered tiffs, including gnome, but they all flattened the layers, which was no good to me. The general consensus out there was to use photoshop if you wanted to work with layered tiffs.

Well I had to finish the mission, so i bought a $200 windows licence and a $1500 photoshop licence, and spend the next couple of hours installing it all.

After a tough installation and some 4gb downloading, I finally got the image opened in photoshop and true enough it had layers!!! I moved the layers around till it resembled a correct QR-Code and used my trusty phone to get the text out. The text of course was the flag!!

**sctf{5t3g0n4gr4phy_i5_fun_r1t3?}**
