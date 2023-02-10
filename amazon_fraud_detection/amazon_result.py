import os
import argparse
from collections import defaultdict
import pandas as pd


def setup_file_list():
    files = os.listdir()
    network_file_list = []
    for file in files:
        if file[-4:] == 'json':
            network_file_list.append(file[:-5])

    return network_file_list

def read_mapping(file_,path=None):
    mapping_ = defaultdict(dict)
    if path is None:
        path = "{}_{}_{}".format(file_, args.t, args.threshold)

    with open("./{}/{}".format(path,'index.txt'), 'r') as file:
        lines = file.readlines()

        for line in lines:
            tokens = line.strip().split('\t')
            mapping_[tokens[0]]['mapping'] = tokens[1]
            mapping_[tokens[0]]['edgetype'] = tokens[2]

    file.close()

    return mapping_


def arrange_algorithms(_file):

    mapping = read_mapping(_file)
    dir_list = os.listdir('./{}_{}_{}'.format(_file, args.t, args.threshold))
    df = pd.DataFrame()
    for filename in dir_list:
        if filename != 'network.dat' and filename != 'network_mapping.dat' and filename != 'index.txt' and filename != 'arrange.xlsx':
            # print(_file,filename)
            with open('./{}_{}_{}/{}'.format(_file, args.t, args.threshold,filename), 'r') as file:
                i_index = 0
                lines = file.readlines()
                for line in lines:
                    tokens = line.strip().split('\t')
                    if len(tokens) != 2:
                        communities = list(map(str, tokens[0].split()))
                        fraud_count = 0
                        for community in communities:
                            if mapping[community]['edgetype'] == '2':
                                fraud_count = fraud_count + 1

                        fraud_ratio =  fraud_count/len(communities)
                        df.loc[i_index, filename[:-4]] = fraud_ratio
                        i_index = i_index + 1

            file.close()
    # print(df)
    df.to_excel('./{}_{}_{}/{}_{}_{}_result.xlsx'.format(_file, args.t, args.threshold,_file, args.t, args.threshold))


def change_variable(filename):
    # print(filename)
    algorithm_, variable_ = filename[:-4].split('_', maxsplit=1)
    mapping_variable = {'kcore': {'k_3':'p1','k_5':'p2','k_7':'p3','k_9':'p4'},
                        'kscore': {'k_3_s_2':'p1','k_3_s_3':'p2','k_5_s_2':'p3','k_5_s_3':'p4'},
                        'khcore': {'k_3_h_2':'p1','k_5_h_2':'p2','k_7_h_2':'p3','k_9_h_2':'p4'},
                        'kpcore': {'k_3_p_0.4':'p1','k_3_p_0.6':'p2','k_5_p_0.4':'p3','k_5_p_0.6':'p4'},
                        'kpeak': {'k_3':'p1','k_5':'p2','k_7':'p3','k_9':'p4'},
                        'ktruss': {'k_4':'p1','k_6':'p2','k_8':'p3','k_10':'p4'},
                        'ktripeak': {'k_4':'p1','k_6':'p2','k_8':'p3','k_10':'p4'},
                        'maxkclique': {'k_3':'p1','k_5':'p2','k_7':'p3','k_9':'p4'},
                        'kvcc': {'k_3':'p1','k_5':'p2','k_7':'p3','k_9':'p4'},
                        'kecc': {'k_3':'p1','k_5':'p2','k_7':'p3','k_9':'p4'},
                        'alphacore': {'alpha_0.2':'p1','alpha_0.4':'p2','alpha_0.6':'p3','alpha_0.8':'p4'},
                        'kcoretruss': {'k_4_alpha_1.0':'p1','k_6_alpha_1.0':'p2','k_8_alpha_1.0':'p3','k_10_alpha_1.0':'p4'},
                        'scan':{'k_3_epsilon_0.4':'p1','k_3_epsilon_0.6':'p2','k_5_epsilon_0.4':'p3','k_5_epsilon_0.6':'p4'}}
    if mapping_variable[algorithm_].get(variable_) is None:
        pass
    else:
        variable_ = mapping_variable[algorithm_][variable_]
    return algorithm_,variable_


def result_to_excelfile():
    dir_list = setup_file_list()
    # print(os.getcwd())
    # print(dir_list)
    df = pd.DataFrame(columns=['Algorithm','Variable','CCid','Ratio','Name'])
    i_index = 0
    for folder in dir_list:
        paths = '{}_{}_{}'.format(folder,args.t, args.threshold)
        _file_list = os.listdir(paths)
        # print(_file_list)
        mapping = read_mapping(folder,path=paths)

        for file_name in _file_list:
            if file_name[:-4] != 'index' and file_name[-4:] != 'xlsx' and file_name[:-4] != 'network' and file_name[:-4] != 'network_mapping' and file_name != 'index.txt.bak':
                print(file_name)
                # algorithm, variable = file_name[:-4].split('_', maxsplit=1)
                algorithm, variable = change_variable(file_name)
                with open('{}/{}'.format(paths, file_name), 'r') as _file:
                    ccid = 1
                    lines = _file.readlines()
                    for line in lines:
                        tokens = line.strip().split('\t')
                        if len(tokens) != 2:
                            communities = list(map(str, tokens[0].split()))
                            fraud_count = 0

                            for community in communities:
                                if mapping[community]['edgetype'] == '2':
                                    fraud_count = fraud_count + 1

                            fraud_ratio = fraud_count / len(communities)
                            # df.iloc[i_index] = [algorithm,variable,ccid,fraud_ratio]
                            df.loc[i_index, 'Algorithm'] = algorithm
                            df.loc[i_index, 'Variable'] = variable
                            df.loc[i_index, 'CCid'] = ccid
                            df.loc[i_index, 'Ratio'] = fraud_ratio
                            df.loc[i_index, 'Name'] = folder[:-8]

                            i_index = i_index + 1
                            ccid = ccid + 1

                _file.close()

    df.to_excel('result_amazon_fraud.xlsx')


parser = argparse.ArgumentParser(description='value k')
parser.add_argument('--t', type=int, default=3,
                    help='user parameter t')

parser.add_argument('--threshold', type=float, default=0.3,
                    help='threshold lambda')
args = parser.parse_args()

if __name__ == '__main__':
    os.chdir('./dataset/amazon/')
    file_list = setup_file_list()
    for file in file_list:
        arrange_algorithms(file)
    result_to_excelfile()


