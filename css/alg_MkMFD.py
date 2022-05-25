import numpy as np
import networkx as nx

# http://www.vldb.org/pvldb/vol6/p85-feng.pdf

def run(G, k):
    G0 = G.copy()
    T = run_MkMFD(G0, k)
    print(T)
    return nx.connected_components(T)

def run_MkMFD(G, k):
    for v in list(G.nodes()):  # lines 1-3
        if G.degree(v) <= k:  # lines 1-3
            G.remove_node(v)  # lines 1-3

    Q = []  # lines 4
    Tr = {}  # lines 5

    for (u, v) in G.edges():
        comm = (set(G.neighbors(u)) & set(G.neighbors(v)))
        e = (u, v) if int(u) < int(v) else (v, u)
        Tr[(e[0], e[1])] = len(comm)
        if Tr[(e[0], e[1])] < k:
            Q.append((e[0], e[1]))

    while len(Q) != 0:
        e = Q.pop()
        (u, v) = e

        comm = (set(G.neighbors(u)) & set(G.neighbors(v)))
        G.remove_edge(u, v)  # lines 13

        for w in comm:
            ep = (u, w) if int(u) < int(w) else (w, u)
            Tr[ep] = Tr[ep] - 1
            if Tr[ep] < k and not ep in Q:
                Q.append(ep)

        for w in comm:
            ep = (v, w) if int(v) < int(w) else (w, v)
            Tr[ep] = Tr[ep] - 1

            if Tr[ep] < k and not ep in Q:
                Q.append(ep)

    for v in list(G.nodes):
        if G.degree(v) == 0:
            G.remove_node(v)

    return G
