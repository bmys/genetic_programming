from typing import Sequence, Callable, Set
from sequences.manipulation import random_change_at_index, \
    random_swap, \
    get_random_index, \
    change_at_index, \
    get_random_indexes, \
    random_enumerations, \
    change_at_indexes
from random import randint


def mutation_swap(sequence: Sequence, mutation_function: Callable) -> Sequence:
    (first_index, first_instruction), (second_index, second_instruction) = random_enumerations(sequence, 2)
    # mutated_first, mutated_second = map(mutation_function, (first_instruction, second_instruction))
    mutated_first, mutated_second = mutation_function(first_instruction, second_instruction)
    return change_at_indexes(sequence, (first_index, mutated_first), (second_index, mutated_second))


def mutation_swap_instructions(program: Sequence) -> Sequence:
    return random_swap(program)


def mutation_swap_operation(program: Sequence) -> Sequence:

    def swap_operations(seq_1, seq_2):
        mutated_first_instruction = seq_2[0] + seq_1[1:]
        mutated_second_instruction = seq_1[0] + seq_2[1:]
        return mutated_first_instruction, mutated_second_instruction

    return mutation_swap(program, swap_operations)


def mutation_swap_operands(program: Sequence) -> Sequence:

    def swap_operands(seq_1, seq_2):
        mutated_first_instruction = change_at_index(seq_2, 0, seq_1[0])
        mutated_second_instruction = change_at_index(seq_1, 0, seq_2[0])
        return mutated_first_instruction, mutated_second_instruction

    return mutation_swap(program, swap_operands)


def mutation_swap_operand(program: Sequence) -> Sequence:

    def swap_operand(seq_1, seq_2):
        first_operand_index = randint(1, len(seq_1) - 1)
        second_operand_index = randint(1, len(seq_2) - 1)
        mutated_first_instruction = change_at_index(seq_1, first_operand_index, seq_2[second_operand_index])
        mutated_second_instruction = change_at_index(seq_2, second_operand_index, seq_1[first_operand_index])
        return mutated_first_instruction, mutated_second_instruction

    return mutation_swap(program, swap_operand)


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
