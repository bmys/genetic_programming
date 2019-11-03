import random
import string
from typing import Sequence
from virtual_machine.vm_base import Vm


class VmRegister(Vm):
    def __init__(self, varc: int, instructions):
        self.variables: dict = dict([(i, 0) for i in string.ascii_uppercase[:varc]])
        self.program: list = list()
        self.operations = instructions

    def reset(self):
        self.variables = dict.fromkeys(self.variables, 0)
        self.program.clear()

    def execute(self, program):
        for instruction in program:
            operation = self.operations[instruction[0]]
            operands = list(instruction[1:])
            operation(self, *operands)
        return self.variables

    def load_vars(self, variables):
        for var in variables:
            self.variables[var[0]] = var[1]


def random_program(operations: Sequence,
                   program_length: int,
                   operands_count: int,
                   variables_names: Sequence):

    for _ in range(program_length):
        operation = random.choice(operations)
        operands = random.choices(variables_names, k=operands_count)
        yield (operation, *operands)

