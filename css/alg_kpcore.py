import networkx as nx
import math

def run(G, k, p):
    t = dict()
    q = []
    G1 = G.copy()
    on = {i: 1 for i in G.nodes()}
    for v in G.nodes():
        t[v] = max(k, math.ceil(p*len(G[v])))
        if len(G[v]) < k:
            q.append(v)
            on[v] = 0

    while q:
        remove_node = q.pop(0)
        G1.remove_node(remove_node)
        for v in G1.nodes():
            if len(G1[v]) < t[v] and on[v] ==1:
                q.append(v)
                on[v] = 0

    return nx.connected_components(G1)


