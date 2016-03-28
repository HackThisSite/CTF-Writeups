Description: Solved by 408 teams.
Someone planted a file on our computer (the [shell server](https://www.easyctf.com/shell), but we don't know what it is! The only clue that we have is that it's owned by a user called `l33t_haxx0r`. Can you figure out the flag?

This challenge requires us to solve the challenge using [shell server](https://www.easyctf.com/shell). After logging in, we issued following command:

`find / -type f -user l33t_haxx0r 2> /dev/null`

This gave us the location of the file which was `/var/www/html/index.html`. Opening it and looking around, we found the flag in comments of the html file.
The flag was:
`easyctf{c0mp1et3ly_r3kt}`
