#!/usr/bin/python2
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
