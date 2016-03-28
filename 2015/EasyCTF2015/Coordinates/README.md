Description:
```
We found this text lying around, but apparently it doesn't do anything. Want to give it a shot?
```
We also get an additional hint:
```
Do you like painting?
```
We need to draw a picture using the coordinates in the text file. Each pair enclosed in parentheses denotes the x and y coordinates of a pixel. The ```qr.rb``` script takes care of parsing the data and then writing the image.
Now all that is left is to decode the QR code with a phone app or an online reader such as http://zxing.org.
The flag is: ```easyctf{bet_y0u_read_that_wiki_page}```
