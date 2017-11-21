# Injection 2

```
I've told my friend a billion times that the user called leet1337 doesn't exist on this website, but he won't listen. Could you please login as this user, even though it doesn't exist in the database? Oh and also, make sure that the user has a power level over 9000!!!!

Running sqlmap or the likes will earn you an IP ban.
```

*hint: The columns in the table are (not in order) username, password, power_level, and a unique id.*


## Solution

As any good crossword puzzle, sql injections, wether in the wild or as part of a CTF,
are best solved manually.

We start by the usual by filling in " or ' into the password field to see if we
get any talk from the underlying script about sql errors.

We dont get any information, so we must assume that this is a blind or semi blind
sql injection. Its all good, we got a lot of information to work with.

* The query should return 4 columns: username, password, power_level, id
* Order matters somewhat, we can assume that atlease username and power_level should be correctly placed in the query
* The username we need to login with IS NOT in the database!

We need for the backend to select 0 rows, so we keep our ussername field blank in the html form.
The password field will be where we put our injection code, we start that string with " so we basically tell the
backend script to execute this query

select username, password, power_level, id from some-table where username="" and password="(our sql string)"

When the backend returns 0 rows, we need to figure out some way to return something more, which is what "union select"
does, basically its a select after the initial select which piles on rows of data to the original query.
It has to contain the same number of columns as the select statement before it.

We need 1 row with the fields/columns username, password, power_level, id.

So that will be a union select which looks something like this

`union select sleep(5),"leet1337","leet1337",9001`

The reason we use sleep(5), is just to indicate to us wether or not our  injection is accepted or not,
if you get a timeout of 5+ seconds before the result, you know it atleast understood your injection and
didn't crash without telling you about it.

Problem with the above injection is, that its not closed and the value 9001 is an integer value.
using the above injection the full sql from the backend servers point of view would be,
something like:

assuming our username field holds nothing and our password field holds:
*" union select sleep(5),"leet1337","leet1337",9001*

```
select username, password, power_level, id from some-table where username="" and password="" union select sleep(5),"leet1337","leet1337",9001"

```

As we can see the sql injection is not "closed" so it will not work like this, we need to account for the ending
"-character. We do this by adding a where clause to our injection, but as we do not know the name of the table we
work with, we can use a mysql build in table in the INFORMATION_SCHEMA database called COLUMNS.
It basically contain the data of each column of each database in the system.

We know plenty of column names, so we just choose to use the one called password.

Our full injection into the password field will now be:

```
" union select sleep(5),"leet1337","leet1337",9001 from INFORMATION_SCHEMA.COLUMNS where COLUMN_NAME="password
```

This will make our injection terminate with grace, as the "-character will now close our statement COLUMN_NAME="password

In some instances you'd be able to terminate the sql injection with ;-- so you wouldnt need to make it
complete, it was not tested in this mission if this was the case, as elegance is always prefered to a
by-chance crude injection.

Basically our injection selects the set field values we need, which arent dependant on any table by itself, but use
the table COLUMNS in order to select atleast 1 record which is what we need.

The column position of the union select was ofcourse based on trial and error, so in the end we got it all
to match, within a few tries.

The flag will be shown when you execute the above injection.

username=""
password=" union select sleep(5),"leet1337","leet1337",9001 from INFORMATION_SCHEMA.COLUMNS where COLUMN_NAME="password"

*Sorry i forgot to write the flag down*

