from typing import Sequence, Callable, Set
from sequences.manipulation import random_change_at_index, \
    random_swap, \
    get_random_index, \
    change_at_index, \
    get_random_indexes
from random import randint


def mutation_swap_instructions(program: Sequence) -> Sequence:
    return random_swap(program)


def mutation_swap_operation(program: Sequence) -> Sequence:
    first_index, second_index = get_random_indexes(program, 2)
    first_instruction, second_instruction = program[first_index], program[second_index]
    operation_first_instruction, operation_second_instruction = first_instruction[0], second_instruction[0]

    mutated_first_instruction = change_at_index(first_instruction, 0, operation_second_instruction)
    mutated_second_instruction = change_at_index(operation_second_instruction, 0, operation_first_instruction)

    mutated_program = change_at_index(program, first_index, mutated_first_instruction)
    mutated_program = change_at_index(mutated_program, second_index, mutated_second_instruction)

    return mutated_program


def mutation_swap_operands(program: Sequence) -> Sequence:
    first_index, second_index = get_random_indexes(program, 2)
    first_instruction, second_instruction = program[first_index], program[second_index]
    operation_first_instruction, operation_second_instruction = first_instruction[0], second_instruction[0]

    mutated_first_instruction = change_at_index(first_instruction, 0, operation_second_instruction)
    mutated_second_instruction = change_at_index(operation_second_instruction, 0, operation_first_instruction)

    mutated_program = change_at_index(program, first_index, mutated_second_instruction)
    mutated_program = change_at_index(mutated_program, second_index, mutated_first_instruction)

    return mutated_program


def mutation_swap_operand(program: Sequence) -> Sequence:
    first_index, second_index = get_random_indexes(program, 2)
    first_instruction, second_instruction = program[first_index], program[second_index]

    first_operand_index = randint(1, len(first_instruction))
    second_operand_index = randint(1, len(second_instruction))

    mutated_first_instruction = change_at_index(first_instruction, first_operand_index, second_instruction[second_operand_index])
    mutated_second_instruction = change_at_index(second_instruction, second_operand_index, first_instruction[first_operand_index])

    mutated_program = change_at_index(program, first_index, mutated_second_instruction)
    mutated_program = change_at_index(mutated_program, second_index, mutated_first_instruction)

    return mutated_program


def mutation_change_operand(program: Sequence, operands: Set) -> Sequence:
    index = get_random_index(program)
    instruction = program[index]

    random_operand_index = randint(1, len(instruction))

    mutated_instruction = random_change_at_index(instruction, random_operand_index, operands)
    return change_at_index(program, index, mutated_instruction)


def mutation_change_operation(program: Sequence, operations: Set) -> Sequence:
    index = get_random_index(program)
    instruction = program[index]
    mutated_instruction = random_change_at_index(instruction, 0, operations)
    return change_at_index(program, index, mutated_instruction)


def mutation(program: Sequence, mutating_function: Callable, args) -> Sequence:
    ...
