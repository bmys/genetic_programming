import string

from functools import reduce
import operator


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

operations = {
    'ADD': add,
    'SUB': sub,
    'MUL': mul,
    'DIV': div,
    'MOV': mov
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
