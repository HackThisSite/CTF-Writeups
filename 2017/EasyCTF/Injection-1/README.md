# Injection 1

I need help logging into this website to get my flag! If it helps, my username is admin.

Running sqlmap or the likes will earn you an IP ban.

## Solution

A classic sql injection problem, which should be fairly easy to tackle.

We are supposed to login as admin, so we put that into the username field

The sql the server preforms should look something like this:

```
select * from users where username="admin" and password=""
```

In order for this to be fooled to log us in, we need to craft something from
the password field, that make the sql statement true.

In our case we want a balanced injection, so we do not rely on commenting out
the rest of the injection as is common, with ;-- or #

To obtain this goal, our password field will have to contain the following:

```
" or "a"="a
```

This will make the sql in the backend script, look something like this,
with admin as the username:

```
select * from users where username="admin" and password="" or "a"="a"
```

This will present us with the flag which is:

*easyctf{a_prepared_statement_a_day_keeps_the_d0ctor_away!}*


