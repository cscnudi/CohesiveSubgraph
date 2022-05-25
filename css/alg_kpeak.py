import networkx as nx
import alg_kpeak_sub as kp

def run(G, k):
    peaknumbers, corenumbers = kp.get_kpeak_decomposition(G)
    nodes = list()
    for x in peaknumbers.keys() :
        v = peaknumbers.get(x)
        if v >= k :
            nodes.append(x)

    #print(nodes)
    G1 = G.subgraph(nodes)
    return nx.connected_components(G1)
