from operator import attrgetter
from random import random

class Individual:
    def __init__(self, representation=None, size=None, valid_set=None, repetition=True, prefilled=None):
        if representation is None:
            if repetition:
                self.representation = [random.choice(valid_set) for _ in range(size)]
            else:
                self.representation = random.sample(valid_set, size)
        else:
            self.representation = representation
            size = len(representation)  # Ensure size is set if representation is provided

        self.size = size
        self.prefilled = prefilled if prefilled is not None else [0] * self.size
        self.fitness = self.get_fitness()

    def get_fitness(self):
        raise NotImplementedError("Subclasses should implement this method.")

class Population:
    def __init__(self, size, optim, sol_size, valid_set, repetition=True, prefilled=None):
        self.size = size
        self.optim = optim
        self.sol_size = sol_size
        self.valid_set = valid_set
        self.repetition = repetition
        self.prefilled = prefilled
        self.individuals = [Individual(size=sol_size, valid_set=valid_set, repetition=repetition, prefilled=prefilled) for _ in range(size)]

    def evolve(self, gens, xo_prob, mut_prob, select, xo, mutate, elitism):
        for gen in range(gens):
            new_pop = []
            while len(new_pop) < self.size:
                parent1, parent2 = select(self), select(self)
                if random() < xo_prob:
                    offspring1, offspring2 = xo(parent1, parent2)
                else:
                    offspring1, offspring2 = parent1, parent2

                if random() < mut_prob:
                    offspring1 = mutate(offspring1)
                if random() < mut_prob:
                    offspring2 = mutate(offspring2)

                new_pop.append(offspring1)
                if len(new_pop) < self.size:
                    new_pop.append(offspring2)

            if elitism:
                if self.optim == "max":
                    elite = max(self.individuals, key=lambda ind: ind.fitness)
                else:
                    elite = min(self.individuals, key=lambda ind: ind.fitness)
                new_pop[0] = elite

            self.individuals = new_pop

            if self.optim == "max":
                print(f"Best individual of gen #{gen + 1}: {max(self.individuals, key=attrgetter('fitness'))}")
            elif self.optim == "min":
                print(f"Best individual of gen #{gen + 1}: {min(self.individuals, key=attrgetter('fitness'))}")

    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]