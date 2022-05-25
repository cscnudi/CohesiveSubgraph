import networkx as nx


def distance_graph(Graph, dist) :

    retG = Graph.copy()

    for v in Graph:
        p = nx.single_source_shortest_path_length(Graph, v, cutoff=dist)
        neighbors = p.keys()
        nbs = list(neighbors)
        for x in nbs :
            retG.add_edge(v, x)

    return retG

def run(G, k) :
    G0 = distance_graph(G, k)
    print(len(G0), len(G0.edges))
    #ret = nx.algorithms.approximation.max_clique(G0)
    ret = nx.find_cliques(G0)
    return list(ret)


