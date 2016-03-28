require 'socket'
require 'date'
require 'digest'

SHA1 = Digest::SHA1
s = TCPSocket.new "188.166.133.53", 11117
flag = ""
puts s.gets
while line = s.gets
  puts line
  if match = line.match(/(\d+):(\d+):(\d+), (\d+)th .* of (\d+) .*: (.*)$/)
    match[6].chomp!
    date_string = "#{match[1]}:#{match[2]}:#{match[3]}:#{match[4]}:#{match[5]}:+0100"
    date = DateTime.strptime(date_string, "%H:%M:%S:%j:%Y:%z")
    date = date.to_time
    date_string = ""
    (-30..30).each do |offset|
      [*" ".."~"].each do |char|
        date_string = (date + offset).strftime("%s") + ":" + char
        if match[6] == SHA1.hexdigest(date_string)
          flag += char
          s.write date_string
          puts date_string
        end
      end
    end
  end
  break if flag.length == 31
end
puts flag
