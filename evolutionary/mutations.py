from typing import Sequence, Callable, Set
from sequences.manipulation import random_change_at_index, \
    random_swap, \
    change_at_index, \
    random_enumerations, \
    change_at_indexes
from random import randint


def mutation_swap(mutation_function):
    def inner(sequence):
        (first_index, first_instruction), (second_index, second_instruction) = random_enumerations(sequence, 2)
        mutated_first, mutated_second = mutation_function(first_instruction, second_instruction)
        return change_at_indexes(sequence, (first_index, mutated_first), (second_index, mutated_second))
    return inner


def mutation_swap_instructions(program: Sequence) -> Sequence:
    return random_swap(program)


@mutation_swap
def mutation_swap_operation(seq_1, seq_2):
    mutated_first_instruction = change_at_index(seq_1, 0, seq_2[0])
    mutated_second_instruction = change_at_index(seq_2, 0, seq_1[0])
    return mutated_first_instruction, mutated_second_instruction


@mutation_swap
def mutation_swap_operands(seq_1, seq_2):
    mutated_first_instruction = change_at_index(seq_2, 0, seq_1[0])
    mutated_second_instruction = change_at_index(seq_1, 0, seq_2[0])
    return mutated_first_instruction, mutated_second_instruction


@mutation_swap
def mutation_swap_operand(seq_1, seq_2) -> Sequence:
    first_operand_index = randint(1, len(seq_1) - 1)
    second_operand_index = randint(1, len(seq_2) - 1)
    mutated_first_instruction = change_at_index(seq_1, first_operand_index, seq_2[second_operand_index])
    mutated_second_instruction = change_at_index(seq_2, second_operand_index, seq_1[first_operand_index])
    return mutated_first_instruction, mutated_second_instruction


def mutation_change_operand(program: Sequence, operands: Set) -> Sequence:
    index, instruction = random_enumerations(program, 1)
    random_operand_index = randint(1, len(instruction))
    mutated_instruction = random_change_at_index(instruction, random_operand_index, operands)
    return change_at_index(program, index, mutated_instruction)


def mutation_change_operation(program: Sequence, operations: Set) -> Sequence:
    index, instruction = random_enumerations(program, 1)
    mutated_instruction = random_change_at_index(instruction, 0, operations)
    return change_at_index(program, index, mutated_instruction)


def mutation(program: Sequence, mutating_function: Callable, args) -> Sequence:
    ...
