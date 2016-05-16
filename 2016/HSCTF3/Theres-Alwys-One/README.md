# There's always one

You know what to do: **jeaud_squiqh_syfxuh_fherbuc**

*hint : Cipher named after Roman dude.*

## Solution

Judging from the hint, the cipher used is the Ceasar Cipher, which produce the ciphertext by shifting the letters in the cleartext a set number of times.

To solve this we will make a perl program to go through each character in the cipher and shift it n places. We repeat the shiftin steps length(alphabet) times.
We will visually inspect the result and choose the cleartext that gives most meaning to us.

## Program

The program to solve this is straight forward, we start by defining out alphabet, which in this case are the letters from a to z.

We go through each letter in the ciphertext and check if it within our alphabet or not, if it, by being shiftet, goes beyond out alphabet, it starts back at the first letter of the alphabet.

We repeat these shift through the length of our alphabet, to get lines with number of shifts and what clear text that produced.


```
Shifted 1 => kfbve_trvjri_tzgyvi_gifscvd
Shifted 2 => lgcwf_uswksj_uahzwj_hjgtdwe
Shifted 3 => mhdxg_vtxltk_vbiaxk_ikhuexf
Shifted 4 => nieyh_wuymul_wcjbyl_jlivfyg
Shifted 5 => ojfzi_xvznvm_xdkczm_kmjwgzh
Shifted 6 => pkgaj_ywaown_yeldan_lnkxhai
Shifted 7 => qlhbk_zxbpxo_zfmebo_molyibj
Shifted 8 => rmicl_aycqyp_agnfcp_npmzjck
Shifted 9 => snjdm_bzdrzq_bhogdq_oqnakdl
Shifted 10 => token_caesar_cipher_problem
Shifted 11 => uplfo_dbftbs_djqifs_qspcmfn
Shifted 12 => vqmgp_ecguct_ekrjgt_rtqdngo
...

```

We can se in the list produced, that shifting the alfabet 10 times, we end up with the tekst *token_caesar_cipher_problem* which is also our flag.


```
#!/usr/bin/perl

my $filename = $ARGV[0];


unless ( -e $filename) { usage(); exit(0); }

open my $fh,"<$filename" or die "Error opening ciphertext file $0!\n";

my $ciphertext = join "",<$fh>;
$ciphertext = lc($ciphertext);

print "Ciphertext: \n";
print $ciphertext;
print "\n";

my @alphabet = ("a" .. "z");

my $hashMap = {};

for (my $i=0;$i<scalar(@alphabet);$i++) {
  $hashMap->{$alphabet[$i]} = $i;
}

my @chars = split "",$ciphertext;

for (my $shift=1;$shift<scalar(@alphabet);$shift++) {
  print "Shifted $shift => ";
  foreach my $c (@chars) {
     if ( defined($hashMap->{$c}) && ( $hashMap->{$c} < scalar(@alphabet)-$shift)) {
        print $alphabet[ $hashMap->{$c} + $shift  ];
     }
     elsif (defined($hashMap->{$c})) {
        my $remainder =   $hashMap->{$c} - (scalar(@alphabet)-$shift) ;
        print $alphabet[$remainder];
     }
     else {print $c;}
  }

}

sub usage {
  print "\n";
  print "Usage: \n";
  print "\t $0 <filename>\n";
  print "\n";
}


```

## Flag

*token_caesar_cipher_problem*
