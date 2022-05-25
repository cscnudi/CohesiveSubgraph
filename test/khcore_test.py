import argparse
import networkx as nx
#import css.alg_kcore
import css.alg_khcore
import css.common_utility

#############################################################################
parser = argparse.ArgumentParser(description='value k')
parser.add_argument('--k', type=int, default=8,
                    help='user parameter k for k-core and k-truss')

parser.add_argument('--h', type=int, default=2,
                    help='distance threshold h for kh-core`')

parser.add_argument('--network', default="../dataset/general_example.dat",
                    help='a folder name containing network.dat')

parser.add_argument('--algorithm', default="khcore",
                    help='specify algorithm name')

args = parser.parse_args()
print(args.k)
print(args.h)
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

C = css.alg_khcore.run(G, args.k, args.h)

css.common_utility.print_result(G, C)

