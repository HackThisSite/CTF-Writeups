## Weird Counting
* Cryptography
* Kyle has invented a new language! Here are the numbers one through 16. What is nalazofa in base 10?
* Computational Linguistics is a very interesting field. Try looking for patterns in the counting system.
*　150 points

First look at the problem text.

My Observations:

* Even numbers end with a, and odd numbers end with o.
* All powers of 2 were only 2 letter "words/numbers", i.e. zo = 2^0 = 1, fa = 2^1 = 2, la = 2^2 = 4 and etc.

* Each prime number is fa plus (n-1) zo's, where n is which prime it is. (i.e. 2 = 1st prime, 3 = 2nd prime, 5 = 3rd prime and so on)
* If you divide a number by 2, the fa at the end becomes a zo. This meant that the final digit was that number's multiple of 2!!!

So the final digit meant how many multiple of 2 it had! zo means its multiplied by 2, 0 times (2^0), fa means that it is multiplied by 2, 1 time, (2^1), and la means multiplied by 2, 2 times and so on. (The la can be seen in fala)

9 then, is fazo (3) Squared and is written as lazo. This implies that the second digit(counting from the right) is how many multiples of 3 it has. 3 also happens to be the second prime. 
so fazo means 3^1 * 2^0. From this we have that the numbers in this writing system give you the prime factorization, and the digit tells you what power that prime is raised to!

So to answer the question: What is nalazofa in base 10?
this is equal then to 
`nazozozo * lazozo * zozo * fa `
                    
`= (4th prime)^4 * (3rd prime)^2 * first prime`
`= 7^4 * 5^2 * 2^1 = 120050`!! (This is the right answer)
