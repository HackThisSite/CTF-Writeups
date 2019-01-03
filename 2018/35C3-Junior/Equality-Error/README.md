# Equality Error
> Solves: 62

> At `assert_equals(num: number)`, we've added an assert to make sure our VM properly handles equality. With only a few basic types, it's impossible to mess this one up, so the assertion has never been triggered. In case you do by accident, please report the output.
> http://35.207.132.47/

> Difficulty estimate: Medium

This is one of the [Wee](../Wee) challenges.

It's the third of 5 similar challenges revolving around breaking assertions
inside the interpreter source.

## Analysis

Appropriate source:

```js
externals.addFunction(
    "assert_equals",
    [{name: "num", type: compiler.NumberType}], compiler.StringType,
    false,
    (num: number) => num === num
        ? "EQUALITY WORKS" : flags.EQUALITY_ERROR
)
```

To solve this challenge we need to find a number which isn't equal to itself.
If we take a look at the
[JavaScript comparison table](https://dorey.github.io/JavaScript-Equality-Table/)
we can see that one such value is `NaN`.

## Solution

There are many ways to generate `NaN` so this is just one of the possible
solutions:

```
liquid$> curl -X POST http://35.207.132.47/wee/run -d '{ "code": "alert(assert_equals(sqrt(-1)))" }'
{"code":"alert(assert_equals(sqrt(-1)))","result":"35C3_NANNAN_NANNAN_NANNAN_NANNAN_BATM4N\n"}
```
