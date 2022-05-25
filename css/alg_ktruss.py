import networkx as nx

def run(G, k):
    P = nx.k_truss(G, k)
    return nx.connected_components(P)
