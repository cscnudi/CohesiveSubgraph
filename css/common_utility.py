
import networkx as nx
from itertools import chain

#############################################################################
#############################################################################

def check_integrity(args):
    assert type(args.k) is int, "k type error"
    assert type(args.h) is int, "h type error"
    assert type(args.s) is int, "s type error"


    if args.algorithm == 'kcore' or args.algorithm == 'kecc' or args.algorithm == 'kvcc' or args.algorithm=='kpeak' \
            or args.algorithm == 'kscore' or args.algorithm == 'kpcore' or args.algorithm == 'MkMFD':
        assert args.k >= 1

    if args.algorithm == 'ktruss':
        assert args.k >= 2

    if args.algorithm == 'alphacore' :
        args.alpha <= 1.0 and args.alpha >= 0.0

    return True


def readEdgeList(fileName):
    #print(fileName)
    g1 = nx.read_edgelist(fileName)
    print("V=", g1.number_of_nodes(), "\tE=", g1.number_of_edges())
    return g1

def print_result(G, C) :
    result = list(C)
    print("----------------------------------------------------------")
    for comp in result:
        comp = [int(x) for x in comp]
        comp = sorted(comp, reverse=False)
        for u in list(comp):
            print(u, ' ', end="")
        print("")
    print("\n----------------------------------------------------------")


    mod, local_mod, v_density, e_density, inv_cond, diam, size = metric(G, result)

    print("result = ", mod, local_mod, v_density, e_density, inv_cond, diam, size)
# sum_modularity, local_modularity, inverse_conductance, average_diameter, average_size = metric(G, C)


def get_average_size(G, C):

    nodeCnt = 0
    E = G.number_of_edges()
    V = G.number_of_nodes()
    cnum = len(C)
    csum = 0
    for c in C:
        csum += len(c)
    return csum/cnum


def get_average_diameter(G, Cgraph):
    sum = 0
    for cg in Cgraph :
        sum = sum + nx.diameter(cg)
    return sum/len(Cgraph)


def degreeSum(G, nodes):
    sum = 0
    for u in nodes:
        sum = sum + G.degree(u)
    return sum


def get_average_modularity(G, Cgraph):
    E = G.number_of_edges()
    sum = 0
    for cg in Cgraph :
        lc = cg.number_of_edges()
        var1 = lc/E
        var2 = (degreeSum(G, cg.nodes)/(2.0*E))**2
        mod = var1 - var2
        sum = sum + mod

    return sum/len(Cgraph)


def get_conductance(G, C):
    sum = 0
    if len(C) == 1 :
        if len(C[0]) == len(G) :
            return 1
    for c in C :
        cd = nx.conductance(G, c)
        sum = sum + cd
    return sum / len(C)

def volume(G, S, weight=None):
    degree = G.out_degree if G.is_directed() else G.degree
    return sum(d for v, d in degree(S, weight=weight))

def get_average_local_modularity(G, C, Cgraph):

    sum = 0
    for idx, S in enumerate(C):
        T = set(G) - set(S)
        cgraph = Cgraph[idx]
        out_degree = cut_size(G, S, T, None)
        in_degree = cgraph.number_of_edges()
        if out_degree == 0 :
            sum += 0
        else :
            sum += in_degree/out_degree

    return sum/len(C)


def cut_size(G, S, T=None, weight=None):

    edges = nx.edge_boundary(G, S, T, data=weight, default=1)
    if G.is_directed():
        edges = chain(edges, nx.edge_boundary(G, T, S, data=weight, default=1))
    return sum(weight for u, v, weight in edges)


def get_avg_graph_density(Cgraph):
    sum = 0
    for cg in Cgraph:
        n = cg.number_of_nodes()
        e = cg.number_of_edges()
        sum += e/n
    return sum/len(Cgraph)

def get_avg_edge_density(Cgraph):
    sum = 0
    for cg in Cgraph:
        n = cg.number_of_nodes()
        e = cg.number_of_edges()
        #print('n', n, 'e', e)
        sum += 2*e/(n*(n-1))
    return sum/len(Cgraph)



# mod, v_density, e_density, inv_cond, size
def fewMetric(G, C):
    if len(C) == 0 :
        return (None, None, None, None, 0)

    Cgraph = []
    for subset in C :
        G0 = G.subgraph\
            (subset)
        Cgraph.append(G0)


    sum_modularity = get_average_modularity(G, Cgraph)
   # average_local_modularity = get_average_local_modularity(G, C, Cgraph)
    average_graph_density = get_avg_graph_density(Cgraph)
    average_edge_density = get_avg_edge_density(Cgraph)
    inverse_conductance = 1.0 - get_conductance(G, C)
   # average_diameter = get_average_diameter(G, Cgraph)
    average_size = get_average_size(G, C)

    return (sum_modularity,
            average_graph_density,
            average_edge_density,
            inverse_conductance,
            average_size)


def metric(G, C):
    if len(C) == 0 :
        return (None, None, None, None, None, None, 0)

    Cgraph = []
    for subset in C :
        G0 = G.subgraph\
            (subset)
        Cgraph.append(G0)


    sum_modularity = get_average_modularity(G, Cgraph)
    average_local_modularity = get_average_local_modularity(G, C, Cgraph)
    average_graph_density = get_avg_graph_density(Cgraph)
    average_edge_density = get_avg_edge_density(Cgraph)
    inverse_conductance = 1.0 - get_conductance(G, C)
    average_diameter = get_average_diameter(G, Cgraph)
    average_size = get_average_size(G, C)

    return (sum_modularity,
            average_local_modularity,
            average_graph_density,
            average_edge_density,
            inverse_conductance,
            average_diameter,
            average_size)

# mod, local_mod, v_density, e_density, inv_cond, diam, size
