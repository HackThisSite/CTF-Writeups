#Vertinet

This problem follows the same specifications as the previous Verticode problem, except that you have to solve many of them by developing a client to communicate with the server available at problems1.2016q1.sctf.io:50000. Good luck.

**The solution relys on Verticode, so for more information see that writeup**

## Solution overview

We have already completed the Verticode algorithm in the Verticode challenge, so this writeup will concentrate mostly on the network code.

First we have to connect to the server, to see what it spits out at us, to do this we issue the telnet command (you can also use nc but telnet is more often installed pr default.)

`telnet problems1.2016q1.sctf.io 50000` or

`nc problems1.2016q1.sctf.io 50000`

The server will output the following (the base64 encoded part has been shortened for brevity ).

```
<html>
 <img src='data:image/png;base64,iVBORw0KGgoAAAAjr56XhIuc3bu4NvwAAAAABJRU5ErkJggg=='></img>
<br><br>

```

The server puts it all on one line, no line break sent with the data. This is important when we program our client.

1) Connect to the server
2) Read from the server, until our buffer contains a start and and ending IMG tag.
3) Extract the base64 encoded image data, using a regular expression:
`/.*?<img src='data:image\/png;base64,(.*?)'.*?<\/img>$/gis`
4) base64 decode the data and save the image to disk using a counter to change the filename
5) Call the solveVerticode function with the filename of the saved png file.
6) Send the result of the solveVerticode function to the server and repeat after emptying the html buffer.
7) Additionally in the main loop search the buffer for the following regex: `/(sctf\{.*?\})/gis`, if its found print out the flag!

## Code

Below is the code for the Vertinet part of the solution, for more information about the solveVerticode() function please check the writeup for "Verticode"

The code is pretty self explanatory and follows the bullet points above

NB. the complete code is available in a separate file decode.pl

```
#!/usr/bin/perl

use Imager;
use IO::Socket::INET;
use MIME::Base64;

$| = 1;


my ($socket,$client_socket);

$socket =  IO::Socket::INET->new (
  PeerAddr => "problems1.2016q1.sctf.io",
  PeerPort => "50000",
  Type     => SOCK_STREAM,
  Proto => "tcp",
) or die "ERROR no socket created :( $!\n";

print "Connected to the mofo.\n";

my $html = "";
my $buffer = "";

my $imageNr = 1;

while (my $bytesRead = read($socket, $buffer, 1))
{
  $html .= $buffer;

  if ( $html =~ /.*?<img src='data:image\/png;base64,(.*?)'.*?<\/img>$/gis ) {
   my $outfilename = "output-" . $imageNr++ . ".png";
   open my $outfh,">$outfilename";
   print $outfh decode_base64($1);
   close $outfh;

   my $str = solveVerticode($outfilename);
   print $str . "\n";
   print $socket $str;
   $html = "";
  }

  if ( $html =~  /(sctf\{.*?\})/gis ) {
   print "Flag is: " . $1 . "\n";
  }
}

sub solveVerticode {

   # check the "Verticode" writeup for more on this function.
   ..
   return $vertString;
}

```

## Flag

Run the program and watch as it solves the verticodes and in the end delivers the flag to you.

####sctf{y0ub34tth3v3rt1c0d3}
