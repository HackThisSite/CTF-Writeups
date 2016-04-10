# Frequencies
## The problem
> One of our teachers was so frustrated that they shook their computer. Now all their files are jumbled. What is this?

We're given a file (`coolencrypted.txt`) full of random characters.
The problem's name suggests that it can be solved using frequency analysis.

## The solution
It turns out that replacing the characters using [letter frequency](https://en.wikipedia.org/wiki/Letter_frequency) isn't enough. But it's a good start.
We can already see some common short words being deciphered correctly.
By guessing what other words are supposed to be we can then figure out the rest of the cipher.
It's not necessary to recover the whole file to get the flag.
The following script is enough to decrypt most of ciphertext.

```ruby
file = File.read("coolencrypted.txt")
chars = Hash.new(0)
file.chars.each do |chr|
  chars[chr] += 1;
end

subs = {
  "c" => " ",
  "1" => "e",
  "T" => "t",
  "k" => "a",
  "\"" => "o",
  "|" => "n",
  "w" => "h",
  "0" => "r",
  ":" => "i",
  "2" => "s",
  "V" => "d",
  "S" => "l",
  "K" => "m",
  "E" => "u",
  "7" => "w",
  ")" => "c",
  "x" => "f",
  "u" => "y",
  "]" => "p",
  "L" => "g",
  "C" => "p",
  "i" => "b",
  "m" => "v",
  "G" => "x",
  "e" => "a",
  "W" => "k",
  "/" => "z",
  "h" => "t",
  "$" => "_",
  "R" => "M",
  "r" => "m",
  "f" => "h",
  "-" => "x",
  "a" => "q",
  "X" => "J",
  "v" => "'",
  "#" => "."
}
result = ""
file.chars.each do |char|
  result += subs[char] || char
end
puts result
```
The flag is `this_is_one_of_my_fav_novels`.
