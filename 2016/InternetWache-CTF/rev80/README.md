# Eso Tape
>Description: I once took a nap on my keyboard. I dreamed of a brand new language, but I could not decipher it nor get its meaning. Can you help me? Hint: Replace the spaces with either '{' or '}' in the solution. Hint: Interpreters don't help. Operations write to the current index.

>Attachment: rev80.zip

## Solution
The file provided was `priner.tb` and it contained this apparently nonsense string:

```
## %% %++ %++ %++ %# *&* @** %# **&* ***-* ***-* %++ %++ @*** *-* @*** @** *+** @*** ***+* @*** **+** ***+* %++ @*** #% %% %++ %++ %++ %++ @* %# %++ %++ %++ %% *&** @* @*** *-** @* %# %++ @** *-** *-** **-*** **-*** **-*** @** @*** #% %% %++ %++ %++ %++ %# *+** %++ @** @* %# *+** @*** ## %% @***
```

After doing some research we find that the above text is actually a program written in TapeBagel, an esoteric programming language. The task here is to write an interpreter for this language and see what the program does. Here follows a summary of the relevant part of how TapeBagel works:
```
TapeBagel is a language with a pointer and three registers.
The pointer can be incremented or zeroed and it points to one of the three registers.
Every operation executed stores it's return value into the register the pointer currently points to.

Commands:
##  - clear all three registers
%%  - zero the pointer
%#  - increment the pointer
#%  - set all three registers to 1
&&  - pause the program
&@  - clear the screen
%++ - increment the current register

Operators:
&  - multiply
+  - sum
$  - divide
-  - subtract
@  - print integer as character (1->A, 2->b, ... , 26->Z)
@@ - print integer as integer

Operands:
*   - value stored in the first register
**  - value stored in the second register
*** - value stored in the third register

Examples:
*+** - sums the value stored in register 1 with the value stored in register 2 and stores the result in the register the pointer is currently pointing to.
**$* - divides the value in register 2 by the value in register 1 and stores the value to the register the pointer is currently pointing to.
@*   - prints the value in register 1 as a character
@@*** - prints the value in register 3 as an integer
```

There is more to TapeBagel than that, but this is more than enough for this mission.
So, all we have to do is implement the basic functionality of TapeBagel and feed it the given program:

```python
import sys

# define tape bagel class
class tape_bagel():

    # commands
    def zero_ptr(self):
        self.ptr = 0
    def increment_ptr(self):
        self.ptr += 1
    def dafuq(self):
        pass
    def set_regs_1(self):
        self.registers = [1, 1, 1]
    def pause(self):
        pass
    def clear_screen(self):
        pass
    def increment_reg(self):
        self.registers[self.ptr] += 1
    def zero_regs(self):
        self.registers = [0, 0, 0]

    # operations
    def multiply(self, ops):
        op1 = self.registers[ops[0]]
        op2 = self.registers[ops[1]]
        self.registers[self.ptr] = op1 * op2

    def sum(self, ops):
        op1 = self.registers[ops[0]]
        op2 = self.registers[ops[1]]
        self.registers[self.ptr] = op1 + op2

    def divide(self, ops):
        op1 = self.registers[ops[0]]
        op2 = self.registers[ops[1]]
        self.registers[self.ptr] = op1 / op2

    def subtract(self, ops):
        op1 = self.registers[ops[0]]
        op2 = self.registers[ops[1]]
        self.registers[self.ptr] = op1 - op2

    def print_char(self, ops):
        i = self.registers[ops[1]]
        char = chr(i+64) if (i > 0 and i < 26) else ' '
        sys.stdout.write(char)

    def print_int(self, ops):
        s = str(self.registers[ops[1]])
        sys.stdout.write(s)

    # dict containing commands
    commands = {
    '%%':zero_ptr,
    '%#':increment_ptr,
    '%&':dafuq,
    '#%':set_regs_1,
    '&&':pause,
    '&@':clear_screen,
    '%++':increment_reg,
    '##':zero_regs
    }

    # dict containing operations
    operations = {
    '&':multiply,
    '+':sum,
    '$':divide,
    '-':subtract,
    '@':print_char,
    '@@':print_int
    }

    def __init__(self):
        self.ptr = 0
        self.registers = [0, 0, 0]

    def execute(self, cmd):
        for i in cmd:
            if i in self.commands:
                self.commands[i](self)
            else:
                oper = lambda s: s.strip('*')
                ops = lambda s: s.split(oper(s))
                opreg = lambda s, i: len(ops(s)[i])-1
                self.operations[oper(i)](self, [opreg(i, 0), opreg(i, 1)])

def interactive_mode(tape):
    print tape.ptr, tape.registers
    while True:
        command = raw_input("tb>> ").strip().split()
        tape.execute(command)
        print tape.ptr, tape.registers


def pipeline_mode(tape):
    command = sys.stdin.read().strip().split()
    tape.execute(command)

def main():
    tape = tape_bagel() #create tape object

    if '-' in sys.argv: # read from stdin until EOF
        pipeline_mode(tape)

    else:
        interactive_mode(tape)

### Entry point ###
main()
```

Running the given program with the above python script gives the flag:

`IW ILOVETAPEBAGEL `

As the hint suggested, we substitute the spaces with '{' and '}' to get the correct flag format:
`IW{ILOVETAPEBAGEL}`
