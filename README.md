# CohesiveSubgraph

A Python library to compute Cohesive subgraphs on NetworkX graph.

This work computes Core-based, Triangle-based, Clique-based, connected-component based, and other approaches.

### CORE-BASED APPROACHES

- $k$-core [1]
- $(k,s)$-core [2]
- $(k,h)$-core [3]
- $(k,p)$-core [4]
- $k$-peak [5]

### TRIANGLE-BASED APPROACHES

- $k$-truss [6]
- $k$-tripeak [7]

### CLIQUE-BASED APPROACHES

- $k$-size clique [8]
- $k$-distance clique [8]
- max $k$-clique [8]
- $k$-clan [9]
- $k$-club [9]

### CONNECTED-COMPONENT BASED APPROACHES

- $k$-VCC($k$-vertex connected component) [13]
- $k$-ECC($k$-edge connected component) [14]

### OTHER APPROACHES

- Alphacore [15]
- $k$-core-truss [16]

---
## Parameter Setting & Result 

### Parameter Settings

| Algorithms | parameter | example |
| :---: | :---: | :---: |
| $k$-core | $k$=3 | simple toy network |
| $(k,s)$-core | $k$ = 3, $s$ = 2 | [2] Fig. 2.|
| $(k,h)$-core | $k$ = 5, $h$ = 2 | [3] Fig. 1.|
| $(k,p)$-core | $k$ = 3, $p$ = 0.5 | [4] Fig. 1.|
| $k$-peak | $k$ = 3 | simple toy network |
| $k$-truss | $k$ = 4 | simple toy network |
| $k$-tripeak | $k$ = 4 | [7] Fig. 2.|
| max $k$-clique | $k$ = 5 | simple toy network 2|
| $k$-distance clique | $k$ = 2 | simple toy network 2|
| $k$-VCC | $k$ = 3 | simple toy network |
| $k$-ECC | $k$ = 5 | simple toy network |
| Alphacore | $\alpha$ = 0.1 | simple toy network |
| $k$-core-truss | $k$=3, $\alpha$ = 1 | [16] Fig. 2.|


### Result

The plot of the results of the previous parameter setting is shown.


| $k$-core | ($k,s$-core) | ($k,h$)-core |
| :---: | :---: | :---: |
| <img src ="https://user-images.githubusercontent.com/106224155/175987166-b8393d89-ea02-4cc0-be86-de86fb54b9bc.png" width ="300" height="300"/> | <img src ="https://user-images.githubusercontent.com/106224155/176001279-fc58d6b3-4e8b-4225-b0fd-c4a768f2c9b2.png" width ="300" height="300"/>| <img src = "https://user-images.githubusercontent.com/106224155/176001695-aec53068-1449-4b33-8c1d-d61d6a3fc2e2.png" width = "300" height="300"/> |
| ($k,p$)-core | $k$-peak | $k$-truss |
| <img src ="https://user-images.githubusercontent.com/106224155/176002452-2ddb3c3d-8ac1-4d56-8e15-3d798ac73900.png" width ="300" height="300"/> | <img src ="https://user-images.githubusercontent.com/106224155/176002358-37ce02fd-43d9-4be3-adec-2b0334d5c464.png" width ="300" height="300"/>| <img src = "https://user-images.githubusercontent.com/106224155/176002198-702f2483-7431-48c7-8414-3f3600e1d013.png" width = "300" height="300"/> |
| $k$-tripeak | max $k$-clique | $k$-VCC |
| <img src ="https://user-images.githubusercontent.com/106224155/176003126-87caa0c7-db8d-4ee1-bdf6-6e8611f4b5f0.png" width ="300" height="300"/> | <img src ="https://user-images.githubusercontent.com/106224155/176003205-20c4236b-7708-4b33-ba5b-2a5091f7cd6a.png" width ="300" height="300"/>| <img src = "https://user-images.githubusercontent.com/106224155/176003275-13ce1164-dad7-489e-b5bb-dfaa0cc3365d.png" width = "300" height="300"/> |




---

## Package Requirements

- python = 3.8
- networkx = 2.7.1
- pandas = 1.1.3
- scipy = 1.4.1

---



## How to use
We have parameter 
k,network,algorithm
First, move test folder and we 

- Usage
```python
import networkx as nx
from css import alg_kcore,alg_alphacore, alg_kecc, alg_khcore, alg_kpcore, alg_kpeak, alg_kscore, alg_ktruss, alg_kvcc
from css import alg_kdistance_clique, alg_ksize_clique, alg_ktripeak, alg_alg_kcoretruss, common_utility

G = nx.karate_club_graph() # input graph

C = alg_kcore.run(G, k=3) # run k-core 
common_utility.print_result(G, C)

C = alg_kscore.run(G, k=3,s=2) # run (k,s)-core 
common_utility.print_result(G, C)

C = alg_khcore.run(G, k=5, h=2) # run (k,h)-core
common_utility.print_result(G, C)

C = alg_kpcore.run(G, k=3,p=0.5) # run (k,p)-core 
common_utility.print_result(G, C)

C = alg_kpeak.run(G, k=3) # run k-peak 
common_utility.print_result(G, C)

C = alg_ktruss.run(G, k=4) # run k-truss
common_utility.print_result(G, C)

C = alg_ktripeak.run(G, k=4) # run k-tripeak
common_utility.print_result(G, C)

C = alg_ksize_clique.run(G, k=5) # max k-clique
common_utility.print_result(G, C)

C = alg_kdistance_clique.run(G, k=5) # run k-distance clique
common_utility.print_result(G, C)

C = alg_kvcc.run(G, k=3) # run k-VCC
common_utility.print_result(G, C)

C = alg_kecc.run(G, k=5) # run k-ECC
common_utility.print_result(G, C)

C = alg_alphacore.run(G, alpha=0.1) # run Alphacore
common_utility.print_result(G, C)

C = alg_kcoretruss.run(G, k=5) # run k-core-truss
common_utility.print_result(G, C)


```

- Run test file


Go to test folder and run.


```sh
python kcore_test.py # run k-core
			-k 3  # parameter k value
			--network example.dat  # network edges file
```

```sh
python kscore_test.py # run (k,s)-core
			--k 3  # parameter k value
			--s 2  # parameter s value
			--network example.dat  # network edges file
```

```sh
python khcore_test.py # run (k,h)-core
			--k 5  # parameter k value
			--h 2  # parameter h value
			--network example.dat  # network edges file
```

```sh
python kpcore_test.py # run (k,p)-core
			--k 3  # parameter k value
			--p 0.5  # parameter h value
			--network example.dat  # network edges file
```

```sh
python kpeak_test.py # run k-peak
			--k 3  # parameter k value
			--network example.dat  # network edges file
```

```sh
python ktruss_test.py # run k-truss
			--k 4  # parameter k value
			--network example.dat  # network edges file
```

```sh
python ktripeak_test.py # run k-tripeak
			--k 4  # parameter k value
			--network example.dat  # network edges file
```

```sh
python ksize_clique_test.py # run max k-clique
			--k 5  # parameter k value
			--network example.dat  # network edges file
```

```sh
python kdistance_clique_test.py # run max k-clique
			--k 5  # parameter k value
			--network example.dat  # network edges file
```

```sh
python kvcc_test.py # run k-VCC
		--k 3  # parameter k value
		--network example.dat  # network edges file
```

```sh
python kecc_test.py # run k-ECC
		--k 5  # parameter k value
		--network example.dat  # network edges file
```

```sh
python alphacore_test.py # run Alphacore
			--alpha 0.1  # parameter alpha value						
			--network example.dat  # network edges file
```

```sh
python kcoretruss_test.py # run k-core-truss
			--k 5  # parameter k value
			--network example.dat  # network edges file
```

---

## Code

---

## Dataset

- Amazon : [https://snap.stanford.edu/data/com-Amazon.html](https://snap.stanford.edu/data/com-Amazon.html)
- Karate : [https://networkrepository.com/soc-karate.php](https://networkrepository.com/soc-karate.php)
- Polblogs : [https://networkrepository.com/polblogs.php](https://networkrepository.com/polblogs.php)

### other Dataset

we used in paper 

---

## Reference

[1] Stephen B Seidman. 1983. Network structure and minimum degree. Social networks 5, 3 (1983), 269–287.

[2] Fan Zhang, Long Yuan, Ying Zhang, Lu Qin, Xuemin Lin, and Alexander Zhou. 2018. Discovering strong communities with user engagement and tie strength. In International Conference on Database Systems for Advanced Applications. Springer, 425–441

[3] Francesco Bonchi, Arijit Khan, and Lorenzo Severini. 2019. Distance-generalized core decomposition. In Proceedings of the 2019 International Conference on Management of Data. 006–1023.

[4] Chen Zhang, Fan Zhang, Wenjie Zhang, Boge Liu, Ying Zhang, Lu Qin, and Xuemin Lin. 2020. Exploring finer granularity within the cores: Efficient (k, p)- core computation. In 2020 IEEE 36th International Conference on Data Engineering (ICDE). IEEE, 181–192.

[5] Priya Govindan, Chenghong Wang, Chumeng Xu, Hongyu Duan, and Sucheta Soundarajan. 2017. The k-peak decomposition: Mapping the global structure of graphs. In Proceedings of the 26th International Conference on World Wide Web. 1441–1450.

[6] Jonathan Cohen. 2008. Trusses: Cohesive subgraphs for social network analysis. National security agency technical report 16, 3.1 (2008).

[7] Xudong Wu, Long Yuan, Xuemin Lin, Shiyu Yang, and Wenjie Zhang. 2019. Towards efficient k-tripeak decomposition on large graphs. In International Conference on Database Systems for Advanced Applications. Springer, 604–621.

[8] Balabhaskar Balasundaram, Sergiy Butenko, and Svyatoslav Trukhanov. 2005. Novel approaches for analyzing biological networks. Journal of Combinatorial Optimization 10, 1 (2005), 23–39.

[9] Shahram Shahinpour and Sergiy Butenko. 2013. Algorithms for the maximum k-club problem in graphs. Journal of Combinatorial Optimization 26, 3 (2013), 520554

[13]

[14] Tianhao Wang, Yong Zhang, Francis YL Chin, Hing-Fung Ting, Yung H Tsin, and Sheung-Hung Poon. 2015. A simple algorithm for finding all k-edge-connected components. Plos one 10, 9 (2015), e0136264.

[15] Friedhelm Victor, Cuneyt G Akcora, Yulia R Gel, and Murat Kantarcioglu. 2021. Alphacore: Data Depth based Core Decomposition. In Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery & Data Mining. 1625–1633.

[16] Zhenjun Li, Yunting Lu, Wei-Peng Zhang, Rong-Hua Li, Jun Guo, Xin Huang, and Rui Mao. 2018. Discovering hierarchical subgraphs of k-core-truss. Data Science and Engineering 32 (2018)136–149

---

## Contact

Please contact ~~

---

## Cite
