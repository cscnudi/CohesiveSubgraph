import networkx as nx


def enumerate_all_cliques_size_k(G, k):
    i = 0
    ret = []
    for clique in nx.enumerate_all_cliques(G):
        if len(clique) >= k:
            ret.append(clique)
    return ret

def run(G, k):
    if k < 2:
        raise nx.NetworkXError(f"k={k}, k must be greater than 1.")
    cliques = nx.find_cliques(G)
    cliques = [set(c) for c in cliques if len(c) >= k]

    return cliques


