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
#  print $result . "\n";

  if ( $result =~ /\s+extracting:\s+(.*?)\s*\R/gi ) {
    $zipFile = $1;
  }
  else {
    last;
  }

  print $number . ":" . $password . "\n";
  print $fh $number . ":" . $password . "\n";

}

close $fh;
