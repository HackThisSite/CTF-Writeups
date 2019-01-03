# Conversion Error
> Solves: 63

> With `assert_conversion(str: string)`, we assert that our VM properly handles conversions. So far we never triggered the assertion and are certain it's impossible.
> http://35.207.132.47/

> Difficulty estimate: Medium

This is one of the [Wee](../Wee) challenges.

It's the fourth of 5 similar challenges revolving around breaking assertions
inside the interpreter source.

## Analysis

The function to attack:

```js
externals.addFunction(
    "assert_conversion",
    [{name: "str", type: compiler.StringType}], compiler.StringType,
    false,
    (str: string) => str.length === +str + "".length || !/^[1-9]+(\.[1-9]+)?$/.test(str)
        ? "Convert to Pastafarianism" : flags.CONVERSION_ERROR
)
```

While this challenge doesn't exactly feel like it works the way it was intended
to it's really easy to solve. `+str` converts the string to a number. All we
have to do is provide a string which contains a number without the digit `0`
which is also not equal to it's length.

## Solution

There's really nothing exciting to it.

```
liquid$> curl -X POST http://35.207.132.47/wee/run -d '{ "code": "alert(assert_conversion(\"2\"))" }'
{"code":"alert(assert_conversion(\"2\"))","result":"35C3_FLOATING_POINT_PROBLEMS_I_FEEL_B4D_FOR_YOU_SON\n"}
```
