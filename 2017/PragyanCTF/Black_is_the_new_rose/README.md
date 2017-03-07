# Black Is The New Rose

There were two hints in this challenge. One on the website (something like "look for the black") and second at the end of the file ("seems like you are still a noobie at bash  .. Have a closer look !! ... :D  ...").

First I've taken a look at the picture looking for black. I found out, there are lines of black in the middle of the image. So I've decided to make a script to analyze them.

The script sets the number of black pixels initially to 0. Then it does the iteration over all pixels in the image and increments result $res[$yy] if it detects black (RGB 0,0,0). Those are the first 2 nested for cycles.

In the result $res are many zeros and a few numbers between 2 and 15, so it could be hex numbers.

Next iteration over result $res puts non-zero numbers to the new array $fus.

Next iteration over array $fus makes those numbers hex, producing new array $haa.

Last iteration over array $haa outputs couples of hex to browser (I used XAMPP on Windows for that).

It produces this: {ziv_gslhv_klgziz_vziirmth?}

It looks very much like the flag but is not accepted, so here comes the team work finding the right cipher. We found out it's Atbash cipher and the resulting flag is {are_those_potara_earrings?}

Done. Thank you Blackfisk for finding out it's Atbash cipher.

mooph
