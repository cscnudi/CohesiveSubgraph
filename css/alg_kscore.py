import networkx as nx
from collections import deque

# G_input is an input graph
# k is an engagement constraint
# s is a tie-strength

# output : a set of connected components

# pls check the algorithm 1 of Discovering Strong Communities # with User Engagement and Tie Strength, DASFAA 2020


def run(G,k,s):
    G0 = G.copy()
    T = kscore(G0, k, s)
    print(T)
    return nx.connected_components(T)


def support(G,e): # The number of triangles each containing e in G
    u,v = e
    comm = (set(G[u]) & set(G[v]))
    return len(comm)


def engagement(G,u,sup, s): #The number of edges where each edge e has sup(e, G) ≥ s and e is incident to u in G
    count = 0
    for v in G[u]:
        e = (u, v) if int(u) < int(v) else (v, u)

        if sup[e] >=s:
            count = count + 1
        # if support(G,e) >= s: 
        #     count+=1

    return count


def lessThanKdeg(G,k,deg, q):
    for u in G.nodes():
        if deg[u] < k and (u not in q):
            q.append(u)

    return q


def kscore(G_input, k, s) :

    # initialization
    sup = {}
    deg = {}

    k_prime = max(k, s+1) #line 1
    G = nx.k_core(G_input, k_prime) #line 1

    for u,v in G.edges :#line 2
        # e = (u,v) #line 2
        e = (u, v) if int(u) < int(v) else (v, u)

        sup[e] = support(G, e) #line 2

    for u in G.nodes: #line 2
        deg[u] = engagement(G,u,sup,s) #line 2


    q = deque()
    q = lessThanKdeg(G, k, deg,q)


    while q:
        u = q.popleft()
        for v in set(G[u]).copy():
            if deg[v] >= k:
                G.remove_edge(u,v)
                if sup[(u, v) if int(u) < int(v) else (v, u)] >=s:
                    deg[v] = deg[v] - 1

                W = (set(G[u]) & set(G[v]))
                for w in [w for w in W if deg[w] >= k]:

                    if sup[(v, w) if int(v) < int(w) else (w, v)] >= s:
                        sup[(v, w) if int(v) < int(w) else (w, v)] -= 1
                        if sup[(v, w) if int(v) < int(w) else (w, v)] == s-1:
                            deg[w] = deg[w] - 1
                            deg[v] = deg[v] -1

        G.remove_node(u)
        q = lessThanKdeg(G, k, deg, q)

    return G


