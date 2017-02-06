# RE2: C++ is awesome

100 points
> They say C++ is complex, prove them wrong!

## Solution

We're given a small binary which takes a single argument and returns either:
`Better luck next time` when called with an incorrect flag or `You should have
the flag by now` when called with a part of the flag.

[@Pyhscript](https://github.com/Pyhscript) noticed that this allows us to brute-force the flag without actually
needing to analyze the binary. This simple script turned out to be enough:
```ruby
flag = ''
until flag[-1] == '}'
  [*'A'..'Z', *'a'..'z', *'0'..'9', '_', '{', '}'].each do |ch|
    result = `./re2 #{flag + ch}`
    if result.include? 'flag'
      flag += ch
      break
    end
  end
end
puts flag
```

In a few seconds we get the full flag which is
`ALEXCTF{W3_L0v3_C_W1th_CL45535}`.
