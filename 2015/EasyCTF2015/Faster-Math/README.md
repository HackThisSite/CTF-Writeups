Description:
Solved by 65 teams.

I need help on my homework! Connect to programming.easyctf.com:10300 where a series of 100 problems await you.

So, the challenge really says it all. This is a programming challenge where we have a series of math related questions. The questions are split into four categories and have variating numerical values. The easiest way to do this is to parse out the numbers for the specific problem and define function for each of the four math problem types.

The four math problem types as stated below:

* Operations -
  Fill the operations (+, -, or x) in the blanks. Return 3 operations separated by nothing: (((23 _ 221) _ 85) _ 243) = -356

* Greater/Lesser Root -
  Find the value of the greater root: 32x^2 + 4384x - 2625216

* Distance -
  A holy grail is projected from the side of a desk at a velocity of 2160 m/s. Given that the desk is 720 m tall, the holy grail is 188 g and the Earth's gravitational constant is 10 m/s^2, calculate the distance from the desk where the holy grail first touches the floor.

* Purchase -
  I was going to the checkout at the pizzeria to pay for my $3.14 purchase, when I discovered that I had left my credit cards at home! Frantically digging through my bag for change, I discovered that I had expendable quantities of nickels, quarters, dollar bills, dimes, and pennies. As I way paying for my purchase, I began to wonder... how many ways could I make $3.14 using just nickels, quarters, dollar bills, dimes, and pennies?

All of these problems will be given in a randomized order, with randomized numerical values. Greater/Lesser Root also varies between well.... Greater and Lesser root as well. Beyond this, another tricky part was that towards the end of the challenges, the purchase problem was giving higher inputs that would in turn be more time consuming to complete (i.e, $90 purchases and lots of coins)

I created a main program to connect to the server with the solutions for operations and distance within the script. Greater/Lesser Root calls an external script called `root.py`, and Purchase calls an external script called `coins.py`. The `math.rb` (main) script returns the values from these programs and sends it to the server like normal. I also have the script logging information being received and sent off to the server, and placed that information inside a file named `server-log.txt`
The server spits out the flag after completion and is: `easyctf{A+_for_A+_eff0rt!}`
