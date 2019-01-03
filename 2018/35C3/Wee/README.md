# Wee

> Good coders should learn one new language every year.
> InfoSec folks are even used to learn one new language for every new problem they face (YMMV).
> If you have not picked up a new challenge in 2018, you're in for a treat.
> We took the new and upcoming `Wee` programming language from paperbots.io. Big shout-out to Mario Zechner (@badlogicgames) at this point.
> Some cool Projects can be created in Wee, like:
> [this](https://paperbots.io/project.html?id=URJgCh),
> [this](https://paperbots.io/project.html?id=kpyyrl) and
> [that](https://paperbots.io/project.html?id=F53thj).
> Since we already know Java, though, we ported the server (Server.java and Paperbots.java) to Python (WIP) and constantly add awesome functionality. Get the new open-sourced server at `/pyserver/server.py`.
> Anything unrelated to the new server is left unchanged from commit `dd059961cbc2b551f81afce6a6177fcf61133292` at badlogics paperbot github (mirrored up to this commit here).
> We even added new features to this better server, like server-side Wee evaluation!
> To make server-side Wee the language of the future, we already implemented awesome runtime functions. To make sure our VM is 100% safe and secure, there are also assertion functions in server-side Wee that you don't have to be concerned about.

35C3 featured plenty challenges using the same application. Most of them were
placed in the *Misc* category. They all shared a part of their description and
overlapped to some degree.

## List of challenges

### Web

- DB Secret
- localhost
- Logged in
- NOT IMPLEMENTED

### Misc
- /dev/null
- Conversion Error
- Equality Error
- Layers
- Number Error
- Wee R Leet
- Wee Token

### Crypto
- Decrypted

## Analysis

### Source

Following the hint included in the description we can find the
[server.py](server.py) file as well as the source of the program used to
evaluate Wee on the server - [weeterpreter.ts](weeterpreter.ts).

### Running Wee

To execute Wee code on the server wee need to send it formated in json to the
appropriate endpoint. To recieve any output we need to print it using
`alert(string)`.

Example:

```
liquid$> curl -X POST http://35.207.132.47/wee/run -d '{ "code": "alert(\'hello world\')" }
{"code":"alert(\"hello world\")","result":"hello world\n"}
```

### Notes

While the server doesn't require much comment there are a few things to note in
the interpreter source. It runs code inside a Chromium instance using the
[Puppeteer](https://github.com/GoogleChrome/puppeteer) library. The file also
contains a few special functions used in further challenges. Among them is the
`eval` function which evaluates *Java Script* in context of the browser.
