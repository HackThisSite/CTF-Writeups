#Coffee Maker
>Make an Espresso

**Hint:** *The coffee maker uses SHA-1 to authenticate users.*

The first thing I did was play around with the forms...

![forms](https://github.com/HackThisCode/CTF-Writeups/tree/master/2016/LASA-CTF/Coffee-Maker/coffee.png "Forms")

As you can see, we have some coffee's we can make on the fly. However, we have some that require a 15 character password.
This means that brute-force isn't an option.

Below is a snippet of code pulled from the source. This shows us the three coffee's we can make on the fly, and what their hash values actually are. This is important, as the validation process involves the URI plus the hash.
If the URI matches for a specific Hash, then the request will be sent, otherwise it will never be processed...

An example: `http://web.lasactf.com:14339/brew.php?type=latte&auth=c037b03d65549eaf05607832dae18f26c602d583`

When this request gets sent off, the server checks the URI `/brew.php?type=latte` and then it determines if `&auth=<hash>` is a valid hash for the request.

**Code Snippet:**
```
<script>
    $('#unauth').submit(function (evt) {
      evt.preventDefault();
      hashes = {
        "latte":"c037b03d65549eaf05607832dae18f26c602d583",
        "americano":"5e3ece3a886d5ff19ca157b9f79180f8759f524b",
        "mocha":"85a3db488dfed277198a8c031db5e6ad865d4637"
      };
      var select = document.getElementById("unauthed-select");
      var type = select.options[select.selectedIndex].value;
      window.location = './brew.php' + '?type=' + type + '&auth=' + hashes[type];
    });
    $('#auth').submit(function (evt) {
      evt.preventDefault();
      var select = document.getElementById("authed-select");
      var type = select.options[select.selectedIndex].value;
      var password = document.getElementById("password").value;
      //Hash is generated from password + URI
      var hash = CryptoJS.SHA1(password + '/brew.php?type='+type);
      //Make sure password is correct length
      if (password.length == 15){
        window.location = './brew.php' + '?type=' + type + '&auth=' + hash;
      }
      else{
        var group = document.getElementById("passsword-group");
        group.classList.add('has-error');
        group.classList.add('has-feedback');
        document.getElementById("password-label").innerHTML = "Password must be 15 characters long";
      }
    });
  </script>
  ```

  The exploit:
  >The attack
An application is susceptible to a hash length extension attack if it prepends a secret value to a string, hashes it with a vulnerable algorithm, and entrusts the attacker with both the string and the hash, but not the secret. Then, the server relies on the secret to decide whether or not the data returned later is the same as the original data.
It turns out, even though the attacker doesn't know the value of the prepended secret, he can still generate a valid hash for {secret || data || attacker_controlled_data}! This is done by simply picking up where the hashing algorithm left off; it turns out, 100% of the state needed to continue a hash is in the output of most hashing algorithms! We simply load that state into the appropriate hash structure and continue hashing.

>*TL;DR: given a hash that is composed of a string with an unknown prefix, an attacker can append to the string and produce a new hash that still has the unknown prefix.*

[Source](https://blog.skullsecurity.org/2012/everything-you-need-to-know-about-hash-length-extension-attacks)

[This ShmooCon talk](https://youtu.be/j3wXitDweC4?t=1404) explains more about the process of hash extension attacks.

There are a few tools designed to exploit this type of vulnerability
+ [HashPump](https://github.com/bwall/HashPump) - *A tool to exploit the hash length extension attack in various hashing algorithms - C++*
+ [Hash Extender](https://github.com/iagox86/hash_extender) - *A tool to exploit the hash length extension attack in various hashing algorithms - C*
+ [hlextend](https://github.com/stephenbradshaw/hlextend) - *Pure Python Hash Length Extension module - Python*

I opted to solve this challenge by writing a quick Python program. Using the `hlextend` module, I created a fully functioning solution to the challenge.

[espresso.py](https://github.com/HackThisCode/CTF-Writeups/tree/master/2016/LASA-CTF/Coffee-Maker/espresso.py)

```
import hlextend
import urllib
import requests

ext_attack = hlextend.new('sha1')
type = 'americano';
t = '/brew.php?type='+type;
expand_query = ext_attack.extend('&type=espresso', t, 15, '5e3ece3a886d5ff19ca157b9f79180f8759f524b').replace('\\x', '%')

print expand_query + "\n" + ext_attack.hexdigest() + "\n"

url  = "http://web.lasactf.com:14339";
query = expand_query + "&auth="+ ext_attack.hexdigest();
url  = url + query;

resp = requests.get(url);
print resp.text;
```

Running the program, we get a successful little message in our response!

`A note was left on the receipt: lasactf{3xt3nding_l3ngth}`
