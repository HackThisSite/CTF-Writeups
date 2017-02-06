# SC1: Math bot

100 points
> It is well known that computers can do tedious math faster than human.
>
> `nc 195.154.53.62 1337`

## Solution

When connection to the ip/port , we get a welcome banner and the following
instructions:

```

Our system system has detected human traffic from your IP!
Please prove you are a bot
Question  1 :
32303143160037726535237726790459 + 55153352394171285161776505945632 =

```

From this we can see that we need to calculate the answer to the math problem
and it seems we need to use something that can handle big numbers!

To solve the mission, I choose to use perl and the bigint module


```perl
#!/usr/bin/perl

use IO::Socket::INET;
use bigint;
$| = 1;

my ($socket,$client_socket);

$socket =  IO::Socket::INET->new (
  PeerAddr => "195.154.53.62",
  PeerPort => "1337",
  Type     => SOCK_STREAM,
  Proto => "tcp",
) or die "ERROR no socket created :( $!\n";

print "Connected to the mofo.\n";

my $html = "";
my $buffer = "";

while ( my $line = <$socket> ) {
  print $line;
  chomp $line;
  if ( $line =~ /(.*?)\s?=$/) {
     my $result = eval($1);
     print $socket $result . "\n";
  }
}

```

The perl program is pretty straight forward, we read one line at
at time from the socket and check if it ends with a "=", its a crude
test but its all we need.

We evaluate the line we get (excluding the "=") and get the result,
which we send back, and continue this way untill we get

```
Well no human got time to solve 500 ridiculous math challenges
Congrats MR bot!
Tell your human operator flag is: ALEXCTF{1_4M_l33t_b0t}
````




