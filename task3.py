import numpy as np
import itertools
import random
import networkx as nx
import matplotlib.pyplot as plt

def c(G):
    cycles_3 = [cycle for cycle in nx.cycle_basis(G) if len(cycle) == 3]
    paths = []
    for source in G.nodes():
        for target in G.nodes():
            if source != target:
                for path in nx.all_simple_paths(G, source, target, cutoff=2):
                    paths.append(path)
    if len(cycles_3)!=0 and len(paths)!=0:
        return len(cycles_3) / len(paths)
    else:
        return 0




def G(graphs, n_size, p):
    n = [i for i in range(n_size)]
    c_sum = 0
    for i in range(graphs):

        edges = []
        for i in itertools.combinations(n, 2):
            if random.random() < p:
                edges.append(i)

        f = nx.Graph()
        f.add_edges_from(edges)
        f.add_nodes_from(n)
        c_sum += c(f)


    return c_sum/graphs

n_size = 1000
graphs = 30
ps = np.arange(0, 1.1, 0.1)
E_c = []
for p in ps:
    E_c.append(G(graphs, n_size, p))
    # generate many G's for p, return E(C) for each
    pass

# plot p on x-axes and c on y-axes
# Create the plot
plt.plot(ps, E_c)

# Add labels and title
plt.xlabel('probability')
plt.ylabel('E(c)')
plt.title('expected global clustering coefficient')

# Display the plot
plt.show()