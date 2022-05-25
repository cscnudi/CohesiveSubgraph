import networkx as nx

#https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.connectivity.kcomponents.k_components.html?highlight=k_components
def run(G, k):
    ret = nx.k_components(G)
    pp = ret.get(k) # since it considers that when we remove at least k nodes, it is disconnected. Thus, we need to set k+1
    return pp