import argparse
import css.alg_kpcore
import css.alg_kpcore_jh
import css.common_utility

#############################################################################
parser = argparse.ArgumentParser(description='value k')
parser.add_argument('--k', type=int, default=3,
                    help='user parameter k for k-core and k-truss')

parser.add_argument('--p', type=int, default=0.75,
                    help='fraction p for kp-core`')

parser.add_argument('--network', default="../dataset/general_example.dat",
                    help='a folder name containing network.dat')

parser.add_argument('--algorithm', default="kpcore",
                    help='specify algorithm name')

args = parser.parse_args()
print(args.k)
print(args.p)
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

C = css.alg_kpcore_jh.run(G, args.k, args.p)

css.common_utility.print_result(G, C)


