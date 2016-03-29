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
