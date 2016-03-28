Description:
Solved by 1325 teams.

We need to get the flag at this site. That shouldn't be too hard.

Upon reviewing the source code, we can see an HTML comment towards the bottom:
```
<!-- you thought the flag would be in the comments didn't you? nice try we're better than that -->
```
This code is directly above a linked JavaScript script named `script.js`
Following this script, we see the following code:
console.log('no one would EVER think to look in the console! flag backup: easyctf{remember_to_check_everywhere}');

The code clearly contains the given flag: `easyctf{remember_to_check_everywhere}`
