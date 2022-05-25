import argparse
import css.alg_kscore
import networkx as nx
import css.common_utility

#############################################################################
parser = argparse.ArgumentParser(description='value k')
parser.add_argument('--k', type=int, default=3,
                    help='user parameter k for k-core and k-truss')

parser.add_argument('--s', type=int, default=2,
                    help=' s for ks-core`')

parser.add_argument('--network', default="../dataset/kscore_fig2.txt",
                    help='a folder name containing network.dat')

parser.add_argument('--algorithm', default="kscore",
                    help='specify algorithm name')

args = parser.parse_args()
print(args.k)
print(args.s)
print(args.network)
print(args.algorithm)

#############################################################################
#############################################################################
#############################################################################

#############################################################################
# Global Parameter
G = None
C = None
#############################################################################
# read network
G = css.common_utility.readEdgeList(args.network)
#############################################################################

C = css.alg_kscore.run(G, args.k, args.s)

css.common_utility.print_result(G, C)