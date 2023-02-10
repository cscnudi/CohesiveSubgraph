import json
import argparse
import networkx as nx
import os

def setup_file_list():
    files = os.listdir()
    network_file_list = []
    for file in files:
        if file[-4:] == 'json':
            network_file_list.append(file[:-5])

    return network_file_list


def create_folder(directory):
    """
    create folder
    :param directory: directory name
    :return: directory folder
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error Creating directory. ' + directory)


def jaccard(u, v):
    intersection = u & v
    union = u | v
    return len(intersection) / len(union)


def similarity(h, e1, e2):
    e1_u, e1_v = e1.split('_')
    e2_u, e2_v = e2.split('_')
    value_u = jaccard(set(h[e1_u]), set(h[e2_u]))
    value_v = jaccard(set(h[e1_v]), set(h[e2_v]))
    return (value_u + value_v) / 2.0


def json_to_dat(name):
    _file = name + '.json'
    data = [json.loads(line) for line in open(_file, 'r')]

    f = open('{}.dat'.format(name), 'w')
    for idx in range(len(data)):
        if data[idx]['helpful'][1] != 0:
            if data[idx]['helpful'][0] / data[idx]['helpful'][1] >= 0.75:
                edge_type = 1
            elif data[idx]['helpful'][0] / data[idx]['helpful'][1] <= 0.25:
                edge_type = 2
            else:
                edge_type = 0
            f.write('{}\t{}\t{}\t{}\t{}\n'.format(data[idx]['reviewerID'], data[idx]['asin'], data[idx]['helpful'][0],
                                                  data[idx]['helpful'][1], edge_type))
    f.close()
    H, positive, negative = preprocessing_file_read(name)

    print(name)
    print("node size : " ,nx.number_of_nodes(H),'edge size : ',nx.number_of_edges(H))
    print("# of positive = ",positive)
    print("# of negative = ",negative)
    print()

def preprocessing_file_read(name):
    G = nx.Graph()
    number_of_positive_edges, number_of_negative_edges = 0,0
    with open("./{}.dat".format(name), 'r') as _file:
        lines = _file.readlines()

        for line in lines:
            tokens = line.strip().split('\t')
            G.add_node(tokens[0], bipartite=0)
            G.add_node(tokens[1], bipartite=1)
            G.add_edge(tokens[0], tokens[1])
            G[tokens[0]][tokens[1]]['positive'] = int(tokens[2])
            G[tokens[0]][tokens[1]]['total'] = int(tokens[2])
            G[tokens[0]][tokens[1]]['edgetype'] = int(tokens[4])
            if int(tokens[4]) == 1:
                number_of_positive_edges += 1
            elif int(tokens[4]) == 2:
                number_of_negative_edges += 1

    _file.close()
    return G, number_of_positive_edges, number_of_negative_edges


def remove_under_t(g, t_):
    h = g.copy()

    for u, v in g.edges:
        if g[u][v]['total'] < t_:
            h.remove_edge(u, v)

    solitary = [node for node, degree in h.degree() if degree == 0]
    h.remove_nodes_from(solitary)
    return h


def create_mapping(file_):
    G = nx.read_edgelist('./{}_{}_{}/network.dat'.format(file_, args.t, args.threshold))
    mapping = {old_label:new_label for new_label, old_label in enumerate(G.nodes())}
    G0,p,n = preprocessing_file_read(file_)
    f = open('./{}_{}_{}/index.txt'.format(file_, args.t, args.threshold),'w')
    for k,v in mapping.items():
        e1, e2 = k.split('_')
        f.write('{}\t{}\t{}\n'.format(v,k, G0[e1][e2]['edgetype']))
    f.close()
    H = nx.relabel_nodes(G, mapping)
    f = open('./{}_{}_{}/network_mapping.dat'.format(file_, args.t, args.threshold),'w')
    for u, v in H.edges:
        f.write('{}\t{}\n'.format(u,v))
    f.close()


def make_network(name):

    G,p,n = preprocessing_file_read(name)
    H = remove_under_t(G, args.t)

    H0 = nx.Graph()

    for u, v in H.edges():

        e1 = (u, v) if u < v else (v, u)
        Nu = set(H[e1[0]])
        Nv = set(H[e1[1]])

        e1 = "{}_{}".format(e1[0],e1[1])
        H0.add_node(e1)

        NNu = set()
        for w in Nu:
            NNu = NNu | set(H[w])

        for x in NNu:
            for w in H[x]:
                e2 = (x, w) if x < w else (w, x)
                e2 = "{}_{}".format(e2[0], e2[1])
                if e1 != e2:
                    H0.add_node(e2)
                    value = similarity(H, e1, e2)
                    if value > args.threshold:
                        H0.add_edge(e1, e2)

        NNv = set()
        for w in Nv:
            NNv = NNv | set(H[w])

        for x in NNv:
            for w in H[x]:
                e2 = (x, w) if x < w else (w, x)
                e2 = "{}_{}".format(e2[0], e2[1])
                if e1 != e2:
                    if H0.has_edge(e1, e2) == False:
                        H0.add_node(e2)
                        value = similarity(H, e1, e2)
                        if value > args.threshold:
                            H0.add_edge(e1, e2)
                            # if H[u][v]['edgetype'] == 2:
                            #     count_negative_edges = count_negative_edges + 1

    H0.remove_nodes_from(list(nx.isolates(H0)))
    count_negative_edges = 0
    for node in H0.nodes():
        u, v = node.split('_')
        if G[u][v]['edgetype'] == 2:
            count_negative_edges = count_negative_edges + 1
    path = "{}_{}_{}".format(name, args.t, args.threshold)
    create_folder(path)
    nx.write_edgelist(H0, "{}/{}.dat".format(path, "network"), data=False)
    print("t = {}, lambda = {}, v1 = {}, v2 = {}, v3 = {}".format(args.t, args.threshold, count_negative_edges,len(H0.nodes) ,count_negative_edges/len(H0.nodes)))


def make_network_mapping_file(_file):
    dir_list = os.listdir('./{}_{}_{}'.format(_file, args.t, args.threshold))
    if 'network_mapping.dat' not in dir_list:
        create_mapping(_file)


parser = argparse.ArgumentParser(description='value k')
parser.add_argument('--t', type=int, default=3,
                    help='user parameter t')

parser.add_argument('--threshold', type=float, default=0.3,
                    help='threshold lambda')
args = parser.parse_args()


if __name__ == '__main__':
    os.chdir('./dataset/amazon/')
    file_list = setup_file_list()
    for file in file_list:
        json_to_dat(file)
        make_network(file)
    for file in file_list:
        make_network_mapping_file(file)
