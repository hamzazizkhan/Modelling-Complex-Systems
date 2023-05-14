import numpy as np
import itertools
import random
import networkx as nx
import matplotlib.pyplot as plt

# the function below computes the clustring coefficient
# G is the network graph with nodes and edges.
def c(G):
    # cycles_3 stores a list of cycles of length 3 from G
    cycles_3 = [cycle for cycle in nx.cycle_basis(G) if len(cycle) == 3]
    # paths store the simple paths (no repeated nodes) of length 2 from G
    paths = []
    for source in G.nodes():
        for target in G.nodes():
            if source != target:
                # nx.all_simple_paths returns a list of simple paths with length 2 with starting node, source and ending node, target
                for path in nx.all_simple_paths(G, source, target, cutoff=2):
                    paths.append(path)
    if len(cycles_3)!=0 and len(paths)!=0:
        # below clustering coefficient calculated as number of graph cycles of length 3/number of graph paths of length 2
        return len(cycles_3) / len(paths)
    else:
        return 0

# the function below returns the average clustering coefficient for a number of graphs
# it takes grpahs - the number of graphs, n_size - number of nodes/vertices, p - probability
def G(graphs, n_size, p):
    # n stores the nodes
    n = [i for i in range(n_size)]
    # c_sum stores the sum of the clustering coeff for each graph
    c_sum = 0
    for i in range(graphs):
        # edges stores the edges for the current graph in the iteration
        edges = []
        for i in itertools.combinations(n, 2):
            # only if the edges probability is less than p will it be used as an edge
            # otherwise there is no edge
            if random.random() < p:
                edges.append(i)
        # create a network graph.
        f = nx.Graph()
        # below we add the edges and the nodes
        f.add_edges_from(edges)
        f.add_nodes_from(n)
        # calculate the clustering coeff for the graph in the iteration and add it to c_sum
        c_sum += c(f)

    # return the average clustering coeff
    return c_sum/graphs

n_size = 1000
graphs = 30

dt = 0.1
# create a list of probabilities in ps
ps = np.arange(0+dt, 1, dt)
E_c = []
for p in ps:
    # for each probability, get the average clustering coefficient for a number of graphs
    # add this to E_c list
    E_c.append(G(graphs, n_size, p))
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