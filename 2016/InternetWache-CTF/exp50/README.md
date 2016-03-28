# Ruby's count
 > Description: Hi, my name is Ruby. I like converting characters into ascii values and then calculating the sum.

> Service: 188.166.133.53:12037

# Solution
The server will calculate the sum of 10 characters. The characters also have to match the regular expression `/^[a-f]{10}$/` (the server tells us this if the match fails). The flag will be given to us if the sum of those characters is bigger than 1020. That is unfortunately the biggest number we can achieve with these 10 characters. The regex however will match only one line. To exploit this we need to simply pass the server another line with any characters in it.
```Ruby
require 'socket'
s = TCPSocket.new "188.166.133.53", 12037

s.write "ffffffffff\nf"
puts s.read
s.close
```
The flag is `IW{RUBY_R3G3X_F41L}`.
