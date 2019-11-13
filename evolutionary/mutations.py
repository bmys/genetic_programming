from typing import Sequence, Callable, Set
from random import randrange
from functools import wraps
from sequences.manipulation import random_change_at_index, \
    random_swap, \
    change_at_index, \
    random_enumerations, \
    change_at_indexes


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
    first_operand_index = randrange(1, len(seq_1))
    second_operand_index = randrange(1, len(seq_2))
    mutated_first_instruction = change_at_index(seq_1, first_operand_index, seq_2[second_operand_index])
    mutated_second_instruction = change_at_index(seq_2, second_operand_index, seq_1[first_operand_index])
    return mutated_first_instruction, mutated_second_instruction


def mutation_change(fun):
    def inner(seq, operands):
        (index, instruction), *_ = random_enumerations(seq, 1)
        mutated_instruction = fun(instruction, operands)
        return change_at_index(seq, index, mutated_instruction)
    return inner


@mutation_change
def mutation_change_operand(instruction, operands):
    random_operand_index = randrange(1, len(instruction))
    mutated_instruction = random_change_at_index(instruction, random_operand_index, operands)
    return mutated_instruction


@mutation_change
def mutation_change_operation(instruction, operations):
    return random_change_at_index(instruction, 0, operations)


def mutation(program: Sequence, mutating_function: Callable, args) -> Sequence:
    ...
