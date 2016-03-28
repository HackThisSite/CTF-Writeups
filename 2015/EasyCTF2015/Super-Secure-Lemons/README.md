Description: Solved by 776 teams.
This [site](https://web.easyctf.com:10202/) uses an encryption technology to keep its lemons super secure! On second thought, it might not be as secure as we thought.

Out of curiosity, we clicked the [link](https://web.easyctf.com:10202), which showed us following error on Chromium (same in Google Chrome).
![alt text][image]

Digging through the information, we see a line which says "its security certificate is not trusted by your computer's operating system.". We began examining the site's security certificates' information.See [Tips](#tips)
Digging more information about the site, we found that the site had self-signed certificate and the Organizational Unit (OU) to which it was issued to/by gave us the flag.
![alt text][cert]


The flag was: `easyctf{never_trust_se1f_signd_certificates}`


### Tips ###
To view certificate information of a site on Google Chrome/Chromium, follow these steps:

1. Open a site on Google Chrome/Chromium
2. In the address bar in the top left, click the lock icon or page icon.
3. Click **Connection** tab.
4. Click **Certificate Information**

[image]: ./images/privacy_error.png "Privacy Error"
[cert]: ./images/certificate_det.png "Certificate Details"
