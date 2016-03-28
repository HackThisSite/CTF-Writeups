Description: Solved by 521 teams.
```
mystery1 - mystery2
```
The hint we get is:
```
Did you know you can do math on images?
```
This problem could be solved in a number of ways. The easiest one of them was to use ```composite```.
```
composite mystery1.png mystery2.png -compose difference out.png
```
This command generates an image that contains the difference between the pixels in the two given files.
The flag can be then read from the image: ```easyctf{pretty_pixel_math}```
