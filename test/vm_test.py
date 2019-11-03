import unittest
from virtual_machine import Vm
from virtual_machine.operations import operations


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
        v = Vm(3, operations)

        program = (('ADD', 'A', 'B', 'C'), ('ADD', 'B', 'C', 'A'))
        program2 = (('MOV', 'A', 'C'), ('ADD', 'B', 'C', 'A'))
        v.execute(program)


if __name__ == '__main__':
    unittest.main()
