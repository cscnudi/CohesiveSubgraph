import networkx as nx


def ktripeak(G,k_):

    H0 = G.copy()
    H0 = nx.k_truss(H0,k_)
    k = dict()
    while len(H0.edges) != 0:
        Ckmax, kmax= maxTruss(H0)
        H1 = nx.k_truss(H0, kmax)
        Ktrussedge = H1.edges()
        if kmax < k_ -1:
            break
        for e in Ckmax:
            if e in Ktrussedge:
                k[e] = kmax
                H0.remove_edge(e[0],e[1])

    return k


def computeSupport(G):
    maxSupport = 0
    supportValue = {}
    for (u, v) in G.edges :
        cnt = len(set(G[u]) & set(G[v]))
        supportValue[(u, v)] = cnt
        if maxSupport < cnt:
            maxSupport = cnt

    nx.set_edge_attributes(G, supportValue, "sup")
    return maxSupport


def getMinSupEdge(E):
    for support, edgeList in E.items():
        if len(edgeList) != 0:
            edge = E[support].pop()
            sup = support
            break
    e0, e1 = edge
    return e0, e1, sup


def edgeSort(u,v):
    e = (u, v) if int(u) < int(v) else (v, u)
    return e


def supportUpdate(G_,u_,v_,w_,supDict):
    uw_sup = G_[u_][w_]['sup']
    uw = edgeSort(u_, w_)
    supDict[uw_sup + 1].remove(uw)

    supDict[uw_sup].append(uw)
    vw_sup = G_[v_][w_]['sup']
    vw = edgeSort(v_, w_)
    supDict[vw_sup + 1].remove(vw)
    supDict[vw_sup].append(vw)


def maxTruss(_H0):

    G = _H0.copy()
    T = {}
    maxsup = computeSupport(G)
    E = {sup: list() for sup in range(maxsup+1)}

    for u, v in G.edges():
        e0 = edgeSort(u,v)
        E[G.edges[u,v]['sup']].append(e0)


    k_max = 2

    while len(G.edges) != 0 :
        u, v, k = getMinSupEdge(E)
        k = k + 2
        k_max = max(k_max, k)
        T[(u,v)] = k_max

        u, v = (u, v) if G.degree(u) < G.degree(v) else (v, u)

        G.remove_edge(u, v)

        for w in G[u] :
            if w in G.neighbors(v) :

                G[u][w]['sup'] = G[u][w]['sup'] - 1
                G[v][w]['sup'] = G[v][w]['sup'] - 1
                supportUpdate(G, u, v, w, E)
                
    return T, k_max



def run(G, k):
    G0 = G.copy()
    T = ktripeak(G0,k)
    ret = []
    for (key, value) in T.items() :
        if value >= k:
            ret.append(key)
    P = G.edge_subgraph(ret)
    return nx.connected_components(P)
