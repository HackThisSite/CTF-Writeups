#crypto300 - Las cifras de sustitución han estado por mucho tiempo

##Solution

We are given image with weird looking characters (TODO:add image)
Title of problem is written in spanish and it says "substitution ciphers have been around for long time".
After spending lots of time comparing ciphertext with various writing systems I decided to simply google phrase "spanish cipher" and look at images we can see this image

[image]: http://cryptiana.web.fc2.com/code/cg1.jpg

We can recognize that characters on table are same as ones in ciphertext.

So I discovered that cipher used is Philip II cipher.
Rules for decrypting were following:

1.look up symbol in the table
2.if it has one dot under or above it's insignificant character
3.if it has 2 dots above or under it it's double letter

Plaintext is:

philip iix as a pretty smart guY too bad that his cipher brocen in three months head to rc three ctf dot rcthree dot club slash zbynzhggxaxxhymmvahg to get the flag

Sadly https://rc3ctf.rc3.club/zbynzhggxaxxhymmvahg returned 404 but that turned out to be just a server problem, I got the flag after contacting admin.

Flag: RC3-2017{crypt0_1s_n0t_4ll_3ngl1sh_4lph4b3t}
