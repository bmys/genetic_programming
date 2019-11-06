import random
import string
from typing import Sequence
from virtual_machine.vm_base import Vm


class VmRegister(Vm):

    @property
    def program(self):
        return self.program

    @program.setter
    def program(self, pr):
        self.p = pr

    def __init__(self, variable_count: int, instructions):
        self.variables: dict = dict([(i, 0) for i in string.ascii_uppercase[:variable_count]])
        self.p: list = list()
        self.operations = instructions

    def reset(self):
        self.variables = dict.fromkeys(self.variables, 0)
        self.p.clear()

    def execute(self, program):
        for instruction in program:
            operation = self.operations[instruction[0]]
            operands = list(instruction[1:])
            operation(self, *operands)
        return self.variables

    def update_variables(self, variables: dict):
        self.variables.update(variables)


def random_program(operations: Sequence,
                   program_length: int,
                   operands_count: int,
                   variables_names: Sequence):

    for _ in range(program_length):
        operation = random.choice(operations)
        operands = random.choices(variables_names, k=operands_count)
        yield (operation, *operands)
