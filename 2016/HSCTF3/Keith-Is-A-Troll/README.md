# Keith is a Troll
> Ha! Keith likes to troll, and now he's trolling you! He has written a [login](https://github.com/HackThisCode/CTF-Writeups/tree/master/2016/HSCTF3/Keith-Is-A-Troll/login.java "login.java source") that he says is impossible to get into. Can you prove him wrong?

Source Code:
------

```
package exploit;

import java.util.Scanner;

public class KeithLikesToTroll {
	public static void main(String[] args){
		int key;

		Scanner scn = new Scanner(System.in);
		System.out.print("Enter key: ");
		key = scn.nextInt();
		scn.close();

		if(1338557220 / key * key != 1338557220 && key > 0){
			System.out.println("Login succesful. The flag is the smallest key which will let you log in.");
		}else{
			System.out.println("Login rejected.");
		}
	}
}
```

The code is pretty straight forward. We need to find a key where `1338557220 / key * key is not equal to 1338557220` with a constraint of `key > 0`

Anyone that knows me will tell you how much I love Ruby. So, of course I whipped up a one liner for the command line to complete this challenge.

`ruby -e '(1..(1.0/0)).map{|d|abort("#{d}") if 1338557220/d*d != 1338557220}'`

Once we run this script, we get the output `8`, this is the flag:

```
┌─[x509@infosploit] - [~] - [2016-05-23 09:03:09]
└─[1] <> ruby -e '(1..(1.0/0)).map{|d|abort("#{d}") if 1338557220/d*d != 1338557220}'
8
```

If you are a bash lover, this will also work, however it's sloppy. If the key was a larger number in the millions, it would not finish nearly in time... Luckily we only have to loop up to 8 for our key.

```
for i in {1..10}; do if [[ $((1338557220/ $i * $i)) -ne '1338557220' ]]; then echo $i; fi; done
```
