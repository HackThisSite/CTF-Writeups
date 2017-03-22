Match Me
======
* **300 points**
* **Category: Programming**
* **Hint** This is a fairly well-known graph problem.
I would guess there is some sort of internet source on it.
* **Problem statement below [It's long]**
* **APOLOGIES FOR ANY POTENTIALLY PERCEIVED OFFENSE, NONE INTENDED IT IS THE NATURE OF THE PROBLEM AND DESCRIBING IT**

When making pairings between two sets of objects based on their preferences (in this case people), there can be multiple stable solutions, stable meaning that no two elements would prefer to be matched with each other over their current matching. A side-effect of having multiple solutions is that there are solutions favor one group over the other.

We received two files, one listing men and the other women.
Each line contains a name, followed by a series of numbers.
Each number N corresponds to their preference to be matched with the Nth member of the opposite list, with 1 being the highest.

For example, the entry ``"Joe 4, 5, 3, 1, 2"`` means that Joe would most prefer the 4th entry on the opposite list, and least prefer the 2nd.

We have heard that there are some pairings that will be together in all possible stable matchings, please find them.
However, because there are quite a bit of them, please submit your solution as the following:

MD5 hash of ``(male_1,female_1)(male_2,female_2)...(male_n,female_n)``, where the pairings are sorted alphabetically by male names. For example, ``(Bob,Susie)(Jim,Carol)(Tom,Emma)`` would be submitted as `b0d75104ce4b3a7d892f745fd515fea4`.

Here are the lists of preferences:[male preferences](male), [female preferences](female).

----------------------------

This was a fun programming problem! I had already seen the video https://www.youtube.com/watch?v=Qcv1IqHWAzg (Stable Marriage Problem by Dr Emily Riehl and filmed by Brady Haran from Numberphile) which happened to describe the algorithm to this exact same problem! I encourage watching it.

So the algorithm's description:
Make an array of all the males, and an array of their ranked preferences of women, where the nth element is the nth male.
Also create a map between ID's and their name
Do the same for females and their rankings of men.

Create an array of the men's current pairings, where the nth element is an array of the nth man pairing.
Array has two elements, his personal rank of the woman assigned to him, and that woman's ID.

Then create a list of the ID's of all the unassigned woman. (Currently everyone)
Keep going through the following until this list is empty.

Iterate through all unassigned women and try assigning them to their top choice man. If the man has a better offer, remove the man from that womans list. (Her top choice, so were always looking at her top available choice. This way we don't ever repeat checking the same M/F combo)

If the man has her ranked better than who he is already paired with, kick off the person currently paired with the man, and put her ID in the unassignedWomenIDs. Remove person being paired from unassignedWomenIDs.

That will finish executing, and then you have all the pairs.

Repeat the entire process with man and woman swapped. This gets us the ones that are stable in configurations.
I wasn't sure if some of these combinations would be unstable in different combos, so if this didn't work then I'd find a way to iterate randomly through unassignedWomenIDs to simulate more configurations.
I currently don't know if in theory it is possible to have an input with less stable configurations than what this code will detect.

Compare the results, and keep only the results that are the same.
Format the according string, and MD5 it! Thats your flag!

Pairs:
```
(Adonis,Aja)(Aidan,Eden)(Alvaro,Ciara)(Andres,Melanie)(Anton,Dominique)(Aric,Randi)(Arron,Kathleen)(Austyn,Sonya)(Blair,Suzanne)(Braden,Carlee)(Brayan,Meagan)(Brendan,Karley)(Bret,Dalia)(Brock,Cora)(Brooks,Alaina)(Daron,Bryanna)(Davon,Georgia)(Devan,Doris)(Diamond,Kristi)(Dimitri,Zoe)(Donavan,Arlene)(Edward,Kaitlyn)(Everett,Renee)(Fabian,Leslie)(Francis,Kimberlee)(Frederick,Ashleigh)(Garett,Ashlynn)(Gordon,Krystal)(Grady,Vivian)(Graham,Berenice)(Hugo,Cheyenne)(Irving,Brandi)(Jacoby,Jami)(Jamar,Nicolette)(Jeremy,Sade)(Jordan,Aurora)(Juan,Leanne)(Kane,Miracle)(Keenan,Jerrica)(Lester,Aimee)(Madison,Whitley)(Marshall,Angie)(Melvin,Krista)(Moshe,Amani)(Nathanial,Monika)(Nico,Elsa)(Nicolas,Elaina)(Rocky,Beth)(Roderick,Kasandra)(Shelby,Lexus)(Skylar,Kallie)(Stephan,Shania)(Steve,Marlena)(Stewart,Rita)(Ulysses,Sofia)(Walter,Jaime)
```
MD5 of that ( Our flag):
```
51cacb0258b7862d646964c0da7c6125
```
