Phunky Python 2
======
* **115 points **
* **Category: Reverse Engineering**
* **Problem statement:** _We stumbled across another phunky Python file. Can you find the redacted value of jkx that makes this program print True?_
* **Problem hint:** _No hint_

So were given a super weird python 2 file, _phunky2.py_. To unravel this, lets start from the beggining.
``` python
pork = ((12*jkx+44)/4)-(1234/617)*jkx-sum([1, 4, 7])
pork = (3*jkx+11)-(1234/617)*jkx-12
pork = 3*jkx+11-2*jkx-12
pork = jkx - 1
```
In the next line jkx is multiplied by this value so that becomes
``` python
jkx = jkx*(jkx-1)
```
Now lets look at the next line
``` python
pp = filter(lambda g: not any(g % u == 0 for u in range(2, g)), range(2, 10000))
```
What filter does, is it essentially selects everything from the list in the second parameter that meets the criterion of the first parameter.
So the second parameter is just all numbers less than 10k
The first parameter is
``` python
lambda g: not any(g % u == 0 for u in range(2, g))
```
g, where g is any number that isn't divisible by any u, where u is a number less than g.
In other words, g is a number that isn't divisible by any number less than it, aside from 1. Wait thats a prime!

So the code is selecting all prime numbers less than 10000 and storing that in pp!

The next line is:
``` python
b = reduce(operator.mul, (pp[i] ** int(str(jkx)[i]) for i in range(len(str(jkx)))))

```
What reduce does is it applies the function in the first parameter to every element in the second parameter. So in this case its multiplying every element in the second parameter together. `reduce` was actually removed in python3, since its essentially a for loop.

The second parameter is raising pp[i] to the power of the ith digit in jkx. Since pp[i] is the ith prime of, and were multiplying every value in this list together, this is actually defining a prime factorization! The digits in jkx are defining the exponents of the prime factorization.

So then the solution is simple, we have to find the prime factorization of what b is supposed to be equal to, and then the exponents concatenated are jkx! Well its not quite that simple, since we want the original value of jkx, and it gets reassigned in the code to `jkx = jkx*(jkx-1)`
Lets call the original jkx "jkx", and call the jkx after this assignment "jkx2"

Since the range of the for loop for b is actually based on the length of the jkx2, we can add as many 0's as we want to the end of jkx2. So once we have the factorization we can keep adding zeroes to the end of jkx2 (multiplying it by 10), until it is of the form (jkx)(jkx-1), and then jkx is our solution! To test that it is of this, try `jkx2 == floorSqrt(jkx2)*(1+floorSqrt(jkx2))`, multiplying jkx2 by 10 until true! Then `jkx=1+floorSqrt(jkx2)` This is coded in solver.py
``` python
$ python solver.py
exponents = [4, 6, 4, 2, 6, 8, 7, 9, 5, 5, 0, 0, 5, 4, 7, 2, 5, 0, 2, 3, 6, 7, 5, 8, 2, 1, 2, 6, 4, 3, 9, 4, 5, 6, 7]
jkx2 = 464268795500547250236758212643945670
jkx  = 681372728761980355

```
Fun and easy deobfuscation problem!
