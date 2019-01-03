# Number Error

> Solves: 71

> The function `assert_number(num: number)` is merely a debug function for our Wee VM (WeeEm?). It proves additions always work. Just imagine the things that could go wrong if it wouldn't!
> http://35.207.132.47/

> Difficulty estimate: Easy - Medium

This is one of the [Wee](../Wee) challenges.

It's the second of 5 similar challenges revolving around breaking assertions
inside the interpreter source.

## Analysis

`weeterpreter.ts` defines that function as follows:

```js
externals.addFunction(
    "assert_number",
    [{name: "num", type: compiler.NumberType}], compiler.StringType,
    false,
    (num: number) => !isFinite(num) || isNaN(num) || num !== num + 1
        ? "NUMBERS WORK" : flags.NUMBER_ERROR
)
```

This means that we have to find a number which is not infinite, isn't `Nan` and
is equal to itself incremented by one. While this might seem daunting, floating
point numbers are implemented in a way which allows for such inaccuracies. At
some point it becomes impossible to encode certain numbers so they have to be
rounded. This means that the result of adding `1` to a sufficiently big number
will not change it's value.

## Solution

Just input any arbitrary large number:

```
liquid$> curl -X POST http://35.207.132.47/wee/run -d '{ "code": "alert(assert_number(9999999999999999))" }'
{"code":"alert(assert_number(9999999999999999))","result":"35C3_THE_AMOUNT_OF_INPRECISE_EXCEL_SH33TS\n"}
```
