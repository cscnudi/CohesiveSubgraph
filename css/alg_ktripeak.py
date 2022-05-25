import networkx as nx
import pandas as pd



def ktripeak(G):

    H0 = G.copy()
    k = dict()
    while len(H0.edges) != 0:
        Ckmax, kmax, k_ = maxTrusss(H0)

        H1 = nx.k_truss(H0, kmax)
        Ktrussedge = H1.edges()

        for e in Ckmax:
            if e in Ktrussedge:
                k[e] = kmax
                # if kmax > k_:
                #     k[e] = kmax
                # else:
                #     k[e] = 0 # define


                H0.remove_edge(e[0],e[1])

    return k



def support(G,e): # The number of triangles each containing e in G
    u,v = e
    comm = (set(G.neighbors(u)) & set(G.neighbors(v)))
    return len(comm)



def Dataframe_insertSortedList(df, _elem): # binary search
    start = 0
    end = df.shape[0] - 1

    while start <= end:
        mid = (start + end) // 2

        if df.iloc[mid]['sup'] == _elem:
            return mid+1  #
        elif df.iloc[mid]['sup'] < _elem:
            start = mid + 1
        else:
            end = mid - 1

    return mid+1# return index,

def maxTrusss(H0):
    G0 = H0.copy()
    pi_k_max = set()#defaultdict(set)
    df = pd.DataFrame(columns=['edge','sup'])
    cnt = 0
    for u, v in G0.edges:  # line 2
        e = (u, v) if int(u) <= int(v) else (v, u)
        df.loc[cnt] = [e,support(G0, e)]
        cnt +=1
        # sup[e] = support(G0, e)
    df =df.sort_values(by=['sup'], axis=0)

    k_max = 2

    while len(G0.edges()) != 0:

        u,v = df.iloc[0]['edge']
        k = df.iloc[0]['sup'] + 2

        k_max = max(k_max, k)

        pi_k_max.add((u, v))

        if len(G0[u]) < len(G0[v]):
            _u = u
            _v = v
        else:
            _u = v
            _v = u
        # _u = u if len(G0[u]) < len(G0[v]) else v
        # _v = v if len(G0[u]) < len(G0[v]) else u

        nbrU = G0[_u]
        # idx = df.index[df['edge'] == ('16','17')]# if int(u) <= int(v) else (v, u)

        for w in nbrU :
            if G0.has_edge(_v,w) is True : # if edge exists
                e = (_u, w ) if int(_u) <= int(w) else (w, _u)
                idx = df.index[df['edge'] == e]
                # print('df===========',df)
                # print('before',df.loc[idx[0]]['sup'])
                # df.at[idx, 'sup'] = df.loc[idx[0]]['sup'] -1
                sup1 = df.loc[idx[0]]['sup'] -1
                new_data1 = {
                    'edge': e,
                    'sup': sup1
                }
                df = df.drop(idx)
                # print('after',df.loc[idx[0]]['sup'])
                e = (_v, w) if int(_v) <= int(w) else (w, _v)
                idx = df.index[df['edge'] == e]
                sup2 = df.loc[idx[0]]['sup'] -1

                new_data2 = {
                    'edge': e,
                    'sup': sup2
                }
                df = df.drop(idx)
                idx = Dataframe_insertSortedList(df, sup1)
                temp1 = df.iloc[:idx]
                temp2 = df.iloc[idx:]
                df = temp1.append(new_data1, ignore_index=True).append(temp2, ignore_index=True)
                idx = Dataframe_insertSortedList(df, sup2)
                temp1 = df.iloc[:idx]
                temp2 = df.iloc[idx:]
                df = temp1.append(new_data2, ignore_index=True).append(temp2, ignore_index=True)

                # df = df.sort_values(by=['sup'], axis=0)

                # df.at[]
                # idx = df[df['edge' == (u,v)]]
                # df.at[]
                # sup[(u, w)] = sup[(u, w)] - 1
                # sup[(v, w)] = sup[(v, w)] - 1
                # e_uw = (u, w)
                # e_vw = (u, w)
                # remove e_uw in sup
                # remove e_vw in sup
                # e_uw will be added to sup
                # e_vw will be added to sup
        # print('')
        G0.remove_edge(u,v)
        df = df.iloc[1:]  # 0번째 행 삭제하고 나머지 추출

    return pi_k_max, k_max, k

def run(G, k):
    G0 = G.copy()
    T = ktripeak(G0)
    ret = []
    for (key, value) in T.items() :
        if value >= k:
            ret.append(key)
    P = G.edge_subgraph(ret)
    return nx.connected_components(P)

if __name__ == '__main__':


    G = nx.read_edgelist('../dataset/ktripeak.txt')
    ct = ktripeak(G)
    print(ct)
    # print(len(ct))
    # edgelsit = [(1,2),(2,3),(1,3)]
    # G = nx.Graph()
    # G = nx.karate_club_graph()
    # G.add_edges_from(edgelsit)
    # P = nx.k_truss(G, 2)
    # print(P.nodes())