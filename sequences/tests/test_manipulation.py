import unittest
from sequences.manipulation import *


class CrossoverSequencesTestCase(unittest.TestCase):
    def test_even_shuffle_same_length(self):
        first_seq = (1, 2, 3, 4)
        second_seq = ('a', 'b', 'c', 'd')
        first_seq, second_seq = crossover_sequences(first_seq, second_seq, odd=False)
        self.assertEqual(first_seq, (1, 'b', 3, 'd'))
        self.assertEqual(second_seq, ('a', 2, 'c', 4))

    def test_odd_shuffle_same_length(self):
        first_seq = (1, 2, 3, 4)
        second_seq = ('a', 'b', 'c', 'd')
        first_seq, second_seq = crossover_sequences(first_seq, second_seq, odd=True)
        self.assertEqual(first_seq, ('a', 2, 'c', 4))
        self.assertEqual(second_seq, (1, 'b', 3, 'd'))


if __name__ == '__main__':
    unittest.main()
