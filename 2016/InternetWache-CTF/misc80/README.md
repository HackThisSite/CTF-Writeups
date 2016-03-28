# 404 Flag not found
 > Description: I tried to download the flag, but somehow received only 404 errors :( Hint: The last step is to look for flag pattern. 

> Service: downloadable zip, containing dump of pcap.

## Whats cooking?

From the pcap file (we open it in wireshark and browse about).
And here we can see an unusual amount of dns queries taking place.

They are all in the format of:
> ([A-Za-z0-9]+)\.2015.ctf.internetwache.org

Where the first part are random nonsense which at first glance looked like a-z0-9, but it is really
hexadecimal numbers, each pair representing an ascii code (oii where are we going with this).

## Are you ASCII'ing me?

To extract the wierd ascii hex parts of the domain queries, our friend perl is always helpful,
but to make it easier we convert the pcap file to plain text so its easier on the eyes (yes perl got eyes).

> tcpdump -r flag.pcapng > captxt.txt

## Perl incomming

```perl
#!/usr/bin/perl

my $file = $ARGV[0];
open FIL,"<$file" or die "File not found\n";

while (my $line = <FIL> ) {
  if ( $line =~ /([A-Za-z0-9]+)\.2015.ctf.internetwache.org/ ) {
    my $hexStr = $1;
    my @array = ( $hexStr =~ m/../g );
    foreach my $ch (@array) {
     my $dec = hex ("0x" . $ch);
     print chr($dec);
    }
  }
}

```


# Mad Poem

After running the perl program with the captxt.txt as the first argument you are left with the following
poem, which you further have to de-obfuscate, in order to get the flag out.

> In the end, it's all about flaIn the end, it's all about flags.
> Whether you win or lose dogs.
> Whether you win or lose doesn't matter.
> {Ofc, winning isesn't matter.
> {Ofc, winning is cooler
> Did you find other fla cooler
> Did you find other flags?
> Noboby finds other flags!
> gs?
> Noboby finds other flags!
> Superman is my hero.
> _HERO!!!_Superman is my hero.
> _HERO!!!_
> Help me my friend, I'm lost i
> Help me my friend, I'm lost in my own mind.
> Always, always,n my own mind.
> Always, always, for ever alone.
> Crying until  for ever alone.
> Crying until I'm dying.
> Kings never die.
> SoI'm dying.
> Kings never die.
> So do I.
> }!
> do I.
>}!

I don't remember how to reduce the poem but look at parts if the flag IW{} in there and 
you'll find it. Maybe someone else can write that part.

