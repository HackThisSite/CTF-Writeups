# A numbers game 2.
 > Description: Math is used in cryptography, but someone got this wrong. Can you still solve the equations? Hint: You need to encode your answers.

> Service: 188.166.133.53:11071 

## Solution

You get a python fragment which is the encryption algorithm that the server/service encrypts its communitation with.
From the first glance you can see that its using XOR on each character value, which tells you that it can be reversed
pretty easy.

The encode function is converted to perl and a decode function is made by basically going from the bottom of
the encode function to the top, reversing the steps done.

The server/service gives you a string like this, when you connect to it:
>Level 1.: 4.4.5.3.3.3.3.3.3.3.5.5.3.3.3.3.3.4.4.4.3.3.3.3.3.4.6.4.3.3.3.3.3.4.5.3.3.4.4.4

The last part is the encoded string, we decode this with the function we made in perl, and from this we get
a simple math problem on the form x + 1 = 21.

We have to solve the math problem AND encode it and then send that encoded string back to the server, 
in order to pass a level. There are 100 levels so this is not feasable to do manually, or semi automatic.

The perl code made also passes the simple math problems and solve them.


```perl
#!/usr/bin/perl
use IO::Socket::INET;

$| = 1;

my ($socket,$client_socket);

$socket = new IO::Socket::INET (
  PeerHost => "188.166.133.53",
  PeerPort => "11071",
  Proto => "tcp",
) or die "ERROR no socket created :( $!\n";

print "Connected to the mofo.\n";

while (my $data = <$socket>) {

  #Level 1.: 4.4.5.3.3.3.3.3.3.3.5.5.3.3.3.3.3.4.4.4.3.3.3.3.3.4.6.4.3.3.3.3.3.4.5.3.3.4.4.4
  if ( $data =~ /Level (\d+).:\s([\d\.]+)/ ) {
    my $level = $1;
    my $data = $2;

    # x * 14 = 84
    my $math = decode($data);

    $math =~ /([\dx]+) ([\+\-\*\/]) ([\dx]+) = ([\d+-]+)/;
    my $first = $1;
    my $op= $2;
    my $second = $3;
    my $res = $4;

    my @items = split / /,$math;

    print "Level $level: $data | $math\n";
    print "Math operand $op\n";

    my $actionInt = 0;
    if ( $first eq "x" ) { $actionInt = $second; }
    else {$actionInt = $first;}

    my $result = "";
    if    ($op eq "*" ) {  $result = $res / $actionInt;  }
    elsif ($op eq "/" ) {  $result = $res * $actionInt;  }
    elsif ($op eq "-" ) {  $result = $res + $actionInt; }
    elsif ($op eq "+" ) {  $result = $res - $actionInt; }

    print "Result: " . $result . "\n";

    my @parts = split //,$result;
    my @enc = ();

    foreach my $p (@parts) {
      my $e = encode($p);
      push @enc,$e;
    }

    $" = ".";
    my $encString = join ".",@enc;
    print "Encoded: " . $encString . "\n";
    print $socket "$encString\n";
  }
  else {
   print ">> $data\n";
  }
}

sub decode {
  my $encStr = shift;

  my @elms = split /\./,$encStr;
  my $nrChars = (scalar @elms) / 4;

  my @pairs = ();
  foreach my $e (@elms) {
    my $ord  = ord($e) - 51;
    my $bin = dec2bin($ord);
    $ord = ( length($bin)==1?"0".$bin:$bin);
    push @pairs,$ord;
  }

  my $b = join "",@pairs;
  my @chars = ( $b =~ m/.{8}/g );

  my $decoded = "";

  foreach my $byte (@chars) {
    $byte =~ s/^1/0/;
    my $int = bin2dec($byte); # this is the xor 32 result
    my $chres =  $int ^ 32;
    $decoded .= chr($chres);
  }

  return $decoded;
}


sub encode {
   my $eq = shift;
   my @out = ();

   my @chars = split //,$eq;

   foreach my $c (@chars) {
     my $xorRes =  ord($c) ^ 32;
     my $bin = to_binary($xorRes);
     push @out,$bin;
   }

   my $b = join //,@out;
   my @pairs = ( $b =~ m/../g );

   my @pr = ();
   foreach my $p (@pairs) {
     my $chr = chr(bin2dec($p)+51);
     push @pr,$chr;
   }

   return join ".",@pr;
}


sub to_binary {
  my $int = shift;
  my $bin = sprintf ("%b",$int);
  my $res = "0" x (8-length($bin)) . $bin;
  return $res;
}

sub bin2dec {
  return unpack("N", pack("B32", substr("0" x 32 . shift, -32)));
}

sub dec2bin {
    my $str = unpack("B32", pack("N", shift));
    $str =~ s/^0+(?=\d)//;   # otherwise you'll get leading zeros
    return $str;
}
```

