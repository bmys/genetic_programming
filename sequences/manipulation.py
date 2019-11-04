from random import randrange, choice, sample
from typing import Sequence, Tuple, Set, Any, Iterable
from itertools import chain, tee, zip_longest


def concat_sequence(sequence: Sequence, *args) -> Sequence:
    concat = chain.from_iterable(args)
    if hasattr(sequence, 'join'):
        return ''.join(concat)
    else:
        return type(sequence)(concat)


def random_enumerations(seq: Sequence, count: int) -> Tuple[Tuple[int, Any], ...]:
    indexes = get_random_indexes(seq, count)
    return tuple((idx, seq[idx]) for idx in indexes)


def get_random_indexes(seq: Sequence, count: int) -> Tuple[int, ...]:
    """
    Return tuple of n random indexes from range 0 to length of sequence
    :param seq:
    :param count:
    :return Tuple[int]:
    """
    return sample(range(len(seq)), count)


def get_random_index(seq: Sequence) -> int:
    """
    Return random index from sequence
    :param seq:
    :return int:
    """
    return randrange(len(seq))


def swap_elements(seq: Sequence, indexes: Tuple[int]) -> Sequence:
    """
    Return sequence of type seq with swapped elements at given indexes
    :param seq:
    :param indexes:
    :return:
    """
    assert len(indexes) == 2, "Indexes length not equal 2"
    mi, mx = min(indexes), max(indexes)
    assert mi >= 0 or mx >= len(seq), 'Indexes are out of bounds'
    head, between, tail = seq[:mi], seq[mi+1:mx], seq[mx+1:]
    return concat_sequence(seq, head, (seq[mx],), between, (seq[mi],),  tail)


def random_swap(seq: Sequence) -> Sequence:
    """
    Random swap two elements from sequence
    :param seq:
    :return:
    """
    indexes = get_random_indexes(seq, 2)
    return swap_elements(seq, indexes)


def change_at_index(sequence: Sequence, index: int, element: Any) -> Sequence:
    """
    Return new sequence created from sequence with replaced element at given index with given element
    :param sequence:
    :param index:
    :param element:
    :return:
    """
    if index >= len(sequence) or len(sequence) < 0:
        raise ValueError('Index should be in range from 0 to length of sequence - 1 ')
    return concat_sequence(sequence, sequence[:index], (element, ), sequence[index+1:])


def change_at_indexes(sequence: Sequence, *enumerations: Tuple[int, Any]) -> Sequence:
    for idx, elem in enumerations:
        sequence = change_at_index(sequence, idx, elem)
    return sequence


def random_change_at_index(sequence: Sequence, index: int, source: Set) -> Sequence:
    to_choose = source.copy()
    to_choose.discard(sequence[index])
    chosen = choice(to_choose)
    return change_at_index(sequence, index, chosen)


def pair_wise(iterable: Iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def random_slices(seq, n) -> Tuple[Tuple[Any, Any]]:
    assert len(seq) >= n, 'n is larger than length of sequence'
    length = len(seq)
    split_indexes = [0] + list(sample(range(1, length), k=n-1)) + [length]
    split_indexes = sorted(split_indexes)
    slices = tuple(pair_wise(split_indexes))
    return slices


def split_at_points(seq, split_points):
    for point in split_points:
        sl = slice(*point)
        yield seq[sl]


def odd_elements(seq: Sequence) -> Sequence:
    """
    Return sequence created from odd elements from seq
    :param seq:
    :return:
    """
    return seq[0::2]


def even_elements(seq: Sequence) -> Sequence:
    """
    Return sequence created from even elements from seq
    :param seq:
    :return:
    """
    return seq[1::2]


def crossover_sequences(seq_1: Sequence, seq_2: Sequence, odd: bool = False):

    seq_1_odd_elements, seq_1_even_elements = odd_elements(seq_1), even_elements(seq_1)
    seq_2_odd_elements, seq_2_even_elements = odd_elements(seq_2), even_elements(seq_2)

    if odd:
        seq_1_processed = zip_longest(seq_2_odd_elements, seq_1_even_elements)
        seq_2_processed = zip_longest(seq_1_odd_elements, seq_2_even_elements)
    else:
        seq_1_processed = zip_longest(seq_1_odd_elements, seq_2_even_elements)
        seq_2_processed = zip_longest(seq_2_odd_elements, seq_1_even_elements)

    seq_1_processed = filter(lambda x: x is not None, chain(*seq_1_processed))
    seq_2_processed = filter(lambda x: x is not None, chain(*seq_2_processed))

    return concat_sequence(seq_1, seq_1_processed), concat_sequence(seq_2, seq_2_processed)
