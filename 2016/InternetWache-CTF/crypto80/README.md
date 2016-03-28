# Procrastination
> Description: Watching videos is fun! Hint: Stegano skills required.

>Attachment: crypto80.zip

>Service: https://procrastination.ctf.internetwache.org


## Solution
The provided archive contained the first 30 seconds of Rick Astley's Never Gonna Give You Up (rick roll) video clip in WebM format. Analysing the hexdump of the file and trying to import the audio into audacity (or other audio editing software) revealed a hidden audio track.
The hidden audio track had 21 groups of 3 or 4 beeps of varying frequencies. The following frequencies for the beeps were obtained analysing the spectrogram of the hidden audio:
```
Frequencies in Hz
Group 01: (4 beeps)
B1: 941 + 1336
B2: 697 + 1209
B3: 697 + 1209
B4: 697 + 1209

Group 02: (4 beeps)
B1: 941 + 1336
B2: 697 + 1209
B3: 697 + 1337
B4: 852 + 1209

Group 03: (4 beeps)
B1: 941 + 1336
B2: 697 + 1209
B3: 852 + 1209
B4: 697 + 1477

Group 04: (4 beeps)
B1: 941 + 1336
B2: 697 + 1209
B3: 941 + 1336
B4: 770 + 1209

Group 05: (4 beeps)
B1: 941 + 1336
B2: 697 + 1209
B3: 697 + 1336
B4: 697 + 1336

Group 06: (3 beeps)
B1: 941 + 1336
B2: 770 + 1477
B3: 941 + 1336

Group 07: (4 beeps)
B1: 941 + 1336
B2: 697 + 1209
B3: 697 + 1209
B4: 770 + 1477

Group 08: (3 beeps)
B1: 941 + 1336
B2: 770 + 1477
B3: 697 + 1477

Group 09: (4 beeps)
B1: 941 + 1336
B2: 697 + 1209
B3: 697 + 1336
B4: 697 + 1477

Group 10: (4 beeps)
B1: 941 + 1336
B2: 697 + 1209
B3: 697 + 1477
B4: 852 + 1209

Group 11: (4 beeps)
B1: 941 + 1336
B2: 697 + 1209
B3: 697 + 1336
B4: 852 + 1209

Group 12: (3 beeps)
B1: 941 + 1336
B2: 770 + 1477
B3: 697 + 1209

Group 13: (4 beeps)
B1: 941 + 1336
B2: 697 + 1209
B3: 697 + 1336
B4: 770 + 1209

Group 14: (4 beeps)
B1: 941 + 1336
B2: 697 + 1209
B3: 697 + 1209
B4: 941 + 1336

Group 15: (4 beeps)
B1: 941 + 1336
B2: 697 + 1209
B3: 697 + 1477
B4: 852 + 1209

Group 16: (4 beeps)
B1: 941 + 1336
B2: 697 + 1209
B3: 697 + 1336
B4: 941 + 1336

Group 17: (4 beeps)
B1: 941 + 1336
B2: 697 + 1209
B3: 697 + 1209
B4: 941 + 1336

Group 18: (3 beeps)
B1: 941 + 1336
B2: 770 + 1477
B3: 941 + 1336

Group 19: (4 beeps)
B1: 941 + 1336
B2: 697 + 1209
B3: 697 + 1209
B4: 770 + 1477

Group 20: (3 beeps)
B1: 941 + 1336
B2: 770 + 1477
B3: 697 + 1477

Group 21: (4 beeps)
B1: 941 + 1336
B2: 697 + 1209
B3: 697 + 1336
B4: 697 + 1477
```

These beeps composed of two different frequencies each are DTMF tones. They decode to this sequence of numbers:

`0111 0127 0173 0104 0122 060 0116 063 0123 0137 0127 061 0124 0110 0137 0120 0110 060 0116 063 0123`

Those numbers are the codes of ascii characters in octal representation. We can translate them with:

```python
import sys

a = sys.stdin.read().strip().split()

for i in a:
    character = chr(int(i, 8))
    sys.stdout.write(character)

sys.stdout.write('\n')
```

This yields the flag (without the trailing '}', this had to be added manually): `IW{DR0N3S_W1TH_PH0N3S`
