import networkx as nx
import math

def run(G, k, p):
    t = dict()
    q = []
    G1 = G.copy()
    on = {i: True for i in G.nodes()}

    # initialize Q and on[]
    for v in G.nodes():
        t[v] = max(k, math.ceil(p*len(G[v])))
        if len(G[v]) < k:
            q.append(v)
            on[v] = False

    while q:
        remove_node = q.pop(0)
        neibs = G1[remove_node]
        G1.remove_node(remove_node)
        for v in neibs:
            if len(G1[v]) < t[v] and on[v] is True:
                q.append(v)
                on[v] = False

    return nx.connected_components(G1)

