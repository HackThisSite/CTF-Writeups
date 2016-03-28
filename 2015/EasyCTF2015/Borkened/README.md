Description: Solved by 63 teams.
There's a team that's breaking the rules and hiding flags on this site! Find the flag.

Description tells us that the flag is somewhere within the site. But where?
First of all, we thought what were the rules that the team broke. To know more about it, we went to their [Rules and Prizes](https://www.easyctf.com/rules) section.
Viewing the source code and searching for the flag format `easyctf{...}`, we found this: `easyctf{example_flag}`. It's a false flag but we get our first Easter egg here. 

Now, we focus our attention to "team". There's one place where all the teams are listed and that is [Scoreboard](https://www.easyctf.com/scoreboard).
We first tried viewing the source code to see if we can find the flag. But no luck. Now we turned to Google Chrome's Inspect Element devtool.
After looking for a bit, we saw a line that was commented out under `<tbody id="scoreboardtable_body">` as:

```<!-- <tr><td>0</td><td><a href='/team?EasyCTF'>EasyCTF</a></td><td>Various Schools</td><td>Infinity</td></tr> -->```

We now jumped over to the team [page](https://www.easyctf.com/team?EasyCTF) for EasyCTF. After looking around for a bit on the Console, we saw "Object" amidst of various warning and errors. Turns out that this was a JSON file which was used to render all the information about the team. We began looking into it and found our flag under the name 'secret' which was:
`easyctf{h4xxing_th3_c0mpetition_s1t3}`
