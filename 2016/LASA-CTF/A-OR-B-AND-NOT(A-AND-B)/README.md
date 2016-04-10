# A OR B AND NOT(A AND B)
## The problem
> Our logic teacher communicates with us with these weird lists of numbers. What is this?

> Hint: 3 bytes

## The solution
The logic operation in the name of the problem is called "exclusive or" or XOR for short.
It's often used in cryptography ([XOR cipher](https://en.wikipedia.org/wiki/XOR_cipher)).
We can assume that the numbers in the file (`encryptedmessage.txt`) represent the byte values of the encrypted characters.
Because the key used to encrypt it is quite short (3 bytes) we can bruteforce it within a reasonable amount of time.

```ruby
bytes = File.read("encryptedmessage.txt").split(",").map { |s| s.to_i }

key_values = 0x00..0xff_ff_ff

key_values.each do |value|
  key = [value].pack("L")[0..2]
  string = ""
  bytes.each_with_index do |byte, i|
    string += (byte ^ key[i%3].ord).chr
  end
  if string.match /lasa/
    puts string, "Key: " + key.unpack("C*").map { |c| c.to_s 16 }.join
  end
end
```
The decrypted message:
> "to find why this sheep's wool was red; and the prize was awarded to a learned man of the North, who demonstrated by A plus B minus C divided by Z, that the sheep must be red, and die of the rot." - lasactf{I_like_candide_sheep}

> Key: 677a32

The flag is `lasactf{I_like_candide_sheep}`.
