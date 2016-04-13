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

  my $filename = shift;
  my $CODEHEIGHT = 12; # what height in pixels is each band in the image
  my $BITPATTERNSTART = 84;
  my $BITPATTERNWIDTH = 12;

  my $img = Imager->new(file=>$filename) or die Imager->errstr();

  my $width  = $img->getwidth();
  my $height = $img->getheight();

  my $COLORSHIFT = {
                   "255,0,0"   => 0,   # rED
                   "128,0,128" => 1,   # Purple
                   "0,0,255"   => 2,   # bLUE
                   "0,128,0"   => 3,   # Green
                   "255,255,0" => 4,   # Yellow
                   "255,165,0" => 5,   # Orange

                 };

  my @COLORNAMES = ("RED","PURPLE","BLUE","GREEN","YELLOW","ORANGE");

  my $vertString = "";

  for ( my $i=0; $i<$height; $i+=$CODEHEIGHT ) {

    my $shiftPixelColor = $img->getpixel(x=>1,y=> $i);
    my ($r,$g,$b,$a) = $shiftPixelColor->rgba();

    my $pixelColorString = "$r,$g,$b";
    my $shiftValue = $COLORSHIFT->{$pixelColorString};


    my $bitPattern = "";

    for ( my $j=$BITPATTERNSTART ; $j < $width; $j+=$BITPATTERNWIDTH ) {
      my $bitColor = $img->getpixel(x=>$j,y=> $i);
      my ($br,$bg,$bb,$ba) = $bitColor->rgba();
      my $bcString = "$br,$bg,$bb";
      my $bit = $bcString eq "0,0,0"?"1":"0";
      $bitPattern .=  $bit;
    }

    my $x_num = oct("0b0". $bitPattern);
    my $shiftedChar = $x_num -$shiftValue;
    $vertString .= chr($shiftedChar);

  }

   return $vertString;
}

