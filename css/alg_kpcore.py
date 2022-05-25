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


if __name__ == '__main__':

    # dataname = 'karate'  # args.dataset
    # dataname = 'kpcore_icde2020.txt'
    # G = nx.karate_club_graph()
    G = nx.read_edgelist('./dataset/kpcore_fig2_icde2020.txt')
    # print(G.nodes())
    # print(G.edges(1))
    G1= run(G,k=3,p=3/8)
    print(G1.nodes())
    print(G1.edges())
    print(len(G1.edges()))
    print(len(G1.nodes()))

    n = ['11','12','13','14','4','17','16','15','18','6']
    a = G.subgraph(n)
    print(a.edges())
    print(len(a.edges()))
    if a.edges() == G1.edges():
        print('true')



