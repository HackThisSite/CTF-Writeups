#!/usr/bin/perl

use Imager;

my $filename = $ARGV[0];

unless (-e $filename ) {usage(); exit(0);}


my $CODEHEIGHT = 12; # what height in pixels is each band in the image	
my $BITPATTERNSTART = 84;
my $BITPATTERNWIDTH = 12;


my $img = Imager->new(file=>$filename) or die Imager->errstr();

my $width  = $img->getwidth();
my $height = $img->getheight();


print "Image information \n";
print "\tWidth  : $width\n";
print "\tHeight : $height\n";

my $COLORSHIFT = { 
                   "255,0,0"   => 0,   # rED
		   "128,0,128" => 1,   # Purple                   
		   "0,0,255"   => 2,   # bLUE
		   "0,128,0"   => 3,   # Green		
	           "255,255,0" => 4,   # Yellow
                   "255,165,0" => 5,   # Orange

		 };

my @COLORNAMES = ("RED","PURPLE","BLUE","GREEN","YELLOW","ORANGE");


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

  print chr($shiftedChar) . "";


}


sub usage {

  print "\n";
  print "Usage: \n";
  print "\t $0 <imagefile to decode>\n";
  print "\n";

}

