Description: Solved by 997 teams.
Hack my friend's [website](https://www.easyctf.com/static/problems/intro-js/index.html)! From what she tells me, it's super secure. Why don't we prove her wrong :)

This challenge is easy to solve. First of all, we viewed the source for the web page. It following JavaScript code:
```javascript
var _0xa107=["\x64\x65\x76\x65\x6C\x6F\x70\x65\x72\x5F\x63\x6F\x6E\x73\x6F\x6C\x65\x5F\x69\x73\x5F\x79\x6F\x75\x72\x5F\x66\x72\x69\x65\x6E\x64","\x65\x61\x73\x79\x63\x74\x66\x7B","\x7D"];
var _0x6fdc=[_0xa107[0],_0xa107[1],_0xa107[2]];
var secret=_0x6fdc[0];
secret=_0x6fdc[1]+secret+_0x6fdc[2];
</script>
```

We were sure that `secret` contained our secret. All we had to do was display what `secret` was holding. To do that, we chose Inspect Element of Google Chrome and on Console, we submit the following line:
`alert(secret)`
which revealed the flag to be: `easyctf{developer_console_is_your_friend}`
