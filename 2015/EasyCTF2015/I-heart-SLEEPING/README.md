Description: Solved by 61 teams.
We received this string, but I have no idea what it means! `3845281945283805284526053525260547380516453748164748478317454508`

Just by looking at it, it doesn't make that much sense. Let's go for hints.

Hints:
ARGH I CAN'T SLEEP PEOPLE KEEP STEALING MY ZZZZs . . . NO MORE ZZZs /cries

P.S. You're overthinking it.

P.P.S. Blocks of 2

Final hint: sqrt(ABCDEFGHIJKLMNOPQRSTUVWXY). Where'd my Z's go?

Focusing on "Blocks of 2" and absence of 'Z' in the final hint, we can say that this has something to do with a sqaure which has one or more letter missing.
After doing a little bit of research, we found out that this problem is related to [Polybius Square](https://en.wikipedia.org/wiki/Polybius_square) but filled with letters from A to Y.

Following the second hint, we divided the string into blocks of two as:

`38 45 28 19 45 28 38 05 28 45 26 05 35 25 26 05 47 38 05 16 45 37 48 16 47 48 47 83 17 45 45 08`

But there is a problem, Polybius Square must have numbers in range of 1 to 5 but given string doesn't fit the criteria.

If we look closely, we can see a pattern. First digit of every 2 bytes block is in range of 0 to 4 and second digit is in range of 5 to 9 (except for digit 5th block from last which is a typo). With this knowledge, we created a Polybius Square as:

|       | **0** | **1** | **2** | **3** | **4** |
| ----- |:-----:|:-----:|:-----:|:-----:|:-----:|
| **5** |   A   |   B   |   C   |   D   |   E   |
| **6** |   F   |   G   |   H   |   I   |   J   |
| **7** |   K   |   L   |   M   |   N   |   O   |
| **8** |   P   |   Q   |   R   |   S   |   T   |
| **9** |   U   |   V   |   W   |   X   |   Y   |

We translated our string using the above Polybius Square and we got following message:
`38 45 28 19 45 28 38 05 28 45 26 05 35 25 26 05 47 38 05 16 45 37 48 16 47 48 47 83 17 45 45 08`
`S  E  R  V  E  R  S  A  R  E  H  A  D  C  H  A  O  S  A  G  E  N  T  G  O  T  O  S  L  E  E  P ` = `serversarehadchaosagentgotosleep`

Adjusting the text to the flag format, we got our flag which is: `easyctf{serversarehadchaosagentgotosleep}` 
