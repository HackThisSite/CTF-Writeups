#Verticode

Welcome to Verticode, the new method of translating text into vertical codes.

Each verticode has two parts: the color shift and the code.

The code takes the inputted character and translates it into an ASCII code, and then into binary, then puts that into an image in which each black pixel represents a 1 and each white pixel represents a 0.

For example, A is 65 which is 1000001 in binary, B is 66 which is 1000010, and C is 67 which is 1000011, so the corresponding verticode would look like this.

Except, it isn't that simple.

A color shift is also integrated, which means that the color before each verticode shifts the ASCII code, by adding the number that the color corresponds to, before translating it into binary. In that case, the previous verticode could also look like this.

The table for the color codes is:

0 = Red
1 = Purple
2 = Blue
3 = Green
4 = Yellow
5 = Orange

This means that a red color shift for the letter A, which is 65 + 0 = 65, would translate into 1000001 in binary; however, a green color shift for the letter A, which is 65 + 3 = 68, would translate into 1000100 in binary.

Given this verticode, read the verticode into text and find the flag.

Note that the flag will not be in the typical sctf{flag} format, but will be painfully obvious text. Once you find this text, you will submit it in the sctf{text} format. So, if the text you find is adunnaisawesome, you will submit it as sctf{adunnaisawesome}.

## Solution overview

In this challenge we need to find a decent image library to use, in order to inspect the different pixels in the image we have to decode. I am using perl and for this I will use the library **Imager**. You can find a suitable image library for your favorite programming language.

1) Determine pixel positions
2) Determining the logic of our program
3) Code
4) Running code and interpreting the result

## Determine pixel positions

Before we start the programming, we need to determine the pixel positions for the different parts of the image. For this task I use **gimp** , you can use whatever program suits you.

In order to parse all the image parts we need the following measurements

1) Height of the Verticode
2) Bit pattern start position X axis.
3) With of each "bit" in the bit pattern section.

Once we have these measurements, we can move on.

## Determining the logic of our program

We got the measurements which we will use in our algorithm, so now we need to quickly sketch up our program logic.

1) Handle command line arguments, we intend to run our program like **./decode.pl <verticode.png>**
2) Traverse the input image's pixels, from y=0 to y< height of image. Each step being the height of the verticode.
3) Get the color of the shift value and look it up to get the integer value associated with it.
4) Go through all bits in the bit pattern part and determine the color/value of each.
5) translate the bit pattern consisting of all the bits from bullet 4, into an integer value
6) Subtract the shift value from bullet 3 from our bit pattern integer and print out the ascii equivalent.


## Code

```
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

```


## Running code and interpreting the result

Now we run our code

`./decode.pl code1.png`

And we get the following result, I added line breaks for brevity

```
JoeLopowasamanofmildtemperamentshortstatureandhadthegoaltobecometheworlds
fastesttelephoneeaterThoughLoponeverknewevenbasicphysicshecreatedatelescope
capableofsightingthesmallesthaironanalienwholivedquiteafewlightyearsaway
JoeLopoquicklydestroyedalargeboulderandusedtheshatteredremainstoformeight
smallstatuesthatstronglyresembledtinycreaturesbeingorrelatedtothewaterflea
Heplacedtheminacircularpatterntoformasortofshrineandplacedthetelescopeinthe
middleofitHethenchanneledthepowerofthestonewaterfleasintothetelescopetoview
thepoweroftheheavensHewasinatrancewiththebeautyofthemysteriousdimensionand
didntevennoticetheverylargetornadoheadingtowardhimTheshrinewasquicklydemolished
andtheimmediatewithdrawlofpowersentJoeLobointoalairofpitchblacknessfoundtobea
paralleldimensionthatcausABCiamtheflagalllowercasenojokeDEFanyonewhosefirstname
beganwithJalongwithMLandQtobecomeratheruncomfortableJoewasalsosuddenlyintroduced
toundroclamaticolomphasisciousytheeccentrictapewormwithastrongmorrocanaccent
ImundroclamaticolomphasisciousytheeccentrictapewormIlikepizzasohowareyadoin
IhavenoideasaidJoe
```

Reading the text, which is about telescopes and aliens, you quickly see that there are odd out of place uppercase characters in the bottom part of the text.

Between ABC and DEF, you can see the flag: *iamtheflagalllowercasenojoke*

Insert it into the flag template and you get:


**sctf{iamtheflagalllowercasenojoke}**
