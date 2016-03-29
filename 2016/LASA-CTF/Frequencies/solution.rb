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
