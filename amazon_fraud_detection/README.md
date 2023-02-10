# AmazonFraudDetection

An implementation of existing cohesive subgraph discovery algorithm utilizing NetworkX. 

It consists of several cohesive subgraph models including core-based, truss-based, clique-based, and others. 


---

## Package Requirements

- networkx = 2.7.1
- pandas = 1.1.3
- scipy = 1.4.1
- cdlib == 0.2.6
- numpy == 1.21
- openpyxl == 3.1.0

---

## Getting started

Clone repo and install requirements.txt in a Python =3.8 environment.

```sh
git clone https://github.com/cscnudi/CohesiveSubgraph
cd CohesiveSubgraph/amazon_fraud_detection
pip install -r requirements.txt
```


## How to run the code

- Usage (example script. please run the following code under the `css` folder)

- After downloading the dataset, put the json file under the amazon folder in the Dataset folder.


```bash
├─dataset
│  │  general_example.dat
│  ├─amazon
│  │      Amazon_Instant_Video_5.json
│  │      Clothing_Shoes_and_Jewelry_5.json
│  │      Musical_Instruments_5.json
│  │      Sports_and_Outdoors_5.json
│  └─polblogs
│          
```
- Preprocessing the Amazon dataset.

```sh
python ./amazon_fraud_detection/generate_amazon_dataset.py
```

- Running the algorithm with user-specified parameters in the console. (Refer to the amazon_shell_script.txt file.)

- Running code to arrange the results.

```sh
python ./amazon_fraud_detection/amazon_result.py
```


---

## Dataset

The datasets are publicly available. You can download the datasets by checking the url
- http://jmcauley.ucsd.edu/data/amazon/


