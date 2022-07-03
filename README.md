# CohesiveSubgraph

An implementation of existing cohesive subgraph discovery algorithm utilizing NetworkX. 

It consists of several cohesive subgraph models including core-based, truss-based, clique-based, and others. 

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

### Default datasets

#### Simple toy network (version 1)

|$V$| = 13, |$E$| = 28

#### Simple toy network (version 2)

|$V$| = 6, |$E$| = 7


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


### Results  

The following plots present the results of the cohesive subgrpah model by utilizing the above parameters and networks. 


| **$k$-core** | **($k,s$-core)** | **($k,h$)-core** |
| :---: | :---: | :---: |
| <img src ="https://user-images.githubusercontent.com/106224155/175987166-b8393d89-ea02-4cc0-be86-de86fb54b9bc.png" width ="300" height="300"/> | <img src ="https://user-images.githubusercontent.com/106224155/176001279-fc58d6b3-4e8b-4225-b0fd-c4a768f2c9b2.png" width ="300" height="300"/>| <img src = "https://user-images.githubusercontent.com/106224155/176001695-aec53068-1449-4b33-8c1d-d61d6a3fc2e2.png" width = "300" height="300"/> |
| **($k,p$)-core** | **$k$-peak** | **$k$-truss** |
| <img src ="https://user-images.githubusercontent.com/106224155/176002452-2ddb3c3d-8ac1-4d56-8e15-3d798ac73900.png" width ="300" height="300"/> | <img src ="https://user-images.githubusercontent.com/106224155/176002358-37ce02fd-43d9-4be3-adec-2b0334d5c464.png" width ="300" height="300"/>| <img src = "https://user-images.githubusercontent.com/106224155/176002198-702f2483-7431-48c7-8414-3f3600e1d013.png" width = "300" height="300"/> |
| **$k$-tripeak** | **max $k$-clique** | **$k$-VCC** |
| <img src ="https://user-images.githubusercontent.com/106224155/176003126-87caa0c7-db8d-4ee1-bdf6-6e8611f4b5f0.png" width ="300" height="300"/> | <img src ="https://user-images.githubusercontent.com/106224155/176003205-20c4236b-7708-4b33-ba5b-2a5091f7cd6a.png" width ="300" height="300"/>| <img src = "https://user-images.githubusercontent.com/106224155/176003275-13ce1164-dad7-489e-b5bb-dfaa0cc3365d.png" width = "300" height="300"/> |
| **$k$-ECC** | **Alphacore** | **$k$-core-truss** |
| <img src ="https://user-images.githubusercontent.com/106224155/176005340-65bbcb46-8705-4a6f-830c-dff8684b20af.png" width ="300" height="300"/> | <img src ="https://user-images.githubusercontent.com/106224155/176005391-850e26c2-fd80-426e-abec-d7ebf1ed9967.png" width ="300" height="300"/>| <img src = "https://user-images.githubusercontent.com/106224155/176005372-fa91d093-ccb5-4e94-aee2-348f42048a13.png" width = "300" height="300"/> |

Note that $k$-distance clique has two solutions. 

<table>
  <tr>
	<td colspan="2"> <b> k-distance clique </b> </td>
  </tr>
	  <tr>
     <td> Solution 1 </td>
    <td> Solution 2</td>
  </tr>
  <tr>
     <td><img src ="https://user-images.githubusercontent.com/106224155/176013972-69258885-e3ce-412d-a293-cec62e5df9f7.png" width ="300" height="300"/></td>
    <td><img src ="https://user-images.githubusercontent.com/106224155/176013977-9b24b3e9-a32d-42b7-8d18-918bc8df2fbd.png" width ="300" height="300"/></td>
  </tr>
</table>



---

## Package Requirements

- python = 3.8
- networkx = 2.7.1
- pandas = 1.1.3
- scipy = 1.4.1

---

## Getting started

Clone repo and install requirements.txt

```sh
git clone https://github.com/cscnudi/CohesiveSubgraph
cd CohesiveSubgraph
pip install -r requirements.txt
```


## How to run the code

- Usage (example script. please run the following code under the `css` folder)

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

C = alg_kcoretruss.run(G, k=5, alpha=1) # run k-core-truss
common_utility.print_result(G, C)


```

- Running the algorithm with user-specificed paramters in console. 

```sh
python run.py --algorithm kcore # run k-core
			--k 3  # parameter k value
			--network example.dat  # network edges file
```

```sh
python run.py --algorithm kscore # run (k,s)-core
			--k 3  # parameter k value
			--s 2  # parameter s value
			--network example.dat  # network edges file
```

```sh
python run.py --algorithm khcore # run (k,h)-core
			--k 5  # parameter k value
			--h 2  # parameter h value
			--network example.dat  # network edges file
```

```sh
python run.py --algorithm kpcore # run (k,p)-core
			--k 3  # parameter k value
			--p 0.5  # parameter h value
			--network example.dat  # network edges file
```

```sh
python run.py --algorithm kpeak # run k-peak
			--k 3  # parameter k value
			--network example.dat  # network edges file
```

```sh
python run.py --algorithm ktruss # run k-truss
			--k 4  # parameter k value
			--network example.dat  # network edges file
```

```sh
python run.py --algorithm ktripeak # run k-tripeak
			--k 4  # parameter k value
			--network example.dat  # network edges file
```

```sh
python run.py --algorithm maxkclique # run max k-clique
			--k 5  # parameter k value
			--network example.dat  # network edges file
```

```sh
python run.py --algorithm kdistanceclique # run k-distance clique
			--k 5  # parameter k value
			--network example.dat  # network edges file
```

```sh
python run.py --algorithm kvcc # run k-VCC
			--k 3  # parameter k value
			--network example.dat  # network edges file
```

```sh
python run.py --algorithm kecc # run k-ECC
			--k 5  # parameter k value
			--network example.dat  # network edges file
```

```sh
python run.py --algorithm alphacore # run Alphacore
			--alpha 0.1  # parameter alpha value						
			--network example.dat  # network edges file
```

```sh
python run.py --algorithm kcoretruss # run k-core-truss
			--k 5  # parameter k value
			--alpha 1  # parameter alpha value						
			--network example.dat  # network edges file
```

---

## Dataset

The datasets are publicly available. You can download the datasets by checking the following references
- Karate [XX?]
- blah blah [ ]
- blah blah [ ] 
- lbha blah [ ]
- 

---

## Reference

[1] Stephen B Seidman. 1983. Network structure and minimum degree. Social networks 5, 3 (1983), 269–287.

[2] Fan Zhang, Long Yuan, Ying Zhang, Lu Qin, Xuemin Lin, and Alexander Zhou. 2018. Discovering strong communities with user engagement and tie strength. DASFAA. Springer, 425–441

[3] Francesco Bonchi, Arijit Khan, and Lorenzo Severini. 2019. Distance-generalized core decomposition. SIGMOD. 006–1023.

[4] Chen Zhang, Fan Zhang, Wenjie Zhang, Boge Liu, Ying Zhang, Lu Qin, and Xuemin Lin. 2020. Exploring finer granularity within the cores: Efficient (k, p)-core computation. ICDE. IEEE, 181–192.

[5] Priya Govindan, Chenghong Wang, Chumeng Xu, Hongyu Duan, and Sucheta Soundarajan. 2017. The k-peak decomposition: Mapping the global structure of graphs. WWW. 1441–1450.

[6] Jonathan Cohen. 2008. Trusses: Cohesive subgraphs for social network analysis. National security agency technical report 16, 3.1 (2008).

[7] Xudong Wu, Long Yuan, Xuemin Lin, Shiyu Yang, and Wenjie Zhang. 2019. Towards efficient k-tripeak decomposition on large graphs. DASFAA. Springer, 604–621.

[8] Balabhaskar Balasundaram, Sergiy Butenko, and Svyatoslav Trukhanov. 2005. Novel approaches for analyzing biological networks. J. Comb. Optim. 10, 1 (2005), 23–39.

[9] Shahram Shahinpour and Sergiy Butenko. 2013. Algorithms for the maximum k-club problem in graphs. J. Comb. Optim. 26, 3 (2013), 520554

[13]

[14] Tianhao Wang, Yong Zhang, Francis YL Chin, Hing-Fung Ting, Yung H Tsin, and Sheung-Hung Poon. 2015. A simple algorithm for finding all k-edge-connected components. Plos one 10, 9 (2015), e0136264.

[15] Friedhelm Victor, Cuneyt G Akcora, Yulia R Gel, and Murat Kantarcioglu. 2021. Alphacore: Data Depth based Core Decomposition. SIGKDD. 1625–1633.

[16] Zhenjun Li, Yunting Lu, Wei-Peng Zhang, Rong-Hua Li, Jun Guo, Xin Huang, and Rui Mao. 2018. Discovering hierarchical subgraphs of k-core-truss. DSE 32 (2018)136–149

---

## Contact

Please feel free to contact @Jeongseon Kim (jeongseon@g.cnu.ac.kr) if you have any questions about the implementation. 

---

## Thanks to
We really appreciate all the authors of the papers [1-16], networkX and Priya Govindan.
We utilize the code (https://github.com/priyagovindan/kpeak) for k-peak computation. We tried to contact to the first author (Priya Govindan), but failed to contact to her. To get the full code with visualization, please check the above github link. We sincerely thank to Priya Govindan to share the code. 
