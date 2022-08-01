import argparse
import networkx as nx
import alg_alphacore
import alg_kcore
import alg_kecc
import alg_khcore
import alg_kpcore
import alg_kpcore_jh
import alg_kpeak
import alg_kscore
import alg_ktruss
import alg_kvcc
import alg_ktripeak
import alg_MkMFD
import alg_kdistance_clique
import alg_ksize_clique
import os
import time
import sys
import alg_ksize_clique, alg_kdistance_clique, alg_MkMFD,common_utility
import alg_kcoretruss, alg_scan

sys.setrecursionlimit(10000)


def get_base(file_path) :
    path = os.path.dirname(file_path)
    return path+"/"


def get_user_param(args_set, _alg) :

    ret = dict()

    if _alg == 'alphacore':
        ret['alpha'] = args_set.alpha

    if _alg == 'kcore':
        ret['k'] = args_set.k

    if _alg == 'kecc':
        ret['k'] = args_set.k

    if _alg == 'khcore':
        ret['k'] = args_set.k
        ret['h'] = args_set.h

    if _alg == 'kpcore':
        ret['k'] = args_set.k
        ret['p'] = args_set.p

    if _alg == 'kpeak':
        ret['k'] = args_set.k

    if _alg == 'kscore':
        ret['k'] = args_set.k
        ret['s'] = args_set.s

    if _alg == 'ktruss':
        ret['k'] = args_set.k

    if _alg == 'kvcc':
        ret['k'] = args_set.k

    if _alg == 'ktripeak':
        ret['k'] = args_set.k

    if _alg == 'MkMFD':
        ret['k'] = args_set.k

    if _alg == 'kdistanceclique':
        ret['k'] = args_set.k

    if _alg == 'maxkclique':
        ret['k'] = args_set.k

    if _alg == 'kcoretruss':
        ret['k'] = args_set.k
        ret['alpha'] = args_set.alpha

    if _alg == 'scan':
        ret['k'] = args_set.k
        ret['epsilon'] = args_set.epsilon

    return ret

#############################################################################
parser = argparse.ArgumentParser(description='value k')
parser.add_argument('--k', type=int, default=3,
                    help='user parameter k')

parser.add_argument('--h', type=int, default=2,
                    help='threshold h for kh-core`')

parser.add_argument('--p', type=float, default=0.2,
                    help='threshold p for kp-core`')

parser.add_argument('--s', type=int, default=3,
                    help='threshold s for ks-core`')

parser.add_argument('--alpha', type=float, default=1,
                    help='alpha threshold for alpha-core or k-core-truss`')

parser.add_argument('--epsilon', type=float, default=0.5,
                    help='alpha threshold for alpha-core or k-core-truss`')

parser.add_argument('--network', default="../dataset/karate/network.dat",
                    help='a folder name containing network.dat')

parser.add_argument('--algorithm', default="kcoretruss",
                    help='specify algorithm name')

parser.add_argument('--scalability', type=bool, default=False,
                    help='for scalability test')

parser.add_argument('--fullstatistics', type=bool, default=False,
                    help='for speed up')

parser.add_argument('--majorstatistics', type=bool, default=True,
                    help='for speed up')


args = parser.parse_args()
print("network ", args.network)
print("algorithm ", args.algorithm)

user_params = get_user_param(args, args.algorithm)

output = get_base(args.network)
output = output + args.algorithm
for key in user_params.keys() :
    print("params ", key, user_params[key])
    output = output + "_"+str(key)+"_"+str(user_params[key])
output = output+".dat"
print("output", output)

#############################################################################
#############################################################################

#############################################################################
# Global Parameter
G = None
C = None
#############################################################################

#############################################################################
# check integrity
satisfying_integrity = common_utility.check_integrity(args)

if not satisfying_integrity:
    print('Input parameter has errors, please check the parameters')
    quit()

#############################################################################
# read network
G = common_utility.readEdgeList(args.network)
G.remove_edges_from(nx.selfloop_edges(G))
#############################################################################

start_time = time.time()


if args.algorithm == 'alphacore':
    C = alg_alphacore.run(G, args.alpha)

if args.algorithm == 'kcore':
    C = alg_kcore.run(G, args.k)

if args.algorithm == 'kecc':
    C = alg_kecc.run(G, args.k)


if args.algorithm == 'ktripeak':
    C = alg_ktripeak.run(G, args.k)

if args.algorithm == 'khcore':
    C = alg_khcore.run(G, args.k, args.h)

if args.algorithm == 'kpcore':
    C = alg_kpcore_jh.run(G, args.k, args.p)

if args.algorithm == 'kpeak':
    C = alg_kpeak.run(G, args.k)

if args.algorithm == 'kscore':
    C = alg_kscore.run(G, args.k, args.s)

if args.algorithm == 'ktruss':
    C = alg_ktruss.run(G, args.k)

if args.algorithm == 'kvcc':
    C = alg_kvcc.run(G, args.k)

if args.algorithm == 'MkMFD':
    C = alg_MkMFD.run(G, args.k)

if args.algorithm == 'kdistanceclique':
    C = alg_kdistance_clique.run(G, args.k)

if args.algorithm == 'maxkclique':
    C = alg_ksize_clique.run(G, args.k)

if args.algorithm == 'kcoretruss':
    C = alg_kcoretruss.run(G, args.k, args.alpha)

if args.algorithm == 'scan':
    C = alg_scan.run(G, args.k, args.epsilon)


run_time = time.time() - start_time

result = list()
if C != None :
    result = list(C)
print("----------------------------------------------------------")
for comp in result:
    comp = [int(x) for x in comp]
    comp = sorted(comp, reverse=False)
    for u in list(comp):
        print(u, ' ', end="")
    print("")
print("----------------------------------------------------------")


if args.fullstatistics is True :
    mod, local_mod, v_density, e_density, inv_cond, diam, size = common_utility.metric(G, result)
    print("resultant_statistic ", run_time, mod, local_mod, v_density, e_density, inv_cond, diam, size)

    with open(output, 'w') as f:
        f.write("seconds" + "\t" + str(run_time) + '\n')
        f.write("modularity" + "\t" + str(mod) + '\n')
        f.write("local_modularity" + "\t" + str(local_mod) + '\n')
        f.write("v_density" + "\t" + str(v_density) + '\n')
        f.write("e_density" + "\t" + str(e_density) + '\n')
        f.write("inv_cond" + "\t" + str(inv_cond) + '\n')
        f.write("diam" + "\t" + str(diam) + '\n')
        f.write("size" + "\t" + str(size) + '\n')

        for comp in result:
            comp = [int(x) for x in comp]
            comp = sorted(comp, reverse=False)
            for u in list(comp):
                f.write(str(u) + " ")
            f.write("\n")

    f.close()

else :
    mod, v_density, e_density, inv_cond, size = common_utility.fewMetric(G, result)
    print("resultant_statistic ", run_time, mod, v_density, e_density, inv_cond, size)



    with open(output, 'w') as f:
        f.write("seconds" + "\t" + str(run_time) + '\n')
        f.write("modularity" + "\t" + str(mod) + '\n')
        f.write("v_density" + "\t" + str(v_density) + '\n')
        f.write("e_density" + "\t" + str(e_density) + '\n')
        f.write("inv_cond" + "\t" + str(inv_cond) + '\n')
        f.write("size" + "\t" + str(size) + '\n')

        for comp in result:
            comp = [int(x) for x in comp]
            comp = sorted(comp, reverse=False)
            for u in list(comp):
                f.write(str(u) + " ")
            f.write("\n")

    f.close()

