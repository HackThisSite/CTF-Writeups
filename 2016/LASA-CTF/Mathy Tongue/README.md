   ## Mathy Tongue
* Cryptography
* Given {{url_for(\"problem2.txt\", display=\"this\")}} information, what is zokalal + namekalal?
* All the math symbols have the same functionality, so 2+3=5 and 2*3=6. Good luck!
* 170 points

Problem File
```
You walk into a math classroom and find the following equations on the chalkboard:
nadokalol * mekalal = nadokalkalol
pekalol + mekalal = sakalal
namekalal + fanamekalol = mekalal
dokalkalol - namekalal = fanavodokalkalal
namekalal * dokalol = fanamekalol * pekalol
lokalal * mekalal = lokalkalal
pekalol + pekalol + mekalal - lokalal = rekalol
sakalkalal * pekalol = gokalkalkalol
dokalol = sakalal + mekalal
pekalol + pekalol - sakalal - mekalal = rekalol
lokalal - pekalol = sakalal
nadokalol * nalokalal = nafanavolokalkalkalol
namekalal + namekalal = fanamekalol
fanamekalol * mekalal = pekalol
zokalal + pekalol = sakalkalal
In addition, it appears that someone was counting in this system. They erased most of their writing; however, the following numbers were not erased, and are found in the following order with no lines in between them:

lokalal
nagokalol
fanagokalal
gokalol
nazokalal
fanazokalol
zokalal
```
Note: I worked on this with NETWORKSecurity!

This problem begins with lots of algebraic simplification.

First I saw that 

```namekalal + namekalal = fanamekalol```, so ```2namekalal = fanamekalol ```


and then: ```namekalal + fanamekalol = mekalal ```, therefore
``` 3namekalal = mekalal```
I went ahead and replaced all remaining equations in terms of namekalal then, since the question asked for namekalal + another number.
I also went ahead and simplified a couple of the equations, i.e. combining 2 pekalols into "2pekalol"
```
nadokalol * 3namekalal = nadokalkalol
pekalol + 3namekalal = sakalal
dokalkalol - namekalal = fanavodokalkalal
namekalal * dokalol = fanamekalol * pekalol
lokalal * mekalal = lokalkalal
2pekalol + 3namekalal - lokalal = rekalol
sakalkalal * pekalol = gokalkalkalol
dokalol = sakalal + 3namekalal
2pekalol - sakalal - 3namekalal = rekalol
lokalal - pekalol = sakalal
nadokalol * nalokalal = nafanavolokalkalkalol
2namekalal * 3namekalal = pekalol 
zokalal + pekalol = sakalkalal
```

```2namekalal * 3namekalal = pekalol ``` therefore ```6 (namekalal^2) = pekalol.```


Now substitute
```sakalal = pekalol + 3namekalal```
into
```2pekalol - sakalal - 3namekalal = rekalol```

which gives:
```2pekalol - pekalol - 3namekalal - 3namekalal = rekalol```

soo
```pekalol - 6namekelal = rekalol```

From the equation
```lokalal - pekalol = sakalal```

you get, ```lokalal = sakalal + pekalol```

substituting this value for lokalal into:
```2pekalol + 3namekalal - lokalal = rekalol```

gives ```2pekalol + 3namekalal - pekalol - sakalal = rekalol```

Substitute sakalal, you get:```pekalol + 3 namekalal - pekalol - 3namekalal = rekalol```

```0 = rekalol```

Substitute this into previously obtained equation
```pekalol - 6namkelal = rekalol = 0```
therefore ```pekalol = 6namekalal```
but!
```6 (namekalal^2) = pekalol```
therefore **namekalal = 1, and pekalol = 6!!!**

from this the following values can be easily derived from the above equations.
```
rekalol					0
namekalal				1
fanamekalol				2
mekalal					3
pekalol					6
sakalal					9
dokalol					12
lokalal					15
gokalol					18      *NOTE, the derivation of gokalol will be explained below
zokalal					21			
```
The first thing I noticed is that lal means odd, and lol means even!

Notice these 2 very similar equations:
```
nadokalol * mekalal = nadokalkalol
lokalal * mekalal = lokalkalal
```
a number times mekalal means you add an extra kal to the number, therefore an extra kal means "that number, times 3"

```sakalkalal * pekalol = gokalkalkalol```

then means
```3sakalal * pekalol = 9gokalol```
3*9 * 6 = 9 * gokalol
18 = gokalol

This same understanding of kal will explain why zokalal is 21.

Now it is time to look at the second part of the file, the counting lines.
```
In addition, it appears that someone was counting in this system. They erased most of their writing; however, the following numbers were not erased, and are found in the following order with no lines in between them:

lokalal					(We know is 15)
nagokalol
fanagokalal
gokalol					(We know is 18)
nazokalal
fanazokalol
zokalal					(We know is 21)
```
This seems to imply the numbers are in an arithmetic series, and if we fill in the blanks a bit we get
```
lokalal					(We know is 15)
nagokalol				16
fanagokalal				17
gokalol					(We know is 18)
nazokalal				19
fanazokalol				20
zokalal					(We know is 21)
```
This implies that na means "Whatever comes after it minus 2", and fana means "Whatever comes after it, minus 1"
this works for fanamekalol and namekalal, as they can be interpreted as mekalal -1, and -2 respectively.

From our equations in which we determined what an extra kal meant,
```
nadokalol * mekalal = nadokalkalol
lokalal * mekalal = lokalkalal
```
```nadokalol * mekalal = nadokalkalol```
which means the the na subtracts from the dokalol, before it is multiplied by 3. This is important to note.


From all this we can figure out that our answer(namekalal+zokalal) is equal to (1+21) = 22!
Now we just need to figure out how to write 22 in this language!


Equations left:
```
dokalkalol - namekalal = fanavodokalkalal
nadokalol * nalokalal = nafanavolokalkalkalol
```
Lets start with the first one, aince it looks smaller
dokalkalol - namekalal = fanavodokalkalal
12*3 - 1 = 35
so:
fanavodokalkalal = 35

*Note, to be perfectly honest, I have solved this problem, and I have absolutely no idea what the vo means.*

We know that dokalkalal = 36, and vo does some sort of prefix like thing(Possibly just be a placeholder?),
so the nafa only subtracts from the 36. (I.e. It does not subtract from dokalal before multiplying by 3 for the extra kal)
So by adding an extra prefix, the first prefix does whatever to the dokalol before multiplying by 3, and then the fana comes into effect after multiplication.

Lets now try to answer the question.

We need to obtain 22 from only these numbers:

```
0
1
2
3
6
9
12
15
18
21
```
and these operations: ```-1,-2, *3.```
```
22 = 24-2
24=8*3
8 = fanasakalol
24 = fanasakalkalol
22 then equals nafanasakalkalol!!!
```
This was a tough, but fun problem!
