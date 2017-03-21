#!/usr/bin/perl

use Imager;
use POSIX;
use warnings;
use strict;

my $imageFile = $ARGV[0];

my $img = Imager->new(file=>$imageFile) or die Imager->errstr();
my $width  = $img->getwidth();
my $height = $img->getheight();


print "Image width: " . $width . "\n";
print "Image height: " . $height . "\n";

my $newR = Imager->new(xsize=>$width,ysize=>$height,channels=>4);
$newR->flood_fill(x=>0,y=>0,color=>'white');

my $newG = Imager->new(xsize=>$width,ysize=>$height,channels=>4);
$newG->flood_fill(x=>0,y=>0,color=>'white');

my $newB = Imager->new(xsize=>$width,ysize=>$height,channels=>4);
$newB->flood_fill(x=>0,y=>0,color=>'white');

my $newBlack = Imager->new(xsize=>$width,ysize=>$height,channels=>4);
$newBlack->flood_fill(x=>0,y=>0,color=>'white');

my $newAll = Imager->new(xsize=>$width,ysize=>$height,channels=>4);
$newAll->flood_fill(x=>0,y=>0,color=>'white');


for ( my $x = 0; $x < $width; $x++) {

  for (my $y = 0; $y < $height ; $y++) {
    my $color = $img->getpixel(x=>$x,y=>$y);
    my ($r,$g,$b) = $color->rgba;

    if ( $r ) {
      $newR->setpixel(x=>$x,y=>$y,color=>'black');
    }
    if ( $g ) {
      $newG->setpixel(x=>$x,y=>$y,color=>'black');
    }
    if ( $b ) {
      $newB->setpixel(x=>$x,y=>$y,color=>'black');
    }

    if ( (!$r) && (!$g) && (!$b)) {
      $newBlack->setpixel(x=>$x,y=>$y,color=>'black');
    }

    if ( $r && $g && $b ) {
      $newAll->setpixel(x=>$x,y=>$y,color=>'black');
    }

  }
}

$newR->write(file=>"newfile-r.png") or die $newR->errstr;
$newG->write(file=>"newfile-g.png") or die $newG->errstr;
$newB->write(file=>"newfile-b.png") or die $newB->errstr;
$newBlack->write(file=>"newfile-black.png") or die $newBlack->errstr;
$newAll->write(file=>"newfile-all.png") or die $newAll->errstr;


my $rAscii = image2ascii($newR);
my $gAscii = image2ascii($newG);
my $bAscii = image2ascii($newB);


print "Image RED ASCII : " . $rAscii . "\n";
print "Image GREEN ASCII : " . $gAscii . "\n";
print "Image BLUE ASCII : " . $bAscii . "\n";
print "\n";
print "View the image saved in newfile-g.png and scan the barcode with a barcode scanner on your cellphone\n";

sub image2ascii {
  my $img = shift;

  my $width  = $img->getwidth();
  my $height = $img->getheight();

  my $y = 0;
  my $bits = "";

  for ( my $x = 0; $x < $width; $x++) {
    my $color = $img->getpixel(x=>$x,y=>$y);
    my ($r,$g,$b) = $color->rgba;

    $bits .= "0" if ($r == 255);
    $bits .= "1" if ($r == 0);
  }

  my @bitbytes = ( $bits =~ m/\d{8}/g);
  map {$_ = chr(oct("0b".$_))} @bitbytes;

  return join "",@bitbytes;

}


