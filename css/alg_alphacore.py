import networkx as nx
import os
import numpy as np
import pandas as pd
from scipy.spatial.distance import mahalanobis
import math


def alphacore(G,stepSize, startEpsilon,exponentialDecay=True):
    """

    :param input_graph: directed, weighted, multigraph G=(V,E,w)
    :param featureComputeFun: Set of node property function
    :param stepSize:
    :param startEpsilon:
    :param exponentialDecay:
    :return: node id, core value, and batchID (C,B)
    """
    #weighted = dict(nx.edge_betweenness_centrality(G, normalized=True))
    weighted = dict()
    for (u,v) in G.edges :
        weighted[(u,v)] = 1
    node_features = computeNodeFeaturFun(G, weighted=weighted)
    df = node_features[['degree', 'strength']]
    df = df.astype('float')
    cov = df.cov()
    cov_mat_inv = np.linalg.pinv(cov)

    node_features['depth'] = mhdOrigin(node_features[['degree', 'strength']],cov_mat_inv)
    epsilon = startEpsilon

    result = pd.DataFrame(columns=['node', 'alpha', 'batch'])
    cnt = 0
    for u in G.nodes():
        result.loc[cnt] = [u,0,0]
        cnt += 1

    alpha = 1 - epsilon
    alpha_prev = alpha
    batch_ID = 0
    while G.nodes():
        while True:

            nodes = node_features.loc[node_features['depth']>=epsilon]
            nodes = nodes['node']
            for node in nodes:
                idx = result.index[result['node'] == node]
                result.at[idx[0],'alpha']=alpha_prev
                result.at[idx[0], 'batch'] = batch_ID

            if len(nodes):
                G.remove_nodes_from(nodes.values)
                # nodeset = nodeset - set(nodes.values)
            batch_ID +=1

            if nx.number_of_nodes(G) == 0:
                return result

            node_features = computeNodeFeaturFun(G, weighted=weighted)

            node_features['depth'] = mhdOrigin(node_features[['degree', 'strength']], cov_mat_inv)
            if len(nodes) == 0:
                break


        alpha_prev = alpha

        if exponentialDecay:
            localStepSize = math.ceil(nx.number_of_nodes(G)*stepSize)
            node_features_sort = node_features.sort_values(by=['depth'], axis=0, ascending=False)
            node_features_sort = node_features_sort.head(localStepSize)
            depth = node_features_sort['depth']
            epsilon = min(depth)
        else:
            epsilon -= stepSize

        alpha = 1 - epsilon

    return result

def computeNodeFeaturFun(G,weighted):
    '''
    :param G: graph
    :param weighted: dictionary type,,
    :return:strength : sum of weight
    '''
    df = pd.DataFrame(columns=['node','degree','strength'])
    cnt = 0

    # strength = defaultdict()
    for u in G.nodes():
        weight = 0
        for v in G[u]:
            try:
                weight += weighted[(u,v)]
            except KeyError:
                weight += weighted[(v,u)]
        df.loc[cnt] = [u,len(G[u]), weight]
        cnt +=1

        # strength[u] = weight
    return df

def mahalanobisR(X,meanCol,IC):


    m = []
    for i in range(X.shape[0]):
        m.append(mahalanobis(X.iloc[i, :], meanCol, IC) ** 2)

    m = pd.DataFrame(m)
    return m

def mhdOrigin(data,sigma_inv):
    meanCol = [0]*data.shape[1]
    meanCol = pd.DataFrame(meanCol)

    # mhd = []
    val = 1 + mahalanobisR(data, meanCol, sigma_inv)
    val = np.divide(1,val, out=np.zeros_like(val), where = val!=0)

    return val



def run(G, alpha, stepSize=0.1, startEpsilon=1) :
    G1 = G.copy()
    T = alphacore(G1, stepSize, startEpsilon)
    #print(T)
    ret = []
    for index, each in T.iterrows() :
        if each['alpha'] >= alpha :
            ret.append(each['node'])

    G0 = G.subgraph(ret)
    return nx.connected_components(G0)


if __name__ == '__main__':

    os.chdir('dataset')
    dataname = 'karate'  # args.dataset
    G = nx.karate_club_graph()
    result= alphacore(G)
    print(result)

    # a = [1,1,5,1]
    # a = np.array(a,dtype=float)
    # a = a-1
    # print(a)
    # # a = 1/a
    # a = np.divide(1,a, out=np.zeros_like(a), where = a!=0)
    # print(a)
    # a[a==np.inf] = 0
    # print(a)
    # df = computeNodeFeaturFun(G, weighted=None)
    # print(df[['degree', 'strength']])
    # print(np.cov(df[['degree', 'strength']]))

