# Finn

The Resistance intercepted this suspicious picture of Finn's old stormtrooper helmet, sent by General Hux to Kylo Ren. Hux isn't exactly Finn's biggest fan. What could he be hiding? Good luck!

If you get stuck, We also have this blob of sarcasm, which may or may not be useful in your quest. Worth a shot right?.

```
Everyone complains that my problems are too random. Fine. Here is EXACTLY how to solve this problem.

1. Wow I have an image. I wonder why it’s so big (read: grandma, what large eyes you have)
2. So I figured that part out. Great, there’s a password. I wonder what that has to do with this image. Or wait, I could just brute force it, right? Either way works. It’s called reading the problem description. Or even the title. Titles do matter.
3. Yay, 2 images. What’s the difference? Hmmmm, I wonder what would happen if I expressed that difference pictorially. 
4. Well I got some stuff, but it makes no sense. Oh wait, maybe I need a key! Let’s go back to that thing we extracted earlier, shall we? Maybe those discrepancies are ACTUALLY USEFUL. Nothing is an accident, not even random out of place pixels. Check them. Carefully.
5. What do I do with this message and key? How about, the most obvious thing in every CTF ever. Seriously.

So you got the flag. Congrats! See, it wasn’t that bad.
```

## Solution

We are given a jpg file and a recipe to follow, in order to get to the flag.

First hint suggests that the jpg file containst something more, maybe some other file is embedded
into it.

Second hint suggests that its a zip file, which is password protected.

We fire up bless, a linux hex editor, and search for the magic bytes of a zip file
*50 4B 03 04* , we find this and we can see beforfe it, is the closing bytes of the jpg file
*FF D9*. So what we do is mark the section of the file and cut out the beginning and up till
the first *50 4B 03 04*, and save the resulting file as finn.zip

unzipping the file we can see ther are 2 image files inside in a directory *kylo*, called
*kylo1.png* and *kylo2.png*. The files are however encrypted.

### john the ripper

As we are not good at guessing, we fire up john the ripper, in order to crack the password
of the zip file, we use the jumbo package, which containst the tool zip2john, which 
extract a password hash that john can use, from the zip file.

We use incremental mode, and within seconds we get the password for the zipfile which is
*2187*

### Steganography

Hint 3 suggests that we should do some image manipulation on the images, that we have to
express the difference. First thing that springs to mind is GIMP and using the images
as 2 layers and use some layer algorithms on them.

Open kylo1.png in gimp and open kylo2.jpg also, and copy kylo2.jpg into kylo1.jpg as
a layer. Make sure the layers on kylo1 are ordered so kylo2 is on top.

In the layer view Ctrl+L, click the first layer (kylo2) and choose overlay mode:
*Difference* 

This gives us a pretty dark image, but we can see there are different shades of gray.

Merge the layers, by rightclicking on a layer in the layer view (ctrl+l) and choose
merge visible layers.

Use the color picker tool to pic a color from the ultra grey pattern (qr-code)
Should be the color #010101.

Now we exchange this color with white by going to Colors->Map->Color Exchange
where from color is our fg color of #010101 and the color we exchange with is white.

We now get a clear qr code which we now scan with our phone, and get the following
hex values:

`"\x63\x68\x66\x63\x7e\x71\x73\x34\x76\x57\x72\x3c\x74\x73\x5c\x31\x75\x5d\x6b\x32\x34\x77\x59\x38\x4c\x7f"`

its 26 bytes in all.

As we can see, there are some wierd pixels in the lower left corner of the qr code, 
seems its different shades of gray. 

Before we go on, revert the color exchange you just did, so we preserve the #010101 
colored pixels as they were.

Now from the bottom left of the qr code, we take each grey/black pixel and note the color
value of either of the RGB values (its grey so they are all the same, we just take 1).

We end up with 26 numbers
`5,4,7,4,5,2,7,0,4,8,5,8,6,0,3,0,6,2,9,1,1,3,6,2,8,2`

now we are left with 26 bytes and 26 numbers, and the hint states that we now have to
do the most obvious thing ever.

We make a small perl script to do just that

```
#!/usr/bin/perl

my  $str = "\x63\x68\x66\x63\x7e\x71\x73\x34\x76\x57\x72\x3c\x74\x73\x5c\x31\x75\x5d\x6b\x32\x34\x77\x59\x38\x4c\x7f";
my @pixels = (5,4,7,4,5,2,7,0,4,8,5,8,6,0,3,0,6,2,9,1,1,3,6,2,8,2);  # values of each 5,5,5 rgb = 5

my @chars = split "",$str;
my $i = 0;

$i=0;
foreach my $c (@chars) {
  print chr(ord($c) ^ $pixels[$i]) ;
  $i++;
}
print "\n";
```

We XOR the values together and convert the bytes to their ascii equivalent characters
and get the flag:

flag{st4r_w4rs_1s_b35t_:D}

We convert it to easy cft and get:

*easyctf{st4r_w4rs_1s_b35t_:D}*


