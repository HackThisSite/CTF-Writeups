# Crypto-Pirat
>Description: Did the East German Secret Police see a Pirat on the sky? Help me find out! Hint: We had 9 planets from 1930–2006... Hint2: Each planet has a number. (There's a table on a well-known website). After that you might be interested in ciphers used by the secret police.

>Attachment: crypto50.zip

## Solution
The attached file contained the following:
```
♆♀♇♀♆ ♇♇♀♆⊕ ♇♀♇♀♆ ♇♆♇♆⊕ ♆♇♆♇♇ ♀♆♇♆⊕ ♆♇♆♇♆ ♇♆♇♆⊕ ♆♇♇♀♇ ♀♆⊕♇♀ ♆⊕♇♀♆ ⊕♆♇♆♇ ♇♀♆♇♆ ⊕♇♀♇♀ ♆⊕♆♇♆ ♇♆♇♇♀ ♆⊕♆♇♆ ♇♆♇♆⊕ ♆♇♆♇♆ ♇♆⊕♇♀ ♆♇♇♀♆ ♇♆⊕♇♀ ♆♇♆♇♇ ♀♆⊕♆♇ ♆♇♇♀♇ ♀♇♀♆⊕ ♆♇♆♇♇ ♀♆⊕♇♀ ♇♀♆♇♆ ⊕♆♇♇♀ ♆⊕♇♀♆ ♇♇♀♇♀ ♆⊕♆♇♆ ♇♆♇♆♇ ♆⊕♇♀♆ ♇♇♀♆♇ ♆⊕♇♀♆ ♇♆♇♇♀ ♆⊕♆♇♆ ♇♇♀♇♀ ♇♀♆⊕♇ ♀♆♇♆♇ ♆⊕♇♀♇ ♀♇♀♆⊕ ♇♀♇♀♆ ♇♆♇♆⊕ ♆♇♆♇♆ ♇♆⊕♆♇ ♇♀♇♀♆ ⊕♆♇♆♇ ♆♇♆♇♇ ♀♆⊕♇♀ ♇♀♆♇♆ ♇♆⊕♆♇ ♆♇♆♇♇ ♀♇♀♆⊕ ♆♇♆♇♆ ♇♆⊕♆♇ ♇♀♆♇♆ ♇♆⊕♆♇ ♆♇♆♇♆ ♇♆♇♆⊕ ♆♇♇♀♇ ♀♆⊕♇♀ ♇♀♆♇♆ ⊕♆♇♆⊕ ♆♇♆♇♇ ♀♇♀♇♀ ♆⊕♇♀♆ ♇♇♀♆♇ ♆⊕♇♀♇ ♀♆♇♆♇ ♆♇♆⊕♇ ♀♆♇♆⊕ ♇♀♇♀♆ ♇♆♇♆⊕ ♆♇♆♇♆ ♇♆⊕♇♀ ♆♇♆♇♇ ♀♆⊕♆♇ ♆⊕♇♀♇ ♀♇♀♆⊕ ♆♇♇♀♆ ♇♆⊕♆♇ ♇♀♇♀♇ ♀♆⊕♆♇ ♇♀♇♀♆ ♇♆⊕♆♇ ♆♇♇♀♆ ⊕♇♀♆♇ ♆♇♆♇♇ ♀♆⊕♇♀ ♆♇♆♇♆ ♇♇♀♆⊕ ♇♀♆♇♆ ♇♆♇♇♀ ♆⊕♇♀♆ ♇♆♇♆♇ ♇♀♆⊕♇ ♀♆♇♆♇ ♆♇♇♀♆ ⊕♇♀♆♇ ♆♇♆♇♇ ♀
```

These symbols are used to represent the planets in the solar system, here follows the complete table:

```
(Solar) planets 1930–2006:

Mercury ☿   1
Venus   ♀   2
Earth   ⊕   3
Mars    ♂   4
Jupiter ♃   5
Saturn  ♄   6
Uranus  ♅   7
Neptune ♆   8
Pluto   ♇   9
```
(table from wikipedia: https://en.wikipedia.org/wiki/Planet#20th_century)

Replacing the symbols with the number of the respective planet gives:

```
82928 99283 92928 98983 89899 28983 89898 98983 89929 28392 83928 38989 92898 39292 83898 98992 83898 98983 89898 98392 89928 98392 89899 28389 89929 29283 89899 28392 92898 38992 83928 99292 83898 98989 83928 99289 83928 98992 83898 99292 92839 28989 83929 29283 92928 98983 89898 98389 92928 38989 89899 28392 92898 98389 89899 29283 89898 98389 92898 98389 89898 98983 89929 28392 92898 38983 89899 29292 83928 99289 83929 28989 89839 28983 92928 98983 89898 98392 89899 28389 83929 29283 89928 98389 92929 28389 92928 98389 89928 39289 89899 28392 89898 99283 92898 98992 83928 98989 92839 28989 89928 39289 89899 2
```

The East German Secret Police is the Stasi. They had a conversion table known as the TAPIR that was used to convert plaintext to numbers before using a one-time-pad to encrypt the message. Pirat is an acronym for Tapir, so this is probably what the hint indicates. Decoding the above sequence of numbers with the TAPIR table we get the following: (ZwR and Zi substituted by spaces)

```
 -.- --.. ..-. .... .-- - - ..-. -- ...- ... ... -.-. -..- ..--- ..- --. .- -.-- .... -.-. -..- ..--- -.. --- --.. ... .-- ....- --.. ...-- ... .-.. ..... .-- --. . ..--- -.-. --... -. --.. ... -..- . --- .-. .--- .--. ..- -...- -...- -...- -...- -...- -...-
```
(link to a TAPIR table: https://rgpsecurity.files.wordpress.com/2014/10/tapir_fulbrich.jpg)

This is morse code, and it translates to:

```
KZFHWTTFMVSSCX2UGAYHCX2DOZSG4Z3SL5WGE2C7NZSXEORJPU======
```

Which is a valid base32 encoded string and decodes to:

`VJ{Neee!_T00q_Cvengr_lbh_ner:)}`

Then we ROT13 the above to get the flag:

`IW{Arrr!_G00d_Pirate_you_are:)}`
