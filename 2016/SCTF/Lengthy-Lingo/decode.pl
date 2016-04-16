#!/usr/bin/perl

my $filename = $ARGV[0];

unless (-e $filename) {usage();exit(0);}

open my $fh,"<$filename" or die "Error opening file $filename!\n";


my $content = join "",<$fh>;
chomp $content;


decrypt($content);




sub decrypt {
  my $content = shift;

  my @parts = split /,/,$content;

  foreach my $p (@parts) {
    $p =~ s/\s+//g;
    print chr(length($p));
  }

}









sub usage() {
  print "\n";
  print "Usage: \n";
  print "\t$0 <encrypted-file>\n";
  print "\n";
}
