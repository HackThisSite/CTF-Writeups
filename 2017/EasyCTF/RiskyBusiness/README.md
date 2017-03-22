# Risky Business


We wanted to branch into the casino business, but human employees are too expensive so we decided to automate it. I feel like we missed something obvious though... Oh well! Here's the binary: casino

Solve this problem by logging into the shell server and navigating to /problems/casino.


## Solution

We login to the shell server and before anything else, we run the binary and figure
out that its a game where you have to enter the amount you wish to bet, from 1 to 100000000.

The twist is that you are still allowed to play when you go negative on your bankroll.

Doing a few spins and with no suprise we see that we loose a lot more than we are winning.

We could take a look at the binary through gdb, but already we got a lot of hints to
move forward with

* The game is programmed in C/C++
* You can have a negative bankroll
* You have unlimited tries.

We assume that the bankroll is kept internally as a long, which as we can see from going
negative is signed, so we can assume that it can go to −2,147,483,647 before overflowing
to positive.

We test out our thesis and after around 30 bets of 100000000, we overflow the long and
are left with aorund 2000000000 credits, after which we are told we are special, and 
get the flag!

*easyctf{m4by3_w3_c0u1d_h4v3_d0n3_th47_b3t7er}*
