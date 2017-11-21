My USB
======
* **150 points**
* **Category: Forensics**
* **Problem statement:** _I found_ [my usb](usb.img) _from a long time ago. I know there's a flag on there somewhere; can you help me find it?_
* **Hint:** _No hint_

We're given a USB img. First thing I did was try to actually restore the USB image onto a USB. We see a document called "hack.docx", with two images in it, and a zip file called flag.zip, with an image of the usaflag in it, and an image called cryptolock.png.

Doing my standard forensic analysis, (Which is quite limited), like looking at hexdumps, and looking for other file headers through scalpel*, yielded nothing.
There is some code visible on both of the images inside the word file, but it seems too distorted to be relevant.

Then I thought to scalpel the original img file.

``` bash
$ scalpel -c scalpelConfig.txt  usb.img
```

This gives 3 images, instead of just the two inside of the docx! (It doesn't give the image inside of flag.zip)

Heres the extra file:

![flag.jpg](flag.jpg)

Theres our flag!
