import networkx as nx

# The implementation of k-core
# I borrowed the implementation in networkX.
# input : a graph G and an integer k
# output : a set of connected components

def run(G, k):
    P =  nx.k_core(G, k)
    return nx.connected_components(P)
