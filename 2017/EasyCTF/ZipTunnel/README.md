# Zip Tunnel

Great blazes! Something looks awfully suspicious about this zip file. Can you find out just how deep the rabbit hole goes?

*Hint: Whenever I go to Subway, I get double ham, wamerican, bacon, lettuce, and mayo. No frills.*

## Solution

We are presented with a password protected zip file, so we immediately try to bruteforce it with
a dictiontary we got handy. We use the rockyou dictionary for this and we crach the password.

But we are then presented with another zip file, which is also password protected :O. 
* a pattern emerges *

We will build a script to take care of cracking any further zip files, as we can see by now
that we likely have to crack 420 zip files all in all.

We will use some perl-fu and produce the following program


```
#!/usr/bin/perl

my $JOHN_PATH = "./john/run";
my $JOHN_WORDLIST = "./american-english-insane.txt";

my $zipFile = $ARGV[0];

open my $fh,">./pwdlist.txt" or die "Cant open pwdlist.txt for writing!\n";

unless ($zipFile =~ /^level\d+\.zip$/) {
  print "Make sure the INITIAL zipfile is called level420.zip, rename and try again!\n";
  print "You can use this tool starting from whatever zip file levelxxx.zip,\n";
  print "but the initial file must be called level420.zip!\n";
  exit 0;
}

unless ( -e $zipFile) {die "Zip file not found\n";}
unless ( -e $JOHN_PATH . "/john") {die "john executable not found, please change \$JOHN_PATH\n";}
unless ( -e $JOHN_PATH . "/zip2john") {die "zip2john executable not found, please change \$JOHN_PATH\n";}

while (42) {

  my ($number) = ($zipFile =~ /(\d+)/);
  my $password = "";

  my $cmd = "$JOHN_PATH/zip2john level" . $number . ".zip 2>/dev/null > ./zip.hash";
  `$cmd`;

  $cmd = "$JOHN_PATH/john --wordlist=$JOHN_WORDLIST ./zip.hash";
  `$cmd`;

  $cmd = "$JOHN_PATH/john --show ./zip.hash";
  my $result = `$cmd`;

  if ( $result =~ /^level\d+\.zip\:(.*?)\n/gis ) {
    $password = $1;
  }

  $cmd = "unzip -o -P" . $password . " level" . $number . ".zip";
  $result = `$cmd`;

  if ( $result =~ /\s+extracting:\s+(.*?)\s*\R/gi ) {
    $zipFile = $1;
  }
  else {
    last;
  }

  print $number . ":" . $password . "\n";
  print $fh $number . ":" . $password . "\n";

}
```

We rename the initial zip file to level420.zip and run the program, we however find pretty
quickly that our choosen wordlist/disctionary was not up to task cracking any more passwords.

We ponder this for a while and read the hint, which has something about wamerican, which one
of our team mates remembers there is a debian package with that name, which holds the
american-english-insane.txt dictionary.

Using this, we quite quickly crack the rest of the passwords, except the very last level0.zip,
which doesnt seem to answer to either dictionary attacks or bruteforce in a resonable time.

We make one last desperate attpept to take all words from the CTF page, initially we only 
thought of taking the words in the hint but we opted for taking all words from the ctf site
and make it into a dictionary.

We run john the ripper again with the new dictionary against level0.zip and bingo, it happily
opens op to spill its secrets to us.

The last password was: *easyctf*

Unzipping level0.zip gives us a file called flag.txt which contain

```
Congratulations, you've made it to the bottom of the zip tunnel! I've got a flag for you: easyctf{x4m1n3_uR_z1pp34_PDq_17c4ee3}
```

Case closed!!

