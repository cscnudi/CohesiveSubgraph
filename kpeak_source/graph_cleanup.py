'''
Created on Feb 6, 2015

@author: priya
'''

import networkx as nx

def removeSelfLoops(G):
    nodes_with_selfloops = G.nodes_with_selfloops()
    
    for node in nodes_with_selfloops:
        G.remove_edge(node, node)
        
    return G
        
def removeSingletons(G):
    degrees=G.degree()
    
    for node in degrees.keys():
        if degrees[node]==0:
            G.remove_node(node)
            
    return G


