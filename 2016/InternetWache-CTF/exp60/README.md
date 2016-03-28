# EquationSolver
> Description: I created a program for an unsolveable equation system. My friend somehow forced it to solve the equations. Can you tell me how he did it?

> Service: 188.166.133.53:12049

# Solution
The server gives as an unsolvable equation:
```
Solve the following equations:
X > 1337
X * 7 + 4 = 1337
Enter the solution X:
```
It is however possible to solve it if we take advantage of how integers work. If some operation on an integer would make it higher than its highest possible value (2,147,483,647 for 32 bit signed integers) it's going to wrap around and add that excessive value to the lowest possible value (-2,147,483,648).

We can use that in our case. 4,294,967,295 is the range of the possible values. If we divide that number by 7 we will get an integer that when multiplied by 7 will equal 0. We also have to add the result of 1333 / 7 to that number.

```
You entered: 613566947
613566947 is bigger than 1337
1337 is equal to 1337
Well done!
IW{Y4Y_0verfl0w}
```
