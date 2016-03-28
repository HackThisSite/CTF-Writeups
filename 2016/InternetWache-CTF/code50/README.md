# A numbers game
> Description: People either love or hate math. Do you love it? Prove it! You just need to solve a bunch of equations without a mistake.

> Service: 188.166.133.53:11027

## Solution
After connecting to the server we get prompted with a math problem.
All we need to do is to write a script that will solve the problems and send the solutions to the server.
```ruby
require 'socket'

s = TCPSocket.new "188.166.133.53", 11027

while line = s.gets
  puts line
  if match = line.match(/x (.) (-?\d+) = (-?\d+)/)
    op = case match[1]
         when "*" then :/
         when ":" then :*
         when "+" then :-
         when "-" then :+
         end
    answer = match[3].to_i.send op, match[2].to_i
    puts answer
    s.write answer
  end
end
```
After solving 100 problems the server gives us the flag: `IW{M4TH_1S_34SY}`.
