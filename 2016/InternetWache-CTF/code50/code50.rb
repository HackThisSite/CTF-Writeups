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
