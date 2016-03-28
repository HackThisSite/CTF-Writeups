require 'socket'
s = TCPSocket.new "188.166.133.53", 12037

s.write "ffffffffff\nf"
puts s.read
s.close
