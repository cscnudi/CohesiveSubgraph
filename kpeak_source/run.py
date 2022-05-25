__author__ = 'priya'

import kpeak_decomposition as kp
import networkx as nx
import numpy as np
import pandas as pd


folderNames = [
'/home/cnudi1/jung/linkcore_data/LA/',
'/home/cnudi1/jung/linkcore_data/enron/',
'/home/cnudi1/jung/linkcore_data/youtube/'
]

for folderName in folderNames : 
	G = nx.read_edgelist(folderName+"/network.dat", data=False)

	# Draws mountain-plot as shown in the paper
	#kp.draw_mountainplot(G, graphname)

	# Draws mountain-plot, including marking each mountain and each component in a mountain
	#kp.draw_mountainplot_components(G, graphname)

	# Returns the peak numbers and core numbers of nodes
	peaknumbers, corenumbers = kp.get_kpeak_decomposition(G)

	#print(peaknumbers);
	#save_dict_to_file(folderName+"/kpeak.dat", peaknumbers)
	(pd.DataFrame.from_dict(data=peaknumbers, orient='index')
   .to_csv(folderName+"/kpeak.dat", header=False))



	
