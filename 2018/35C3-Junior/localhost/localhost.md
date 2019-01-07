# Localhost

>Solves: 69

>We came up with some ingenious solutions to the problem of password reuse. For users, we don't use password auth but send around mails instead. This works well for humans but not for robots. To make test automation possible, we didn't want to send those mails all the time, so instead we introduced the localhost header. If we send a request to our server from the same host, our state-of-the-art python server sets the localhost header to a secret only known to the server. This is bullet-proof, luckily.

>http://35.207.132.47/

>Difficulty Estimate: Medium

## Analysis

This is another one of wee challenges so source code is available in /pyserver/server.py.

Mechanism for discovering LOCALHOST flag is discovered in following code:

```python

if not request.path[-3:] in ["jpg", "png", "gif"]:
        response.headers["X-Frame-Options"] = "SAMEORIGIN"
        response.headers["X-Xss-Protection"] = "1; mode=block"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Content-Security-Policy"] = "script-src 'self' 'unsafe-inline';"
        response.headers["Referrer-Policy"] = "no-referrer-when-downgrade"
        response.headers["Feature-Policy"] = "geolocation 'self'; midi 'self'; sync-xhr 'self'; microphone 'self'; " \
                                             "camera 'self'; magnetometer 'self'; gyroscope 'self'; speaker 'self'; " \
                                             "fullscreen *; payment 'self'; "
        if request.remote_addr == "127.0.0.1":
            response.headers["X-Localhost-Token"] = LOCALHOST

    return response
```

If request path does not end in "jpg", "png" or "gif" and remote address is equal to 127.0.0.1 flag is discovered.

## Solution
NOTE: Solution requires being already logged in, see (logged in writeup)[https://github.com/HackThisSite/CTF-Writeups/tree/master/2018/35C3-Junior/Logged-in]
Since it's necessary that request originates from localhost I started searching for some kind of proxying functionality in code and found "/api/proxyimage".

```python
@app.route("/api/proxyimage", methods=["GET"])
def proxyimage():
    url = request.args.get("url", '')
    parsed = parse.urlparse(url, "http")  # type: parse.ParseResult
    if not parsed.netloc:
        parsed = parsed._replace(netloc=request.host)  # type: parse.ParseResult
    url = parsed.geturl()

    resp = requests.get(url)
    if not resp.headers["Content-Type"].startswith("image/"):
        raise Exception("Not a valid image")

    # See https://stackoverflow.com/a/36601467/1345238
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(resp.content, resp.status_code, headers)
    return response

```

It requires response's Content-Type to start with image or it throws out error, but flag giving mechanism blocked gif, png and jpg files.
Luckily for us those are not only image formats, on frontpage there is svg file http://35.207.132.47/img/paperbots.svg which satisfies all our conditions.

We can try to get flag with http://35.207.132.47/api/proxyimage?url=http://127.0.0.1/img/paperbots.svg and...we get a Connection Refused error.
Perhaps it's not ran on port 80? Indeed examining source code discovers following: ```app.run(host="0.0.0.0", port=8075)```

We retry with http://35.207.132.47/api/proxyimage?url=http://127.0.0.1:8075/img/paperbots.svg and get a flag in X-Localhost-Token

35C3_THIS_HOST_IS_YOUR_HOST_THIS_HOST_IS_LOCAL_HOST

