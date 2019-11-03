

def crossing_over(program1, program2):
    split_point = 1 + randrange(len(program1)-1)
    program1 = list(program1)[:split_point]
    k = list(program2)[split_point:]
    program1.extend(k)
    return program1


class Evolution:
    def __init__(self, population_size, population_creator, mutation_rate, crossing_over_rate):
        self.mutation_rate = mutation_rate
        self.crossing_over_rate = crossing_over_rate
        self.population_creator = population_creator
        self.population = population_creator.create(population_size)
