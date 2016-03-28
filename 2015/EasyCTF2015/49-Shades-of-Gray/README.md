Description:
Solved by 363 teams.

We only have 49 shades of gray D:

`#000000` to `#F5F5F5`... there's one shade missing! Find the hex value of the missing shade. Pound sign optional.

![50 Shades](https://github.com/Ninjex/Wargame-Writeups/blob/master/CaptureTheFlag/2015/EasyCTF2015/49-Shades-of-Gray/shades.png?raw=true "50 Shades")

This challenge was actually very simple to solve, and programming knowledge can be minimal if you use the correct tools.
Running the following command will generate a text file called `out.txt` which contains all the unique pixel colors in the given image.

`convert -unique-colors shades.png out.txt`

After we get the list, we can visually search the output and find the pixel which is missing, I did the following:

`cat out.txt | less`

Giving me the following output right off the bat (which contains our answer):
```
# ImageMagick pixel enumeration: 49,1,255,srgb
0,0: (  0,  0,  0)  #000000  black
1,0: (  5,  5,  5)  #050505  grey2
2,0: ( 10, 10, 10)  #0A0A0A  grey4
3,0: ( 15, 15, 15)  #0F0F0F  grey6
4,0: ( 20, 20, 20)  #141414  grey8
5,0: ( 25, 25, 25)  #191919  srgb(25,25,25)
6,0: ( 30, 30, 30)  #1E1E1E  srgb(30,30,30)
7,0: ( 35, 35, 35)  #232323  srgb(35,35,35)
8,0: ( 40, 40, 40)  #282828  srgb(40,40,40)
9,0: ( 45, 45, 45)  #2D2D2D  srgb(45,45,45)
10,0: ( 50, 50, 50)  #323232  srgb(50,50,50)
11,0: ( 55, 55, 55)  #373737  srgb(55,55,55)
12,0: ( 60, 60, 60)  #3C3C3C  srgb(60,60,60)
13,0: ( 65, 65, 65)  #414141  srgb(65,65,65)
14,0: ( 70, 70, 70)  #464646  srgb(70,70,70)
15,0: ( 75, 75, 75)  #4B4B4B  srgb(75,75,75)
16,0: ( 85, 85, 85)  #555555  srgb(85,85,85)
17,0: ( 90, 90, 90)  #5A5A5A  srgb(90,90,90)
18,0: ( 95, 95, 95)  #5F5F5F  srgb(95,95,95)
19,0: (100,100,100)  #646464  srgb(100,100,100)
:
```
Looking at row `15-16`, we notice it jumps and skips `( 80, 80, 80 ) #505050 srgb(80,80,80)`

This is our missing pixel: `#505050`
