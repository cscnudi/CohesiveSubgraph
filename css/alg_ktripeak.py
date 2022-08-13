import networkx as nx


def ktripeak(G):

    H0 = G.copy()
    k = dict()
    while len(H0.edges) != 0:

        Ckmax, kmax= maxTruss(H0)

        H1 = nx.k_truss(H0, kmax)
        Ktrussedge = H1.edges()

        for e in Ckmax:
            if e in Ktrussedge:
                k[e] = kmax

                H0.remove_edge(e[0],e[1])

    return k


def computeSupport(G):
    supportValue = {}
    for (u, v) in G.edges :
        cnt = len(set(G[u]) & set(G[v]))
        supportValue[(u, v)] = cnt

    nx.set_edge_attributes(G, supportValue, "sup")


def getMinSup(E):
    if len(E) == 0 :
        return None
    else :
        print(E[0][2]['sup'])
        return (E[0][2]['sup'])


def getMinSupEdge(E):
    return (E[0][0], E[0][1])


def minDegree(G, u, v):
    if G.degree(u) < G.degree(v) :
        return u
    else :
        return v

def maxTruss(_H0):

    G = _H0.copy()
    T = {}
    computeSupport(G)
    E = sorted(G.edges(data=True), key=lambda t: t[2].get('sup', 1))
    k_max = 2
    while len(G.edges) != 0 :
        (u,v) = getMinSupEdge(E)

        k = G[u][v]['sup'] + 2

        k_max = max(k_max, k)
        T[(u,v)] = k_max

        u, v = (u, v) if G.degree(u) < G.degree(v) else (v, u)

        E.pop(0)
        G.remove_edge(u, v)

        for w in G[u] :
            if w in G.neighbors(v) :
                G[u][w]['sup'] = G[u][w]['sup'] - 1
                G[v][w]['sup'] = G[v][w]['sup'] - 1
                E = sorted(G.edges(data=True), key=lambda t: t[2].get('sup', 1))

    return T, k_max



def run(G, k):
    G0 = G.copy()
    T = ktripeak(G0)
    ret = []
    for (key, value) in T.items() :
        if value >= k:
            ret.append(key)
    P = G.edge_subgraph(ret)
    return nx.connected_components(P)
