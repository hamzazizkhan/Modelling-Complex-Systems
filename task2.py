import random
import itertools
import numpy as np

def G(graphs, n_size):
    isolated_componenets = 0
    n = [i for i in range(n_size)]

    for i in range(graphs):

        p = random.uniform((np.log(n_size) / n_size)+0.0001, 1)
        nodes_with_edges = []
        for i in itertools.combinations(n, 2):
            if random.random() < p:
                #print(i)
                if i[0] not in nodes_with_edges:
                    nodes_with_edges.append(i[0])
                if i[1] not in nodes_with_edges:
                    nodes_with_edges.append(i[1])


        if len(n) - len(nodes_with_edges) == 0:
            isolated_componenets += 1

    return isolated_componenets

graphs = 30
n_size = 1000
isolated_componenets = G(graphs,n_size)
#print(f"out of {graphs} grpahs {isolated_componenets} had isolated componenets for p < ln(n)/n:")
print(f"out of {graphs} grpahs {isolated_componenets} had no isolated componenets for p > ln(n)/n:")

# n is 100: result: out of 20 grpahs 20 had isolated componenets for p < ln(n)/n:
# n is 1000: result: out of 50 grpahs 50 had isolated componenets for p < ln(n)/n:

# n is 100: result: out of 20 grpahs 20 had no isolated componenets for p > ln(n)/n:

# change p and if statement for different cases.




