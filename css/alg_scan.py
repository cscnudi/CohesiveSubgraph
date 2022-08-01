from cdlib import algorithms


def run(G, k, epsilon):
    ret = algorithms.scan(G, epsilon, k).communities
    return ret
