We're given the following description:
>This flag is protected by a password stored in a highly sohpisticated chain of hashes. Can you capture it nevertheless? We are certain the password consists of lowercase alphanumerical characters only.  
>nc 35.207.132.47 1337  
>[Source](https://archive.aachen.ccc.de/junior.35c3ctf.ccc.ac/uploads/ffb8d1ab6ff961419bee1cf1cddfb2e5-ultra_secret.tar)  
>Difficulty estimate: Easy

The provided tar file contains 3 files, **[Cargo.lock](Cargo.lock)**, **[Cargo.toml](Cargo.toml)** and **[src/main.rs](src/main.rs)**. Even though I've never done any rust it is pretty clear that [Cargo](https://doc.rust-lang.org/stable/cargo/) files are for their package manager, and the **```main.rs```** file contains the actual code we're interested in.
```rust
extern crate crypto;

use std::io;
use std::io::BufRead;
use std::process::exit;
use std::io::BufReader;
use std::io::Read;
use std::fs::File;
use std::path::Path;
use std::env;

use crypto::digest::Digest;
use crypto::sha2::Sha256;

fn main() {
    let mut password = String::new();
    let mut flag = String::new();
    let mut i = 0;
    let stdin = io::stdin();
    let hashes: Vec<String> = BufReader::new(File::open(Path::new("hashes.txt")).unwrap()).lines().map(|x| x.unwrap()).collect();
    BufReader::new(File::open(Path::new("flag.txt")).unwrap()).read_to_string(&mut flag).unwrap();

    println!("Please enter the very secret password:");
    stdin.lock().read_line(&mut password).unwrap();
    let password = &password[0..32];
    for c in password.chars() {
        let hash =  hash(c);
        if hash != hashes[i] {
            exit(1);
        }
        i += 1;
    }
    println!("{}", &flag)
}

fn hash(c: char) -> String {
    let mut hash = String::new();
    hash.push(c);
    for _ in 0..9999 {
        let mut sha = Sha256::new();
        sha.input_str(&hash);
        hash = sha.result_str();
    }
    hash
}
```

The code is very short and it doesn't do much:
1. read hashes.text
2. ask user for password
3. split that password into 32 chars (better to crash than accept passwords that aren't 32 characters long I guess)
4. hash each character (10000 times) and compare it to the corresponding hash in hashes.txt

If you've absolutely never done anything security related you might mistakenly think "more hashes must be better" and "hashing more times must be better". We'll see why that is wrong in a second.

First problem of splitting the password into multiple hashes for each character means I only need to crack hashes that I know are 1 character long, it'll take no time at all. So the strength of your 32character password is now the same as one that is 1 character long. Of course I don't have these hashes (yet) to crack them, so just this isn't enough for me to easily get in.

Second problem is hashing things 10000 times. While hashing things multiple times does increase the hash time and is a valid technique to make hashes harder to crack, in combination with the first problem it is disastrous.  
We're not hashing 1 thing 10000 times, we're hashing every character 10000 times, that means 320000 [sha256](https://en.wikipedia.org/wiki/SHA-2) hashes.. that takes a very long time (about 21.4 seconds on the challenge server).

Third and fatal problem is that once the server realizes the password doesn't match it stops hashing and immediately returns. This allows us to perform a [timing attack](https://en.wikipedia.org/wiki/Timing_attack).

### Timing attack
> In cryptography, a timing attack is a side channel attack in which the attacker attempts to compromise a cryptosystem by analyzing the time taken to execute cryptographic algorithms. Every logical operation in a computer takes time to execute, and the time can differ based on the input; with precise measurements of the time for each operation, an attacker can work backwards to the input.[1]
>
>Information can leak from a system through measurement of the time it takes to respond to certain queries. How much this information can help an attacker depends on many variables: crypto system design, the CPU running the system, the algorithms used, assorted implementation details, timing attack countermeasures, the accuracy of the timing measurements, etc.
>
>Timing attacks are often overlooked in the design phase because they are so dependent on the implementation and can be introduced inadvertently with compiler optimizations. Avoidance of timing attacks involves design of constant-time functions and careful testing of the final executable code.[1] 
>
> -- [wikipedia](https://en.wikipedia.org/wiki/Timing_attack)

Timing attacks aren't just limited to cryptography related implementations like in this case. A simple string comparison in any language could make it vulnerable to a timing attack if the standard methods for string comparison are used.  
If the thing you're comparing to needs to stay a secret you should use a comparison function with a fixed length. That is, keep checking each character for a match even if you already know it is wrong.

##### Example
A really simple and dumb example would be a numerical keypad controlling a door that checks each number entered and gives you an error as soon as it finds a number that doesn't match its preprogrammed sequence.  
You'd be able to enter 1111 2111...9111 and once the first number is correct it'd take it slightly longer to respond (or worse it'd not even wait for you to enter all the numbers and gives an error as soon as you press the digit).

When guessing the number to enter the building for a 4 digit code you'd need 10000 attempts (0000-9999) in the absolute worst case.  
But if it is vulnerable to a timing attack you'd only need 40 attempts at most (10 for each digit), significantly less.

Since this example describes an object you'd have physical access to, your time measurements could be very precise. The solution for the manufacturer would be to program its device to store all the entered numbers in a single number and compare them at the same time, which wouldn't cause a time variation when comparing a wrong sequence to a slightly less wrong sequence.

##### Our attack
Our attack will work the same way as the keypad example. We'll start with a wrong password aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa, and change one character at a time until it takes longer to respond.

We could easily write a script to do this, but in this case it is so simple it might be easier to just do it manually than bother writing something.

We'll use the time command to measure the time it takes for the server to close the connection, and while we're doing it manually, we can still do it in bulk. Since we know the password is lowercase alphanumerical I simply pasted the following commands into my terminal in 1 go.

```bash
time ( echo "0aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "2aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "3aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "4aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "5aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "6aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "7aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "8aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "9aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "caaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "daaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "eaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "gaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "haaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "iaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "jaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "kaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "laaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "maaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "paaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "qaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "raaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "saaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "taaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "uaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "vaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "waaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "yaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
time ( echo "zaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc 35.207.158.95 1337)
```
(NOTE: the challenge server is no longer in use, don't harass whoever is the new owner of that ip)

This will run each of those commands sequentially and show us how long it took to complete. We'd be able to see that 1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa took a bit longer to return than all the others and thats how we know the first character was a 1.

Next we try the next sequence 10aaaaaaaa...aa to 1zaaaaaaa...aa and pick the longest of those. As we get more and more correct characters it'll take significantly longer per attempt. So if you have the screen real-estate like I do just run it somewhere in view while you do other things and interupt the commands (CTRL+C) when you see you notice you got a hit. Interupting when you get a hit will make it a lot faster than trying all variations and checking which character took the longest after doing it all (also, I noticed pretty quickly that the password was more like 0-9,a-f, not a-z, so even worse case became less horrible).

I don't know how long it took to perform the attack, but the attempts to find the first character of the password only took 0.7 seconds, the last character took 21.4 seconds per attempt.

In the end I was greeted with the following:

```bash
weekend@haxtop:~$ time ( echo "10e004c2e186b4d280fad7f36e779ed4" | nc 35.207.158.95 1337)
Please enter the very secret password:
35C3_timing_attacks_are_fun!_:)
```

### Conclusion
Pretty similar to the previous writeup, **don't** write your own weird hashing implementations if you don't know what you're doing. 

If they just hashed the password once using sha256 it would have taken a very long time to crack that password.  
In fact lets look at how long exactly. 

If we assume the characters were lowercase alphanumerical, we'd have 36 possible characters (0-9,a-z). There are 32 characters.
That would result in $$36^{32}$$ possible combinations. Let's assume we got a nice computer capable of doing 1000000 hashes per second: 
![](https://latex.codecogs.com/gif.latex?%5C%5C%2036%5E%7B32%7D%20%3D%206.334028666%5Ctimes10%5E%7B49%7D%20%5Ctext%7B%20combinations%7D%20%5C%5C%2036%5E%7B32%7D%20%5Ctext%7B%20combinations%7D%20%5Cquad/%5Cquad%201000000%20%5Ctext%7B%20hashes/sec%20%7D%20%3D%206.334028666%5Ctimes10%5E%7B43%7D%20%5Ctext%7B%20seconds%7D%20%5C%5C%206.334028666%5Ctimes10%5E%7B43%7D%20%5Ctext%7B%20seconds%7D%20%5Cquad/%5Cquad%2060%20%5Ctext%7B%20seconds%7D%20%3D%201.055671444%5Ctimes10%5E%7B42%7D%20%5Ctext%7B%20minutes%7D%20%5C%5C%201.055671444%5Ctimes10%5E%7B42%7D%20%5Ctext%7B%20minutes%7D%20%5Cquad/%5Cquad%2060%20%5Ctext%7B%20minutes%7D%20%3D%201.759452407%5Ctimes10%5E%7B40%7D%20%5Ctext%7B%20hours%7D%20%5C%5C%201.759452407%5Ctimes10%5E%7B40%7D%20%5Ctext%7B%20hours%7D%20%5Cquad/%5Cquad%2024%20%5Ctext%7B%20hours%7D%20%3D%207.331051694%5Ctimes10%5E%7B38%7D%20%5Ctext%7B%20days%7D%20%5C%5C%207.331051694%5Ctimes10%5E%7B38%7D%20%5Ctext%7B%20days%7D%20%5Cquad/%5Cquad%20360%20%5Ctext%7B%20days%7D%20%3D%202.036403248%5Ctimes10%5E%7B36%7D%20%5Ctext%7B%20years%7D%20%5C%5C) 

Even if you have a computer 10, 100 or 1000 times faster than the example 1 million hashes per second it'd still take way too long. Compared to the **36x32=1152** attempts max it'd take to crack these hashes.

Timing attacks aren't hard to prevent once you know how they work. So just remember this challenge and don't make these kinds of silly mistakes.
