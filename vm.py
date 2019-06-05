import random
import string

from functools import reduce
import operator
from random import randrange


class Vm:
    def __init__(self, varc: int, operations):
        self.variables: dict = dict([(i, 0) for i in string.ascii_uppercase[:varc]])
        self.program: list = list()
        self.operations = operations

    def reset(self):
        self.variables = dict.fromkeys(self.variables, 0)
        self.program.clear()

    def execute(self, program):
        for instruction in program:
            operation = self.operations[instruction[0]]
            operands = list(instruction[1:])
            operation(self, *operands)


# machine setup

def mov(vm: Vm, *args):
    source = vm.variables[args[0]]
    destination = args[1]
    vm.variables[destination] = source

def skip(vm: Vm, *args):
    pass

# arithmetic

def mul(vm: Vm, *args):
    arithmetic(operator.mul, vm, args)


def div(vm: Vm, *args):
    arithmetic(operator.truediv, vm, args)


def add(vm: Vm, *args):
    arithmetic(operator.add, vm, args)


def sub(vm: Vm, *args):
    arithmetic(operator.sub, vm, args)


def mod(vm: Vm, *args):
    arithmetic(operator.mod, vm, args)


def pow(vm: Vm, *args):
    arithmetic(operator.pow, vm, args)


def arithmetic(op, vm, args):
    operand1 = vm.variables[args[0]]
    operand2 = vm.variables[args[1]]
    destination = args[2]

    result: float = reduce(op, [operand1, operand2])

    vm.variables[destination] = result


def random_program(opp: dict, program_len: int, size: int,varc: list):

    while program_len != 0:
        program_len -= 1
        operation = random.choice(list(opp.keys()))
        operands = random.choices(varc, k=size)
        yield (operation, *operands)


def mutation(program: tuple, instructions: dict, varc):
    program = list(program)
    choices = ('swap', 'change')
    choice = random.choice(choices)

    if choice == 'swap':
        r1 = randrange(len(program))
        r2 = randrange(len(program))
        program[r1], program[r2] = program[r2], program[r1]
        return tuple(program)
    else:
        instruction = randrange(len(program))
        choices = ('operation', 'operand')
        choice = random.choice(choices)

        if choice == 'operation':
            new = list(program[instruction])
            new[0] = random.choice(list(instructions.keys()))
            program[instruction] = tuple(new)
            return program
        else:
            new = list(program[instruction])
            operand = 1 + randrange(len(new) - 1)
            new[operand] = random.choice(varc)
            program[instruction] = tuple(new)
            return program


def crossing_over(program1, program2):
    split_point = 1 + randrange(len(program1)-1)
    program1 = list(program1)[:split_point]
    k = list(program2)[split_point:]
    program1.extend(k)
    return program1

operations = {
    'ADD': add,
    'SUB': sub,
    'MUL': mul,
    'DIV': div,
    'MOV': mov,
    'SKP': skip
}

v = Vm(3, operations)

program = (('ADD', 'A', 'B', 'C'), ('ADD', 'B', 'C', 'A'))
program2 = (('MOV', 'A', 'C'), ('ADD', 'B', 'C', 'A'))
v.execute(program)

# print(f'add: {add(arr)} \n sub: {sub(arr)} \n mul: {mul(arr)} \n div: {div(arr)}')
# print(vm.variables)

"""
ADD
SUB
MUL
DIV *
/ SIN
/ COS
/ SQR *
/ POW

MOV

INC
DEC

JMP 
 

"""

"""
ADD
MUL
LOC
DIV
IFE
IFL
IFG
IFN
TMP
END
MOV
"""
