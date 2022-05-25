import networkx as nx

#https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.connectivity.edge_kcomponents.k_edge_components.html?highlight=k_edge_components

# The implementation of k-ecc
# I borrowed the implementation in networkX.
# input : a graph G and an integer k
# output : a set of connected components


def run(G, k):
    G0 = G.copy()
    ret1 = nx.k_edge_components(G0, k)
    ret = []
    for x in ret1 :
        if len(x) != 1 :
            ret.append(x)
    return ret