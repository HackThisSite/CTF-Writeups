# Brute with Force
 > Description: People say, you're good at brute forcing... Have fun! Hint: You don't need to crack the 31. character (newline). Try to think of different (common) time representations. Hint2: Time is CET

> Service: 188.166.133.53:11117

## Solution
To solve this challenge we need to send the server a string in a format of `TIME:CHAR` where the `CHAR` is just a random character and the `TIME` represents the time given to us by the server offset by +- 30 seconds. We can brute-force that because we are also given a hash of the string. After a few tries it turns out that the correct time representation is the epoch time. It turns out that the next characters also make up the flag.
```ruby
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
```
The flag is `IW{M4N_Y0U_C4N_B3_BF_M4T3RiAL!}`.
