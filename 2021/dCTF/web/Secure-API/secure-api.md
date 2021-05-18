Challenge: Secure API
<br>
Points: 200
<br>
Category: Web
<br>
Objective: Go to the given URL and get the flag
<br>

Process to find the flag: Okay so this was definitely a hard challenge, I couldn’t even do it alone my teammate helped a lot in this, so basically in this you didn’t had to change any coding or anything you had to send request to the URL, and for that we used Rested By Espen H.
Google extension: https://chrome.google.com/webstore/detail/rested/eelcnbccaccipfolokglfhhmapdchbfg

Firefox extension: https://addons.mozilla.org/en-US/firefox/addon/rested/
So this tool allows us to modify our request really easily.

So my teammate is smarter and more experienced than me so he already knew that we need to make a POST request to the URL, while trying to log in with guest credentials as said when we try to open the given URL.
One thing to be noticed that the POST request is made to http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/login and not to http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/ and this is because we are trying to login as guest, and most of the times the login request goes to /login so we tried that first and it worked. 
We tried the most easiest credentials to log in as guest and they worked.
 
After making this request we got this result, we realized that it’s a JWT token because of the two dots(periods) in between.
 
As we realized that it’s a JWT token we quickly decided to use John The Ripper (https://github.com/openwall/john) to find its secret key.
We needed to find its secret key to change the token and make a Get request at http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/ as an admin, because that was the only thing that we could think of.
But we make a slight mistake here and we edited the token first and changed its value to admin before finding its secret key.

Token before editing:  
Token after editing:  

So as edited it first it we got cracked its wrong secret key and it didn’t work, so then we made the POST request again, got the token and this time we cracked its 256 bit key first.

To crack they key we used John The Ripper and this is how we cracked it.
First we added the token in a file.
 
 

Then we used John The Ripper with rockyou.txt wordlist which can be downloaded from the internet, we also specified the format of the JWT token which can be found from here  

This is what we got from John The Ripper, the secret key which is 147852369
 

Then we used this secret key to modify the token.
All we changed was just the username and we added the secret key
 

Now we used this token to make a GET request.
First we tried this
 
It didn’t work so it made us doubt ourselves where could we have been wrong, then we realized that when we got the token by making the POST request the token had ‘Bearer’ in front of it, so here also we added Bearer in front of the token, and then we got this response
 

The flag: dctf{w34k_k3y5_4r3_n0t_0k4y}
