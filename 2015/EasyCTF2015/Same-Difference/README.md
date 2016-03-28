Description: Solved by 601 teams.
_Solve this problem by connecting to the EasyCTF shell, either in your browser or through some other TTY._

We've noticed that a list of passwords has been modified. Compare the original `master_copy.txt` to the `suspicious.txt` and tell us what the password was changed to! The files are on the shell server at `/problems/same_difference`.

This can be solved only with the tools available in the shell. No scripting languages are required.


This challenge requires us to solve the challenge using [shell server](https://www.easyctf.com/shell). After logging in, and changing the directory to `/problems/same_difference`, all we had to do was use the command named `diff` as:
`diff master_copy.txt suspicious.txt`

We see that `easyctf{17c85a939e5ee1b0b0e00ed7187d11f7}` was changed to `easyctf{60a57b3974029aa012e66b05f122748b}` which is our flag.
So, the flag was:
`easyctf{60a57b3974029aa012e66b05f122748b}` 
