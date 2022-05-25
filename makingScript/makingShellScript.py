import networkx as nx
import math
import os
import fnmatch

#folderName = "D://Data//CSS_data/real/karate/"
folderName = "D://Data//CSS_data/syn_default/" # network.dat
# =>


def setupFileList(fName) :
    networkFileList = []
    for root, dirs, files in os.walk(fName):
        path = root.split(os.sep)
        for file in files:
            if file == "network.dat" :
                root = root.replace("D://Data//", "/root/jung/")
                networkFileList.append((root+"/").replace("\\", "/"))
    return networkFileList


def initialize(opt) :
    # kcore setup

    opt['alphacore'] = dict()
    opt['alphacore']['alpha'] = [0.3,0.4,0.5,0.6]

    opt['kcore'] = dict()
    opt['kcore']['k'] = [3, 4, 5, 6]

    opt['kecc'] = dict()
    opt['kecc']['k'] = [3, 4, 5, 6]

    opt['khcore'] = dict()
    opt['khcore']['k'] = [3, 4, 5, 6]
    opt['khcore']['h'] = [1,2,3]

    opt['kpcore'] = dict()
    opt['kpcore']['k'] = [3, 4, 5, 6]
    opt['kpcore']['p'] = [0.3,0.4,0.5,0.6]

    opt['kscore'] = dict()
    opt['kscore']['k'] = [3, 4, 5, 6]
    opt['kscore']['s'] = [2,3,4,5]

    opt['kpeak'] = dict()
    opt['kpeak']['k'] = [3, 4, 5, 6]


    opt['ktruss'] = dict()
    opt['ktruss']['k'] = [3,4,5,6]

    opt['kvcc'] = dict()
    opt['kvcc']['k'] = [3, 4, 5, 6]


    opt['MkMFD'] = dict()
    opt['MkMFD']['k'] = [2,3,4,5]

    opt['kdistanceclique'] = dict()
    opt['kdistanceclique']['k'] = [1,2,3]

    opt['maxkclique'] = dict()
    opt['maxkclique']['k'] = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


def script(_p) :
    print('nohup python ./css/run.py '+_p + " & ")

def printScript(_map, _aname, _pname) :
    map = _map[_aname]

    if len(map.keys()) == 1 :
        for key in map.keys():
            for value in map[key]:
                param = " --algorithm "+_aname+ " --network "+_pname+ "network.dat --"+key+" "+str(value)
                script(param)

    if len(map.keys()) == 2 :
        keyList = list(map.keys())
        valueList = [map[e] for e in map.keys()]

        v1 = (valueList[0])
        v2 = (valueList[1])


        for elem1 in v1:
            for elem2 in v2:
                param = "--algorithm "+_aname+ " --network "+_pname+ "/network.dat --" + keyList[0] + " " + str(elem1);
                param = param + " --" + keyList[1] + " " + str(elem2);
                script(param)


def printAll(opt, parentFolderList) :
    for algName in opt.keys():
        for pName in pList :
            printScript(opt, algName, pName)


if __name__ == '__main__':
    options = dict()

    pList = setupFileList(folderName)
    initialize(options)

    printAll(options, pList)




