import argparse
import networkx as nx
import css.alg_alphacore
import css.common_utility

#############################################################################
parser = argparse.ArgumentParser(description='value k')

parser.add_argument('--alpha', type=float, default=0.1,
                    help='alphacore threshold')

parser.add_argument('--network', default="../dataset/general_example.dat",
                    help='a folder name containing network.dat')

parser.add_argument('--algorithm', default="alphacore",
                    help='specify algorithm name')

args = parser.parse_args()
print(args.alpha)
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

C = css.alg_alphacore.run(G, args.alpha)

css.common_utility.print_result(G, C)