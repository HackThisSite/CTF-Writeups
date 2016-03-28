# Rock with the wired shark!
 > Description: Sniffing traffic is fun. I saw a wired shark. Isn't that strange? 

> Service: downloadable zip, containing dump of pcap.

## Solution

For this one you need to open the dump.pcapng in wireshark
 > File->Open

You get a listing of various packets, we are interested in the http ones,
before we analyze them, we will check if we can export any datafiles from
the stream of packets.

 > File->Export Objects-> Http

This gives us a list of files that can be re-created from the http packets
one in particular catches out eyes!

> flag.zip

We save this, clicking "Save As".

To our sadness, the zip file is password protected, so what now???

Lets check out the http packet where we request the zip file, lets see if
there are more hints there.  Its packet number 61.

Here we can see that the request comes with a Auth Basic header

> Authorization: Basic ZmxhZzphenVsY3JlbWE=

Wireshark is nice to us and "decrypt" the username:password pair, so you can 
click on the + to expand the header field and get the username and password

> flag:azulcrema

If wireshark hadn't been friendly to you, you could just use the linux command

> base64 -d

And then enter in the ZmxhZzphenVsY3JlbWE= string.

You can now open the zip file with the password "azulcrema", you get a txt file which
contain the flag!!

> IW{HTTP_BASIC_AUTH_IS_EASY}

