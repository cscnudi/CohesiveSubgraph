import argparse
import css.common_utility
import css.alg_ktripeak
#############################################################################
parser = argparse.ArgumentParser(description='value k')
parser.add_argument('--k', type=int, default=6,
                    help='user parameter k for k-core and k-truss')

parser.add_argument('--h', type=int, default=2,
                    help='distance threshold h for kh-core`')

parser.add_argument('--network', default="../dataset/ktripeak.txt",
                    help='a folder name containing network.dat')

parser.add_argument('--algorithm', default="ktripeakcore",
                    help='specify algorithm name')

args = parser.parse_args()
print(args.k)
# print(args.h)
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

C = css.alg_ktripeak.run(G, args.k)

css.common_utility.print_result(G, C)