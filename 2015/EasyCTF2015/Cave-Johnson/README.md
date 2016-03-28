Description: Solved by 111 teams.
Welcome to [Small Hole Sciences](https://www.easyctf.com/static/problems/cave-johnson/cave-johnson.txt).

(Since all of their budget was spent on moon rocks, they were only able to afford an old-fashioned Vigenere Cipher.) 



In this challenge, we were given a text file and a hint **Vigenere Cipher** (more on [Wikipedia](https://en.wikipedia.org/wiki/Vigenere_cipher)).
It didn't take us time to realize that the text file contained ciphertext which was encrypted using Vigenere Cipher.

To crack the ciphertext, we needed to find the encryption key. After searching for a bit about ways to crack it, we stumbled upon [this](http://www.mygeocachingprofile.com/codebreaker.vigenerecipher.aspx) site.

We also stumbled upon [Portal Unofficial Wiki](http://theportalwiki.com/wiki/Cave_Johnson) which told us that Cave Johnson is the founder of Aperture Science. Since "small hole" is also called "aperture", we were convinced that this challenge has some relation with the word "aperture".

Keeping that in mind, we returned to cracking Vigenere Cipher. For that, we copy-pasted text from the given text file to the textbox named **Encrypted Text** and told the site to "try to determine key and message based on analysis of encrypted text" for **Shift key**.

We noticed that the section of the string at the end of the text was different (it had underscores) and resembled to the pattern of the flag. But we were unsure about the length of word it contained before the first underscore. Keeping that in mind, we began analyzing the [result](./result.txt).

While analyzing the [result](./result.txt) from the site, first result with key `eaimorbacorsiammorongore` decrypted the last section of the string (`klqs_ue_ogseviii_inp_is_koym_hfs_uuot`) to `ttis_is_aperpure_enh_we_tnyk_toa_much`. We guessed that length of the word before the first underscore would be a 4 letter word and continued our analysis.

We found out that the word 'aperpure' resembles to `aperture` (a word that we thought had something to do with this challenge) and `ttis` resembles to `this`. Few words didn't make sense and few translated to exact English words. So we had:

`klqs` -> -> `ttis` -> `this`  
`ue` -> `is`  
`ogseviii` -> `aperpure` -> `aperture`  
`inp` -> `enh`  
`is` -> `we`  
`koym` -> `tnyk`   
`hfs` -> `toa`  
`uuot` -> `much`  

We then copy-pasted section of string `klqs_ue_ogseviii_inp_is_koym_hfs_uuot` to [this](http://sharkysoft.com/vigenere/) site and tried decrypting it to produce the output above.
After a long process of analysis, subsitution and guessing, we were able to decrypt the string `klqs_ue_ogseviii_inp_is_koym_hfs_uuot` to `this_is_aperture_and_we_talk_too_much` with key `qdhzllnqnmbnqdhzllnqnmbn`.

After formatting the message to correct flag format, i.e. `easyctf{...}`, we got the flag which turned out to be `easyctf{this_is_aperture_and_we_talk_too_much}`
