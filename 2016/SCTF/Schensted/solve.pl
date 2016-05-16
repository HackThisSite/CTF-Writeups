#!/usr/bin/perl


my $filename = $ARGV[0];

unless (-e $filename) { usage(); exit 0; }

open my $fh,"<$filename" or die "Cant open file $filename!\n";

my $file = join "",<$fh>;
chomp $file;

my @digits = split "",$file;
$file = "";

my $max = 0;

my $currentMax = 0;
my $last = "-";
foreach my $d (@digits) {

  if ( $last eq "-") {
    $last = $d;
    $currentMax++;
    next;
  }

  if ( $last >= $d ) {
   $currentMax++;
  }
  else {
   if ($currentMax > $max ) { $max = $currentMax;}
   $currentMax = 0;   
  }
 
  $last = $d;
}


print "Max: " . $max . "\n";

















sub usage() {

  print "\n";
  print "Usage: \n";
  print "\t$0 <filename>\n";
  print "\n";

}
