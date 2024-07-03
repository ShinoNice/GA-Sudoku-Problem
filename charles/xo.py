from random import randint

def sudoku_single_point_xo(parent1, parent2):
    point = randint(0, len(parent1.representation) - 1)
    offspring1 = parent1.representation[:point] + parent2.representation[point:]
    offspring2 = parent2.representation[:point] + parent1.representation[point:]
    size = len(parent1.representation)
    prefilled = parent1.prefilled
    return Individual(representation=offspring1, size=size, prefilled=prefilled), Individual(representation=offspring2, size=size, prefilled=prefilled)

def pmx(p1, p2):
    xo_points = sample(range(len(p1.representation)), 2)
    xo_points.sort()

    def pmx_offspring(x, y):
        o = [None] * len(x.representation)
        o[xo_points[0]:xo_points[1]] = x.representation[xo_points[0]:xo_points[1]]
        z = set(y.representation[xo_points[0]:xo_points[1]]) - set(x.representation[xo_points[0]:xo_points[1]])

        for i in z:
            temp = i
            index = y.representation.index(x.representation[y.representation.index(temp)])
            while o[index] is not None:
                temp = index
                index = y.representation.index(x.representation[temp])
            o[index] = i

        while None in o:
            index = o.index(None)
            o[index] = y.representation[index]
        return o

    o1, o2 = pmx_offspring(p1, p2), pmx_offspring(p2, p1)
    return o1, o2
