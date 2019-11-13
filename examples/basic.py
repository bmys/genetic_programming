from virtual_machine.vm_register import VmRegister, random_program
from virtual_machine.operations import operations
operations.pop('SKP')

a = operations['MOV']
operations = dict([('MOV', a)])

vm = VmRegister(3, operations)


def create_population(count):
    print(vm.variables.keys())
    for _ in range(count):
        yield list(random_program(list(operations.keys()), 3, 3, list(vm.variables.keys())))


population = list(create_population(10000))

for program in population:
    vm.reset()
    vm.update_variables({'A': 5, 'B': 3})

    try:
        vm.execute(program)
    except ZeroDivisionError:
        pass

    if vm.variables['B'] == 5 and vm.variables['A'] == 3:
        print(program)


# vm.reset()
# vm.update_variables({'A': 2, 'B': 1})
# vm.execute([('SUB', 'B', 'A', 'D'), ('ADD', 'C', 'A', 'B'), ('ADD', 'D', 'A', 'A')])
# print(vm.variables)

class K:
    ...

# swap a and b
# vm.execute([('SUB', 'B', 'A', 'D'), ('ADD', 'C', 'A', 'B'), ('ADD', 'D', 'A', 'A')])
# vm.execute([('SUB', 'B', 'A', 'C'), ('MOV', 'A', 'B'), ('ADD', 'C', 'A', 'A')])
