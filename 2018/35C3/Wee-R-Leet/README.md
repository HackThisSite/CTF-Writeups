# Wee R Leet

> Solves: 78

> Somebody forgot a useless assert function in the interpreter somewhere. In our agile development lifecycle somebody added the function early on to prove it's possible. Wev've only heared stories but apparently you can trigger it from Wee and it behaves differently for some "leet" input(?) What a joker. We will address this issue over the next few sprints. Hopefully it doesn't do any harm in the meantime.
> http://35.207.132.47/

> Difficulty estimate: Easy

This is one of the [Wee](../Wee) challenges.

It's the first of 5 similar challenges revolving around breaking assertions
inside the interpreter source.

## Analysis

If we take a look at the `weeterpreter.ts` file we can find that assertion
mentioned in the description:

```js
externals.addFunction(
    "assert_leet",
    [{name: "maybe_leet", type: compiler.NumberType}], compiler.StringType,
    false,
    (maybe_leet: number) => maybe_leet !== 0x1337 ? "WEE AIN'T LEET" : flags.WEE_R_LEET
)
```

This call exposes the function given as the last argument inside the Wee
runtime. If we want to get our flag wee need to make `maybe_leet !== 0x1337`
return `false`.

## Solution

Because Wee doesn't seem to support hexadecimal numbers we have to convert
`0x1337` to decimal first and then call the assertion:

```
liquid$> curl -X POST http://35.207.132.47/wee/run -d '{ "code": "alert(assert_leet(4919))" }'
{"code":"alert(assert_leet(4919))","result":"35C3_HELLO_WEE_LI77LE_WORLD\n"}
```
