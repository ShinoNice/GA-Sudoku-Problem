from random import sample
from charles.charles import Individual

def sudoku_swap_mutation(individual):
    mut_indexes = sample(range(len(individual.representation)), 2)
    individual.representation[mut_indexes[0]], individual.representation[mut_indexes[1]] = individual.representation[mut_indexes[1]], individual.representation[mut_indexes[0]]
    size = len(individual.representation)
    prefilled = individual.prefilled
    return Individual(representation=individual.representation, size=size, prefilled=prefilled)

def sudoku_inversion_mutation(individual):
    """Inversion mutation for a GA individual. Reverts a portion of the representation.

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    non_prefilled_indices = [i for i, pre in enumerate(individual.prefilled) if not pre]
    if len(non_prefilled_indices) < 2:
        return individual

    mut_indexes = sample(non_prefilled_indices, 2)
    mut_indexes.sort()
    segment = [individual[i] for i in mut_indexes]
    segment.reverse()
    for i, index in enumerate(mut_indexes):
        individual[index] = segment[i]

    individual.fitness = individual.get_fitness()  # Recalculate fitness after mutation
    return individual
