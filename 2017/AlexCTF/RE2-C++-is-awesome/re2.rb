flag = ''
until flag[-1] == '}'
  [*'A'..'Z', *'a'..'z', *'0'..'9', '_', '{', '}'].each do |ch|
    result = `./re2 #{flag + ch}`
    if result.include? 'flag'
      flag += ch
      break
    end
  end
end
puts flag
