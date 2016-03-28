# It's Prime Time!
 > Description: We all know that prime numbers are quite important in cryptography. Can you help me to find some?

> Service: 188.166.133.53:11059

## Solution
To solve this challenge, you need to send the next prime number after the number the server presents to you. You have to solve 100 primes, before the server reutrns the flag to you.
```perl
#!/usr/bin/perl
#  188.166.133.53 11059

use IO::Socket::INET;

$| = 1;


my ($socket,$client_socket);

$socket = new IO::Socket::INET (
  PeerHost => "188.166.133.53",
  PeerPort => "11059",
  Proto => "tcp",
) or die "ERROR no socket created :( $!\n";

print "Connected to the mofo.\n";

while (my $data = <$socket>) {

  if ( $data =~ /Level (\d+).*?(\d+):/ ) {
   my $level = $1;
   my $after = $2;

   my $nextPrime = 0;

   for (my $i=$after+1;;$i++) {
     if ( testPrime($i) ) { $nextPrime = $i; last;}
   }

   print "Level: $level, After: $after ($nextPrime)\n";
   print $socket "$nextPrime\n";

  }
  else {
   print ">> $data\n";

  }
}

print "DONE\n";


sub testPrime
{
  my $m = shift @_;
  my $i = 2;
  while ($i < $m)
  {
    return 0 unless ($m % $i++);
  }
  return 1;
}
```

Flag: `IW{Pr1m3s_4r3_!mp0rt4nt}`

