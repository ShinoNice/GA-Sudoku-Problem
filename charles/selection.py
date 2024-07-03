from operator import attrgetter
from random import uniform, choice

def fps(population):
    if population.optim == "max":
        total_fitness = sum([i.fitness for i in population.individuals])
        r = uniform(0, total_fitness)
        position = 0
        for individual in population.individuals:
            position += individual.fitness
            if position > r:
                return individual
    elif population.optim == "min":
        raise NotImplementedError
    else:
        raise Exception("Optimization not specified (max/min)")

def tournament_sel(population, tour_size=3):
    tournament = [choice(population.individuals) for _ in range(tour_size)]
    if population.optim == "max":
        return max(tournament, key=attrgetter('fitness'))
    elif population.optim == "min":
        return min(tournament, key=attrgetter('fitness'))
