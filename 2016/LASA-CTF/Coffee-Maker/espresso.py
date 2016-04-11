#!/usr/bin/python
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
