import networkx as nx


def ifConditionSatisifed(H0, _k, _alpha, _W) :
    check = []
    if _W is None:
        for (u,v) in H0.edges():
            if min(H0.degree(u),H0.degree(v)) <= _k/ _alpha and H0[u][v]['sup']<=_k-2:
                check.append((u,v))
                H0[u][v]['remove'] = 1


    else:
        for w in _W:
            for v in H0[w]:
                if min(H0.degree(w), H0.degree(v)) <= _k / _alpha and H0[w][v]['sup'] <= _k - 2:
                    if H0[w][v]['remove'] == 0:
                        check.append((v,w))
                        H0[w][v]['remove'] = 1
    if len(check) == 0:
        return None
    else:
        return check



def kcoretruss(G,alpha,k0):
    # k = 2 # line 1
    H = G.copy() # line 1
    k0 = k0-1
    for u,v in H.edges(): # line 3
        H[u][v]['sup'] = len((set(H[u]) & set(H[v])))
        H[u][v]['remove'] = 0

    intersection = None
    while True:
        remove_edges = ifConditionSatisifed(H,k0,alpha, intersection)
        if remove_edges is not None:
            intersection = set()
            for (u,v) in remove_edges:
                H.remove_edge(u,v)
                W = (set(H[u]) & set(H[v]))
                intersection.update(set(H[u]) | set(H[v]))
                for w in W:
                    H[u][w]['sup'] = H[u][w]['sup'] - 1
                    H[v][w]['sup'] = H[v][w]['sup'] - 1
        else:
            break

    remove = [node for node, degree in H.degree() if degree == 0]
    H.remove_nodes_from(remove)

    return H


def run(G, k, alpha):
    G0 = G.copy()
    T = kcoretruss(G0, alpha, k)
    return nx.connected_components(T)
