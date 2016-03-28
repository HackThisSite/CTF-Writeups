Description: Solved by 355 teams.
This string has been encrypted using XOR!

`message = " $6<&1#><*\x1a!$2\x22\x1a,\x1a- $7!\x1a<*0\x1a),. !\x1a=*78"`

The whole motive of this challenge was to find the cipher which would decrypt the message. Since the description doesn't tell us much about the challenge so we look at the hint which says:
"What could the key be? Here's a hint: it was encrypted 3 times."

If we consider the [Leetspeak](https://en.wikipedia.org/wiki/Leet) then `3` translates to `E`. So, we wrote a simple Python script called [xor.py](./xor.py) which gave us the flag:
` easyctf{yo_dawg_i_heard_you_liked_xor} `
