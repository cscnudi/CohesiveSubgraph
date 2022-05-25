import networkx as nx
from collections import defaultdict
import os

def run(G, k, h):
    G0 = G.copy()
    T = khcore(G0, h)
    ret = []
    for (key, value) in T.items() :
        if value >= k:
            ret.append(key)

    P = G.subgraph(ret)
    return nx.connected_components(P)


def khcore(G,h=2):
    '''

    :param G: graph
    :param h: distance threshold
    :return: core
    '''

    """
    Bonchi, Francesco, Arijit Khan, and Lorenzo Severini. "Distance-generalized core decomposition."
    Proceedings of the 2019 International Conference on Management of Data. 2019.
    Algorithm 1
    """

    B = defaultdict(set)
    core = dict()
    invert_B = dict()

    for v in G.nodes():
        deg_hv = len(set(nx.single_source_shortest_path_length(G,v,h)))-1 #line 2
        B[deg_hv].add(v) # distance 0 rmove,
        invert_B[v] = deg_hv #line 3

    B = {i: B[i] for i in sorted(B)} # sorted B

    sizeofgraph = nx.number_of_nodes(G)

    def compute(B,core,invert_B,key):
        flag = False
        while B[key]: #line 5
            for v in B[key].copy():
                B[key].remove(v)
                invert_B.pop(v) #line 6
                core[v] = key #line 7
                NGvh= set(nx.single_source_shortest_path_length(G, v, h))
                NGvh.remove(v)
                G.remove_node(v)
                for u in NGvh: #line 8
                    NGuh = set(nx.single_source_shortest_path_length(G, u, h)) #line 9
                    NGuh.remove(u)
                    moved_u = invert_B[u]
                    B[moved_u].remove(u)
                    moving_u = max(len(NGuh),key) #line 10
                    invert_B[u] = moving_u
                    try:
                        B[moving_u].add(u)
                    except KeyError:
                        B[moving_u] = set()
                        B[moving_u].add(u)# add
                        flag = True
                if flag == True:
                    return B,core,invert_B,flag
        return B, core, invert_B,flag



    while len(core) != sizeofgraph:
        for key, value in B.copy().items():
            B, core, invert_B, flag = compute(B,core,invert_B,key)
            if flag == True:
                break
        B = {i: B[i] for i in sorted(B)}

    return core
