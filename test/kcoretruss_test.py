import argparse
import css.alg_kcoretruss
import css.common_utility

#############################################################################
parser = argparse.ArgumentParser(description='value k')
parser.add_argument('--k', type=int, default=4,
                    help='user parameter k for k-core and k-truss')

parser.add_argument('--alpha', type=int, default=0.5,
                    help='alpha threshold for k-core truss`')

parser.add_argument('--network', default="../dataset/general_example.dat",
                    help='a folder name containing network.dat')

parser.add_argument('--algorithm', default="kcoretruss",
                    help='specify algorithm name')

args = parser.parse_args()
print(args.k)
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

C = css.alg_kcoretruss.run(G, args.k, args.alpha)

css.common_utility.print_result(G, C)

