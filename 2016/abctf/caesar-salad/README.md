# Caesar Salad
>>Most definitely the best salad around. Can you decrypt this for us?
xyzqc{t3_qelrdeq_t3_k33a3a_lk3_lc_qe3p3}

Essentially a staple in many of the easier CTF events cryptography category, this challenge is based on the caesar cipher.
The caesar cipher is essentially a rot-n cipher (rotating each alpha character n times)

An easy solution to these ciphers is to bruteforce it by performing a rot-1 to rot-26 on the string. I wrote a ruby script for this in the past, and used it to solve this challenge.

#caesar.rb
---
```
#!/usr/bin/ruby

def usage
  puts "-- Caesar Cipher Bruteforce --"
  puts "ruby #{$0} <string>"
end

cipher_list = (97..122).map(&:chr)

if !ARGV[0]
  usage
else
  chars = ARGV[0].split('')
  for i in (1..26)
    chars.map! { |c|
      if cipher_list.index(c) == 25
        c = cipher_list[0]
      elsif cipher_list.index(c)
        c = c.next
      else
        c = c
      end
    }
    puts "ROT #{i}: #{chars.join}   |   #{chars.join.upcase}"
  end
end

```
---

Running the script will give us our list of rot-n strings. The flags are in the format of `abctf{}`, so using `grep` on the output for abctf should give us our desired flag, and we will not manually need to skim the output.

`ruby caesar.rb xyzqc{t3_qelrdeq_t3_k33a3a_lk3_lc_qe3p3} | grep abctf`

Output:

`ROT 3: abctf{w3_thought_w3_n33d3d_on3_of_th3s3}   |   ABCTF{W3_THOUGHT_W3_N33D3D_ON3_OF_TH3S3}`

The flag should be lowercase, so the first result is our flag:

`abctf{w3_thought_w3_n33d3d_on3_of_th3s3}`

[![alt](https://asciinema.org/a/29qfl1dwsgd25o91nfv3dvvbn.png)](https://asciinema.org/a/29qfl1dwsgd25o91nfv3dvvbn)
