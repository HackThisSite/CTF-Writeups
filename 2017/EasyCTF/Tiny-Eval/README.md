# Tiny Eval

This page will evaluate anything you give it.


## Solution

We are presented with a website, with a text field, to input our code
that the script will evaluate.

We could try a lot of different languages, but we start with the likely 
candidate first, namely PHP.

In order to check if it indeed evaluate anything we first input
`echo("hello there")`

Here we are told that there are too many characters. So we try with 
shorter and shorter input, untill we figure out it takes max 11 characters

Comming from a perl background there are a few tricks one can try,
one of the most obvious, in order to get your character count down,
is to use backticks, which run the command you enter, in a shell and 
return the result.

Maybe we can list files in the current directory like that?


```
echo`ls`
```

Successfully give us a list of files among which is a file called flag.txt

How can we get a readout of the flag.txt file? Well think linux commands,
and cat comes to mind quickly.

Can we build a command string that will print the flag with cat, in only 11 characters??

```
echo`cat *`
```

Ofcourse we can, and we just did!

Filling in the above command string, gives us the flag:

*easyctf{it's_2017_who_still_uses_php?(jk_82.5%_of_websites)}*

