import networkx as nx

def ifConditionSatisifed(H0, s, _k, _alpha) :
    for (u,v) in H0.edges() :
        e0 = (u, v) if int(u) < int(v) else (v, u)
        if min(len(H0[u]), len(H0[v]) ) <= _k/_alpha and s[e0]<=_k-2:
            return (u,v)
    return None


def kcoreturss(G,alpha):
    k = 2 # line 1
    H = G.copy() # line 1
    sup_H_e = dict()

    for u,v in H.edges(): # line 3
        e = (u, v) if int(u) < int(v) else (v, u)
        sup_H_e[e] = len((set(H.neighbors(u)) & set(H.neighbors(v)))) # line 6

    ct = dict()
    while True:
        while True :
            x = ifConditionSatisifed(H, sup_H_e, k, alpha)
            if x != None:
                (u,v) = x
                H.remove_edge(u, v)
                ct[(u, v)] = k
                W = (set(H.neighbors(u)) & set(H.neighbors(v)))
                for w in W:
                    sup_H_e[(u, w) if int(u) < int(w) else (w, u)] = sup_H_e[(u, w) if int(u) < int(w) else (w, u)] - 1
                    sup_H_e[(v, w) if int(v) < int(w) else (w, v)] = sup_H_e[(v, w) if int(v) < int(w) else (w, v)] - 1
            else :
                break
        if len(H.edges()) != 0:
            k = k + 1
        else:
            break

    return ct



def run(G, k, alpha):
    G0 = G.copy()
    T = kcoreturss(G0, alpha)
    ret = []
    for (key, value) in T.items() :
        if value >= k:
            ret.append(key)
    P = G.edge_subgraph(ret)
    return nx.connected_components(P)




if __name__ == '__main__':
    G = nx.read_edgelist('kcoretruss.txt')
    # G0 = run(G, k=2, alpha=1)
    ct = kcoreturss(G, alpha=1)
    print(ct)
