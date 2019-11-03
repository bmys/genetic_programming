import operator
from functools import reduce


def arithmetic(op, vm, args):
    operand1 = vm.variables[args[0]]
    operand2 = vm.variables[args[1]]
    destination = args[2]
    result = reduce(op, [operand1, operand2])
    vm.variables[destination] = result


def mov(vm, *args):
    source = vm.variables[args[0]]
    destination = args[1]
    vm.variables[destination] = source


def skip(vm, *args):
    pass


def mul(vm, *args):
    arithmetic(operator.mul, vm, args)


def div(vm, *args):
    arithmetic(operator.truediv, vm, args)


def add(vm, *args):
    arithmetic(operator.add, vm, args)


def sub(vm, *args):
    arithmetic(operator.sub, vm, args)


def mod(vm, *args):
    arithmetic(operator.mod, vm, args)


def power(vm, *args):
    arithmetic(operator.pow, vm, args)


operations = {
    'ADD': add,
    'SUB': sub,
    'MUL': mul,
    'DIV': div,
    'MOV': mov,
    'SKP': skip
}
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
